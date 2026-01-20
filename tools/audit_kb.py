#!/usr/bin/env python3
"""Audit the KB for traceability and review hotspots.

This does NOT prove legal correctness. It produces a review report to help humans
verify factual/legal statements.

Checks:
- Missing source references in topic files.
- "Claim-like" lines that contain numbers/dates/strong obligation words but lack
  nearby sources citations.
- Sources with non-200 HTTP status.
- Sources that are very small (often nav-only or error pages).

Usage:
  python3 tools/audit_kb.py
  python3 tools/audit_kb.py --country spain-immigration
  python3 tools/audit_kb.py --write-report AUDIT.md

Exit codes:
- 0: no issues detected by heuristics
- 1: issues detected
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional, Tuple


CLAIM_WORDS_ZH = [
    '必須', '不得', '禁止', '應', '需要', '可', '可以', '允許', '必需', '必然', '一定',
    '罰', '處罰', '罰款', '遣返', '驅逐', '取消', '拒絕', '無效',
]

CLAIM_WORDS_EN = [
    'must', 'must not', 'shall', 'may not', 'required', 'requirement',
    'prohibited', 'ban', 'fine', 'penalty', 'deport', 'remove', 'cancel', 'refuse',
]

DATE_NUMBER_RE = re.compile(
    r'\b(\d{4}[-/.]\d{1,2}[-/.]\d{1,2}|\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4})\b|\b\d+\b'
)

SOURCE_CITATION_RE = re.compile(r'`[^`]*?/sources/[^`]+?\.md`')


@dataclass
class Finding:
    level: str  # 'warn' | 'error'
    country: str
    file: str
    line: int
    message: str


def list_countries(root: str, only: Optional[str] = None) -> List[str]:
    dirs = []
    for name in os.listdir(root):
        if only and name != only:
            continue
        p = os.path.join(root, name)
        if os.path.isdir(p) and name.endswith('-immigration'):
            dirs.append(name)
    return sorted(dirs)


def read_lines(path: str) -> List[str]:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read().splitlines()


def has_nearby_source(lines: List[str], idx: int, window: int = 6) -> bool:
    lo = max(0, idx - window)
    hi = min(len(lines), idx + window + 1)
    blob = '\n'.join(lines[lo:hi])
    return bool(SOURCE_CITATION_RE.search(blob))


def should_ignore_line(line: str) -> bool:
    s = line.strip()
    if not s:
        return True
    # Common metadata lines
    if s.startswith('最後更新') or s.startswith('**標籤**'):
        return True
    if s.startswith('> 注意') or s.startswith('> 說明'):
        return True
    return False


def looks_like_claim(line: str) -> bool:
    s = line.strip()
    if should_ignore_line(line):
        return False
    # ignore headings and pure list items that are just links
    if s.startswith('#'):
        return False
    if s.startswith('|') and s.endswith('|'):
        return False

    low = s.lower()

    if DATE_NUMBER_RE.search(s):
        return True

    for w in CLAIM_WORDS_ZH:
        if w in s:
            return True

    for w in CLAIM_WORDS_EN:
        if w in low:
            return True

    return False


def scan_topic_file(country: str, path: str) -> List[Finding]:
    findings: List[Finding] = []
    lines = read_lines(path)

    # missing refs check
    for i, line in enumerate(lines):
        for m in re.finditer(r'`([^`]*?/sources/[^`]+?\.md)`', line):
            ref = m.group(1)
            if not os.path.exists(ref):
                findings.append(
                    Finding(
                        level='error',
                        country=country,
                        file=path,
                        line=i + 1,
                        message=f'Missing referenced source: {ref}',
                    )
                )

    # claim-like lines without nearby sources
    for i, line in enumerate(lines):
        if not looks_like_claim(line):
            continue
        if SOURCE_CITATION_RE.search(line):
            continue
        if not has_nearby_source(lines, i, window=6):
            findings.append(
                Finding(
                    level='warn',
                    country=country,
                    file=path,
                    line=i + 1,
                    message='Claim-like line without nearby sources citation',
                )
            )

    return findings


def scan_sources(country: str, root: str) -> List[Finding]:
    findings: List[Finding] = []
    src_dir = os.path.join(root, country, 'sources')
    if not os.path.isdir(src_dir):
        return findings

    for p in sorted(glob.glob(os.path.join(src_dir, '*.md'))):
        head = open(p, 'r', encoding='utf-8', errors='ignore').read(1200)
        m = re.search(r'^HTTP status:\s*(\d+)', head, re.M)
        if m:
            st = int(m.group(1))
            if st >= 400:
                findings.append(
                    Finding('error', country, p, 1, f'Non-200 source HTTP status: {st}')
                )
        if os.path.getsize(p) < 1200:
            findings.append(
                Finding('warn', country, p, 1, 'Very small source file (<1.2KB); likely nav-only/error/JS-driven')
            )

    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--country', default=None, help='Limit to a single country folder (e.g., spain-immigration)')
    ap.add_argument('--include-meta', action='store_true', help='Also scan README.md and 99-sources-index.md and metadata lines like 最後更新')
    ap.add_argument('--write-report', default=None, help='Write a Markdown report to this path')
    args = ap.parse_args()

    root = os.getcwd()
    countries = list_countries(root, only=args.country)
    findings: List[Finding] = []

    for c in countries:
        # topic files
        for p in sorted(glob.glob(os.path.join(root, c, '*.md'))):
            base=os.path.basename(p)
            if (not args.include_meta) and base in {'README.md','99-sources-index.md'}:
                continue
            if os.path.getsize(p) == 0:
                findings.append(Finding('error', c, p, 1, 'Empty topic file'))
                continue
            findings.extend(scan_topic_file(c, p))
        findings.extend(scan_sources(c, root))

    # format report
    report: List[str] = []
    report.append('# KB 審查報告（Heuristic Audit）')
    report.append('')
    report.append(f'生成時間(UTC)：{datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}  ')
    report.append('**注意**：此報告只提供「需要人工核對」的線索，不能證明法律正確性。')
    report.append('')

    if not findings:
        report.append('未發現問題（依目前的自動化規則）。')
    else:
        by_level: Dict[str, List[Finding]] = {'error': [], 'warn': []}
        for f in findings:
            by_level.setdefault(f.level, []).append(f)

        for level in ['error', 'warn']:
            items = by_level.get(level, [])
            if not items:
                continue
            report.append(f'## {level.upper()} ({len(items)})')
            for f in items:
                report.append(f"- {f.country}: `{f.file}`:{f.line} — {f.message}")
            report.append('')

    out = '\n'.join(report) + '\n'
    if args.write_report:
        with open(args.write_report, 'w', encoding='utf-8') as f:
            f.write(out)
    else:
        print(out)

    return 1 if findings else 0


if __name__ == '__main__':
    raise SystemExit(main())
