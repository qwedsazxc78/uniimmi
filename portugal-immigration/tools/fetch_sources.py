#!/usr/bin/env python3
"""Fetch official Portugal immigration-related sources into portugal-immigration/sources/*.md.

- Uses a small manifest json mapping "slug" -> URL.
- Extracts readable text from HTML (best effort).
- Keeps each file self-contained with Source + fetch time + HTTP status.

Note: Some government portals are SPA/JS-heavy. In those cases, extracted text may
be incomplete; the Source URL remains the ground truth.
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
    'Accept-Language': 'pt-PT,pt;q=0.9,en;q=0.7',
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
    root = os.path.join('portugal-immigration', 'tools', 'sources_manifest.json')
    sources_dir = os.path.join('portugal-immigration', 'sources')
    os.makedirs(sources_dir, exist_ok=True)

    with open(root, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    max_chars = 160000
    timeout_s = 90

    ok = 0
    fail = 0

    for slug, url in manifest.items():
        out_path = os.path.join(sources_dir, f"{slug}.md")
        try:
            r = requests.get(url, headers=HEADERS, timeout=timeout_s)
            html = r.text
            title = extract_title(html)
            parser = HtmlTextExtractor()
            parser.feed(html)
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
