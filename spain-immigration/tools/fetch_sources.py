#!/usr/bin/env python3
"""Fetch official Spain immigration-related sources into spain-immigration/sources/*.md.

- Uses tools/sources_manifest.json mapping slug -> URL.
- Extracts readable text from HTML (best effort).
- Stores Source + fetch time + HTTP status.

Heuristics:
- Some portals (notably www.inclusion.gob.es) place the actual article content far
  after large navigation HTML. For those, we try to extract starting at the first
  "content wrapper" marker so the saved text contains the substantive content.
"""

import json
import os
import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from typing import List

import requests

UA = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/120.0.0.0 Safari/537.36'
)

HEADERS = {
    'User-Agent': UA,
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.7',
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
        self._skip = 0
        self._out: List[str] = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in {'script', 'style', 'noscript'}:
            self._skip += 1
            return
        if self._skip:
            return
        if tag in BLOCK_TAGS:
            self._out.append('\n')

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in {'script', 'style', 'noscript'}:
            self._skip = max(0, self._skip - 1)
            return
        if self._skip:
            return
        if tag in BLOCK_TAGS:
            self._out.append('\n')

    def handle_data(self, data):
        if self._skip:
            return
        s = data.strip()
        if not s:
            return
        self._out.append(s)
        self._out.append(' ')

    def get_text(self) -> str:
        raw = ''.join(self._out)
        raw = raw.replace('\xa0', ' ')
        raw = re.sub(r'[ \t\r\f\v]+', ' ', raw)
        raw = re.sub(r'\n\s*\n\s*\n+', '\n\n', raw)
        raw = re.sub(r' *\n *', '\n', raw)
        return raw.strip()


def extract_title(html: str) -> str:
    m = re.search(r'<title[^>]*>(.*?)</title>', html, flags=re.IGNORECASE | re.DOTALL)
    if not m:
        return 'Untitled'
    t = re.sub(r'\s+', ' ', m.group(1)).strip()
    return t or 'Untitled'


def focus_html_for_source(url: str, html: str) -> str:
    if 'www.inclusion.gob.es/web/migraciones/' in url:
        markers = [
            'm-genericContent__containerTitle',
            'm-genericContent__wrapper',
            'm-genericContent m-genericContent__wrapper',
            'id="main-content"',
            'class="m-genericContent',
        ]
        idxs = [html.find(m) for m in markers if html.find(m) != -1]
        if idxs:
            start = min(idxs)
            # Keep a small lead-in to not cut tags in the middle.
            start = max(0, start - 2000)
            return html[start:]
    return html


def write_md(path: str, url: str, status: int, title: str, body: str, truncated: bool):
    fetched = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"Source: {url}\n\n")
        f.write(f"Fetched (UTC): {fetched}\n\n")
        f.write(f"HTTP status: {status}\n")
        if truncated:
            f.write("\nNote: Extracted text truncated for repo size. Use the Source URL for full content.\n")
        f.write("\n---\n\n")
        f.write(body.strip())
        f.write("\n")


def main():
    manifest_path = os.path.join('spain-immigration', 'tools', 'sources_manifest.json')
    sources_dir = os.path.join('spain-immigration', 'sources')
    os.makedirs(sources_dir, exist_ok=True)

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    max_chars = 200000
    timeout_s = 90

    ok = 0
    fail = 0

    for slug, url in manifest.items():
        out_path = os.path.join(sources_dir, f"{slug}.md")
        try:
            r = requests.get(url, headers=HEADERS, timeout=timeout_s)
            html = r.text
            title = extract_title(html)

            focus_html = focus_html_for_source(url, html)

            parser = HtmlTextExtractor()
            parser.feed(focus_html)
            text = parser.get_text()

            truncated = False
            if len(text) > max_chars:
                text = text[:max_chars].rstrip() + "\n\n[...truncated...]"
                truncated = True

            write_md(out_path, url, r.status_code, title, text, truncated)
            ok += 1
        except Exception as e:
            fail += 1
            fetched = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write("# Fetch Failed\n\n")
                f.write(f"Source: {url}\n\n")
                f.write(f"Fetched (UTC): {fetched}\n\n")
                f.write(f"Error: {type(e).__name__}: {e}\n")

    print(f"Updated sources: ok={ok} fail={fail} total={len(manifest)}")


if __name__ == '__main__':
    main()
