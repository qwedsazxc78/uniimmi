#!/usr/bin/env python3
"""Audit the KB for traceability and review hotspots.

This does NOT prove legal correctness. It produces a review report to help humans
verify factual/legal statements.

Checks:
- Missing source references in topic files.
- "Claim-like" lines that contain numbers/dates/strong obligation words but lack
  nearby sources citations.
- Sources with non-200 HTTP status (with a known-issues allowlist).
- Sources that are very small (often nav-only or error pages).

Exit codes:
- 0: no issues detected by heuristics (or threshold allows it)
- 1: issues detected (depending on --fail-on)
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple

KNOWN_ISSUES_PATH = os.path.join('tools', 'known_issues.json')

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


def load_known_issues() -> dict:
    if not os.path.exists(KNOWN_ISSUES_PATH):
        return {}
    try:
        with open(KNOWN_ISSUES_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}


def allowed_sources_for(country: str, known_issues: dict) -> Set[Tuple[int, str]]:
    allowed: Set[Tuple[int, str]] = set()
    try:
        for item in known_issues.get(country, {}).get('allowed_sources', []):
            st = int(item.get('status'))
            fn = str(item.get('file'))
            if st and fn:
                allowed.add((st, fn))
    except Exception:
        return set()
    return allowed


def add_arguments(ap: argparse.ArgumentParser) -> None:
    ap.add_argument('--country', default=None, help='Limit to a single country folder (e.g., spain-immigration)')
    ap.add_argument('--countries', nargs='*', default=None, help='Limit to specific country folders')
    ap.add_argument('--include-meta', action='store_true', help='Also scan README.md and 99-sources-index.md')
    ap.add_argument('--fail-on', choices=['none', 'warn', 'error'], default='error', help='Exit code threshold: none/warn/error')
    ap.add_argument('--write-report', default=None, help='Write a Markdown report to this path')


def list_countries(root: str, only: Optional[str] = None) -> List[str]:
    dirs: List[str] = []
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
    if s.startswith('最後更新') or s.startswith('**標籤**'):
        return True
    if s.startswith('> 注意') or s.startswith('> 說明'):
        return True
    return False


def looks_like_claim(line: str) -> bool:
    s = line.strip()
    if should_ignore_line(line):
        return False
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


def scan_sources(country: str, root: str, known_issues: dict) -> List[Finding]:
    findings: List[Finding] = []
    src_dir = os.path.join(root, country, 'sources')
    if not os.path.isdir(src_dir):
        return findings

    allowed = allowed_sources_for(country, known_issues)

    for p in sorted(glob.glob(os.path.join(src_dir, '*.md'))):
        head = open(p, 'r', encoding='utf-8', errors='ignore').read(1200)
        m = re.search(r'^HTTP status:\s*(\d+)', head, re.M)
        st: Optional[int] = None
        if m:
            try:
                st = int(m.group(1))
            except Exception:
                st = None

        if st is not None and (st, os.path.basename(p)) in allowed:
            continue

        if st is not None and st >= 400:
            findings.append(Finding('error', country, p, 1, f'Non-200 source HTTP status: {st}'))

        if os.path.getsize(p) < 1200:
            findings.append(
                Finding('warn', country, p, 1, 'Very small source file (<1.2KB); likely nav-only/error/JS-driven')
            )

    return findings


def relpath_for_report(path: str, root: str) -> str:
    try:
        rp = os.path.relpath(path, root)
        return rp if not rp.startswith('..') else path
    except Exception:
        return path


def run(args: argparse.Namespace) -> int:
    root = os.getcwd()
    known_issues = load_known_issues()

    if args.countries:
        countries = [c for c in list_countries(root) if c in set(args.countries)]
    else:
        countries = list_countries(root, only=args.country)

    findings: List[Finding] = []

    for c in countries:
        for p in sorted(glob.glob(os.path.join(root, c, '*.md'))):
            base = os.path.basename(p)
            if (not args.include_meta) and base in {'README.md', '99-sources-index.md'}:
                continue
            if os.path.getsize(p) == 0:
                findings.append(Finding('error', c, p, 1, 'Empty topic file'))
                continue
            findings.extend(scan_topic_file(c, p))

        findings.extend(scan_sources(c, root, known_issues))

    report: List[str] = []
    report.append('# KB 審查報告（Heuristic Audit）')
    report.append('')
    report.append(f'生成時間(UTC)：{datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}  ')
    report.append('**注意**：此報告只提供「需要人工核對」的線索，不能證明法律正確性。')
    report.append('')

    if not countries:
        report.append('未選到任何國家資料夾（*-immigration）。')
    elif not findings:
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
                fpath = relpath_for_report(f.file, root)
                report.append(f"- {f.country}: `{fpath}`:{f.line} — {f.message}")
            report.append('')

    out = '\n'.join(report) + '\n'
    if args.write_report:
        with open(args.write_report, 'w', encoding='utf-8') as f:
            f.write(out)
    else:
        print(out)

    has_error = any(f.level == 'error' for f in findings)
    has_warn = any(f.level == 'warn' for f in findings)

    if args.fail_on == 'none':
        return 0
    if args.fail_on == 'error':
        return 1 if has_error else 0
    return 1 if (has_error or has_warn) else 0


def cli(argv=None) -> int:
    ap = argparse.ArgumentParser()
    add_arguments(ap)
    args = ap.parse_args(argv)
    return run(args)


if __name__ == '__main__':
    raise SystemExit(cli())
