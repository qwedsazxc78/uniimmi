#!/usr/bin/env python3
"""Update country immigration knowledge base.

What it does:
- Discovers country folders: *-immigration/
- For folders with tools/fetch_sources.py, runs it to refresh sources.
- Rebuilds each country's 99-sources-index.md from sources/*.md.
- Runs lightweight consistency checks (missing refs, bad HTTP status, empty files).

Usage:
  python3 tools/update_all.py
  python3 tools/update_all.py --countries australia-immigration spain-immigration
  python3 tools/update_all.py --no-fetch  # only rebuild indexes + checks

Exit codes:
- 0: ok
- 1: issues found (non-200 sources, missing refs, empty files, fetch failures)
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

KNOWN_ISSUES_PATH = os.path.join('tools', 'known_issues.json')



@dataclass
class SourceRow:
    path: str
    title: str
    url: str
    fetched: str
    status: str


def load_known_issues() -> dict:
    if not os.path.exists(KNOWN_ISSUES_PATH):
        return {}
    try:
        with open(KNOWN_ISSUES_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}


def list_country_dirs(root: str) -> List[str]:
    dirs = []
    for name in os.listdir(root):
        p = os.path.join(root, name)
        if os.path.isdir(p) and name.endswith('-immigration'):
            dirs.append(name)
    return sorted(dirs)


def run(cmd: Sequence[str], cwd: str, timeout_s: int = 900) -> int:
    proc = subprocess.run(cmd, cwd=cwd, timeout=timeout_s)
    return int(proc.returncode)


def parse_sources_rows(country_dir: str) -> List[SourceRow]:
    sources_dir = os.path.join(country_dir, 'sources')
    rows: List[SourceRow] = []
    if not os.path.isdir(sources_dir):
        return rows

    for path in sorted(glob.glob(os.path.join(sources_dir, '*.md'))):
        txt = open(path, 'r', encoding='utf-8', errors='ignore').read(9000)
        title_m = re.search(r'^#\s+(.+)$', txt, re.M)
        url_m = re.search(r'^Source:\s*(\S+)\s*$', txt, re.M)
        fetched_m = re.search(r'^Fetched \(UTC\):\s*(.+)\s*$', txt, re.M)
        status_m = re.search(r'^HTTP status:\s*(\d+)\s*$', txt, re.M)
        rows.append(
            SourceRow(
                path=path,
                title=(title_m.group(1).strip() if title_m else ''),
                url=(url_m.group(1).strip() if url_m else ''),
                fetched=(fetched_m.group(1).strip() if fetched_m else ''),
                status=(status_m.group(1).strip() if status_m else ''),
            )
        )
    return rows


def write_sources_index(country_dir: str, rows: List[SourceRow]) -> None:
    out_path = os.path.join(country_dir, '99-sources-index.md')
    lines: List[str] = []
    lines.append('# 來源索引（sources index）')
    lines.append('')
    lines.append(f'最後更新：{datetime.utcnow().strftime("%Y-%m-%d")}  ')
    lines.append('**標籤**：#sources #官方來源 #可追溯性')
    lines.append('')
    lines.append('> 說明：本索引對應本資料夾內 `sources/` 的「原始頁面文字抽取版」。如遇內容缺漏（例如網站以 JS 動態載入），請直接點 `Source` URL 以官方原文為準。')
    lines.append('')
    lines.append('| 檔案 | HTTP | 抓取時間(UTC) | 標題 | Source |')
    lines.append('|---|---:|---|---|---|')

    for r in rows:
        safe_title = (r.title or '').replace('|', '\\|')
        lines.append(
            '| `{}` | {} | {} | {} | {} |'.format(
                r.path,
                r.status,
                r.fetched,
                safe_title,
                r.url,
            )
        )

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


def scan_missing_refs(country_dir: str) -> List[str]:
    refs: set[str] = set()
    for path in glob.glob(os.path.join(country_dir, '*.md')):
        txt = open(path, 'r', encoding='utf-8', errors='ignore').read()
        for m in re.finditer(r'`([^`]*?/sources/[^`]+?\.md)`', txt):
            refs.add(m.group(1))

    missing = [r for r in sorted(refs) if not os.path.exists(r)]
    return missing


def scan_empty_topic_files(country_dir: str) -> List[str]:
    empties = []
    for path in glob.glob(os.path.join(country_dir, '*.md')):
        if os.path.getsize(path) == 0:
            empties.append(path)
    return sorted(empties)


def scan_bad_sources(country_dir: str, known_issues: dict) -> List[Tuple[int, str]]:
    allowed = set()
    try:
        for item in known_issues.get(country_dir, {}).get('allowed_sources', []):
            allowed.add((int(item.get('status')), item.get('file')))
    except Exception:
        allowed = set()

    bad = []
    for r in parse_sources_rows(country_dir):
        try:
            st = int(r.status)
        except Exception:
            continue
        if st >= 400:
            key = (st, os.path.basename(r.path))
            if key in allowed:
                continue
            bad.append((st, os.path.basename(r.path)))
    return sorted(bad)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--countries', nargs='*', default=None, help='Limit to specific country folders')
    ap.add_argument('--no-fetch', action='store_true', help='Skip running country tools/fetch_sources.py')
    ap.add_argument('--timeout', type=int, default=900, help='Timeout seconds for each fetch_sources.py')
    args = ap.parse_args()

    root = os.getcwd()
    all_countries = list_country_dirs(root)
    countries = all_countries
    if args.countries:
        want = set(args.countries)
        countries = [c for c in all_countries if c in want]

    if not countries:
        print('No country folders found/selected.', file=sys.stderr)
        return 1

    issues: List[str] = []

    known_issues = load_known_issues()

    for c in countries:
        print(f'\n== {c} ==')
        fetch = os.path.join(c, 'tools', 'fetch_sources.py')
        if (not args.no_fetch) and os.path.exists(fetch):
            print(f'- Running: {fetch}')
            rc = run([sys.executable, fetch], cwd=root, timeout_s=args.timeout)
            if rc != 0:
                issues.append(f'{c}: fetch_sources.py failed rc={rc}')

        rows = parse_sources_rows(c)
        if rows:
            print(f'- Rebuilding sources index ({len(rows)} rows)')
            write_sources_index(c, rows)

        empties = scan_empty_topic_files(c)
        if empties:
            issues.append(f'{c}: empty topic files: {len(empties)}')
            for p in empties[:10]:
                issues.append(f'  - {p}')

        missing = scan_missing_refs(c)
        if missing:
            issues.append(f'{c}: missing referenced sources: {len(missing)}')
            for r in missing[:15]:
                issues.append(f'  - {r}')

        bad = scan_bad_sources(c, known_issues)
        if bad:
            issues.append(f'{c}: non-200 sources: {len(bad)}')
            for st, fn in bad[:15]:
                issues.append(f'  - {st} {c}/sources/{fn}')

    if issues:
        print('\nIssues found:')
        for line in issues:
            print(line)
        return 1

    print('\nAll checks passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
