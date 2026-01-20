#!/usr/bin/env python3
"""Fetch and extract text from official sources into australia-immigration/sources/*.md.

The Home Affairs website (SharePoint) often renders visa detail content client-side.
Many visa pages embed a rich JSON payload in a hidden input named
PageSchemaHiddenField_Input. We extract and summarise that payload for traceability.

This script is intentionally "best effort"; it prefers official URLs over perfect
HTML->Markdown fidelity.
"""

import glob
import html as htmllib
import json
import os
import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from typing import Any, Dict, Iterable, List, Optional, Tuple

import requests

UA = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/120.0.0.0 Safari/537.36'
)

HEADERS = {
    'User-Agent': UA,
    'Accept-Language': 'en-AU,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

BLOCK_TAGS = {
    'p', 'div', 'section', 'article', 'main', 'header', 'footer',
    'li', 'ul', 'ol',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'br', 'hr',
    'table', 'thead', 'tbody', 'tr', 'td', 'th',
    'pre', 'code',
}


class HtmlTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self._skip_depth = 0
        self._out: List[str] = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in {'script', 'style', 'noscript'}:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if tag in BLOCK_TAGS:
            self._out.append('\n')

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in {'script', 'style', 'noscript'}:
            self._skip_depth = max(0, self._skip_depth - 1)
            return
        if self._skip_depth:
            return
        if tag in BLOCK_TAGS:
            self._out.append('\n')

    def handle_data(self, data):
        if self._skip_depth:
            return
        s = data.strip()
        if not s:
            return
        self._out.append(s)
        self._out.append(' ')

    def error(self, message):
        pass

    def get_text(self) -> str:
        raw = ''.join(self._out)
        raw = raw.replace('\xa0', ' ')
        raw = re.sub(r'[ \t\r\f\v]+', ' ', raw)
        raw = re.sub(r'\n\s*\n\s*\n+', '\n\n', raw)
        raw = re.sub(r' *\n *', '\n', raw)
        return raw.strip()


def html_to_text(fragment: str) -> str:
    parser = HtmlTextExtractor()
    parser.feed(fragment)
    return parser.get_text()


def extract_title(html: str) -> Optional[str]:
    m = re.search(r'<title>(.*?)</title>', html, flags=re.IGNORECASE | re.DOTALL)
    if not m:
        return None
    t = re.sub(r'\s+', ' ', m.group(1)).strip()
    return t or None


def find_pageschema_json(html: str) -> Optional[Dict[str, Any]]:
    """Return decoded JSON embedded in SharePoint's PageSchemaHiddenField_Input, if any."""
    m = re.search(
        r'PageSchemaHiddenField_Input[^>]*\bvalue="([^"]+)"',
        html,
        flags=re.IGNORECASE,
    )
    if not m:
        return None
    raw = htmllib.unescape(m.group(1))
    try:
        return json.loads(raw)
    except Exception:
        return None


def _collect_eligibility(criteria: Any) -> List[str]:
    out: List[str] = []
    if isinstance(criteria, list):
        for item in criteria:
            out.extend(_collect_eligibility(item))
        return out
    if not isinstance(criteria, dict):
        return out

    title = criteria.get('title') or criteria.get('text')
    desc = criteria.get('description') or criteria.get('body')

    if title:
        out.append(f"- {html_to_text(str(title))}")
    if desc:
        d = html_to_text(str(desc))
        if d:
            out.append(f"  {d}")

    nested = criteria.get('criteria')
    if nested:
        out.extend(_collect_eligibility(nested))

    return out


def _collect_steps(steps: Any, indent: int = 0) -> List[str]:
    out: List[str] = []
    if isinstance(steps, list):
        for s in steps:
            out.extend(_collect_steps(s, indent=indent))
        return out
    if not isinstance(steps, dict):
        return out

    title = steps.get('title') or steps.get('text')
    sub = steps.get('subTitle')
    desc = steps.get('description') or steps.get('body')

    prefix = '  ' * indent + '- '
    if title:
        out.append(prefix + html_to_text(str(title)))
    if sub:
        t = html_to_text(str(sub))
        if t:
            out.append('  ' * (indent + 1) + t)
    if desc:
        t = html_to_text(str(desc))
        if t:
            out.append('  ' * (indent + 1) + t)

    nested = steps.get('steps')
    if nested:
        out.extend(_collect_steps(nested, indent=indent + 1))

    return out


def summarise_pageschema(obj: Dict[str, Any]) -> str:
    lines: List[str] = []

    title = obj.get('title')
    subclass = obj.get('visaSubclassHeading')
    desc = obj.get('description')
    if title or subclass or desc:
        lines.append('## PageSchema 摘要（從官方頁面內嵌資料抽取）')
        if title:
            lines.append(f"- Title: {title}")
        if subclass:
            lines.append(f"- Subclass: {subclass}")
        if desc:
            lines.append(f"- Description: {desc}")

    generic_content = obj.get('content')
    if generic_content:
        lines.append('')
        lines.append('## Content')
        for item in generic_content:
            if not isinstance(item, dict):
                continue
            heading = item.get('text') or item.get('title')
            block = item.get('block') or item.get('description') or item.get('body')
            if heading:
                lines.append(f"### {html_to_text(str(heading))}")
            if block:
                t = html_to_text(str(block))
                if t:
                    lines.append(t)

    applicant = obj.get('applicant') or {}
    overview = applicant.get('overview') or {}
    if overview:
        notes_heading = overview.get('notesHeading')
        notes = overview.get('notes')
        stay = overview.get('stayPeriod')
        cost = overview.get('visaCost')
        lines.append('')
        lines.append('## Overview')
        if notes_heading:
            lines.append(f"- {html_to_text(str(notes_heading))}")
        if notes:
            t = html_to_text(str(notes))
            if t:
                lines.append(t)
        if stay:
            t = html_to_text(str(stay))
            if t:
                lines.append('')
                lines.append(f"Stay: {t}")
        if cost:
            t = html_to_text(str(cost))
            if t:
                lines.append('')
                lines.append(f"Cost: {t}")

    about = applicant.get('aboutVisa') or {}
    content = about.get('content')
    if content:
        lines.append('')
        lines.append('## About this visa')
        for item in content:
            if not isinstance(item, dict):
                continue
            heading = item.get('text') or item.get('title')
            block = item.get('block') or item.get('description')
            if heading:
                lines.append(f"### {html_to_text(str(heading))}")
            if block:
                t = html_to_text(str(block))
                if t:
                    lines.append(t)

    eligibility = applicant.get('eligibility') or {}
    crit = eligibility.get('criteria')
    if crit:
        lines.append('')
        lines.append('## Eligibility（節錄）')
        lines.extend(_collect_eligibility(crit))

    step_guide = applicant.get('stepGuide') or {}
    steps = step_guide.get('steps')
    if steps:
        lines.append('')
        lines.append('## Step guide（節錄）')
        lines.extend(_collect_steps(steps))

    have = applicant.get('haveThisVisa') or {}
    have_content = have.get('content')
    if have_content:
        lines.append('')
        lines.append('## If you already have this visa（節錄）')
        for item in have_content:
            if not isinstance(item, dict):
                continue
            heading = item.get('text') or item.get('title')
            block = item.get('block') or item.get('description')
            if heading:
                lines.append(f"### {html_to_text(str(heading))}")
            if block:
                t = html_to_text(str(block))
                if t:
                    lines.append(t)

    text = '\n'.join(lines).strip()
    return text


def fetch(url: str, timeout_s: int = 60) -> requests.Response:
    return requests.get(url, headers=HEADERS, timeout=timeout_s)


def write_source_md(path: str, url: str, status: int, title: Optional[str], body: str, truncated: bool):
    fetched = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    title_line = (title or 'Untitled').strip()

    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"# {title_line}\n\n")
        f.write(f"Source: {url}\n\n")
        f.write(f"Fetched (UTC): {fetched}\n\n")
        f.write(f"HTTP status: {status}\n")
        if truncated:
            f.write("\nNote: Extracted text truncated for repo size. Use the Source URL for full content.\n")
        f.write("\n---\n\n")
        f.write(body.strip())
        f.write("\n")


def main():
    sources_dir = os.path.join('australia-immigration', 'sources')
    existing_files = sorted(glob.glob(os.path.join(sources_dir, '*.md')))

    urls: Dict[str, str] = {}
    for p in existing_files:
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            head = f.read(2500)
        m = re.search(r'^Source:\s*(\S+)\s*$', head, flags=re.MULTILINE)
        if m:
            urls[p] = m.group(1)

    extra = {
        os.path.join(sources_dir, 'leg_migration_regulations_1994_latest.md'): 'https://www.legislation.gov.au/F1996B03551/latest/text',
        os.path.join(sources_dir, 'leg_australian_citizenship_act_2007_latest.md'): 'https://www.legislation.gov.au/C2004A00319/latest/text',
        os.path.join(sources_dir, 'leg_australian_citizenship_regulations_2016_latest.md'): 'https://www.legislation.gov.au/F2016L00217/latest/text',
    }
    for p, u in extra.items():
        urls.setdefault(p, u)

    # Limit extracted text to keep repo manageable.
    max_chars = 160000

    ok = 0
    fail = 0
    for path, url in urls.items():
        try:
            r = fetch(url)
            html_doc = r.text
            title = extract_title(html_doc)

            schema_obj = find_pageschema_json(html_doc)
            if schema_obj:
                schema_text = summarise_pageschema(schema_obj)
            else:
                schema_text = ''

            # Always keep a baseline text extraction (useful for legislation pages).
            parser = HtmlTextExtractor()
            parser.feed(html_doc)
            plain_text = parser.get_text()

            body_parts = []
            if schema_text:
                body_parts.append(schema_text)
                body_parts.append('')
                body_parts.append('---')
                body_parts.append('')
                body_parts.append('## Baseline HTML text extraction（可能包含大量導覽文字）')
            body_parts.append(plain_text)

            body = '\n'.join(body_parts).strip()
            truncated = False
            if len(body) > max_chars:
                body = body[:max_chars].rstrip() + "\n\n[...truncated...]"
                truncated = True

            write_source_md(path, url, r.status_code, title, body, truncated)
            ok += 1
        except Exception as e:
            fail += 1
            fetched = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
            with open(path, 'w', encoding='utf-8') as f:
                f.write("# Fetch Failed\n\n")
                f.write(f"Source: {url}\n\n")
                f.write(f"Fetched (UTC): {fetched}\n\n")
                f.write(f"Error: {type(e).__name__}: {e}\n")

    print(f"Updated sources: ok={ok} fail={fail} total={len(urls)}")


if __name__ == '__main__':
    main()
