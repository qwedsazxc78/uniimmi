# Repository Guidelines

This repository is a Markdown-based immigration knowledge base designed to be **updatable, traceable, and auditable**.

## Project Structure & Module Organization

- `*-immigration/`: One country per folder (e.g., `hong-kong-immigration/`, `taiwan-immigration/`).
  - `sources/*.md`: Captured official sources. Each file should include `Source: <url>`, `Fetched (UTC): ...`, and `HTTP status: ...` near the top.
  - `*.md`: Topic notes (processes, rules, checklists). Any hard claims (dates, fees, “must/must not”, penalties) should cite nearby `sources/...`.
  - `99-sources-index.md`: Auto-generated index of `sources/` (do not edit manually).
- `tools/`: Repo-level automation.
  - `tools/update_all.py`: Orchestrates updates and rebuilds indexes.
  - `tools/audit_kb.py`: Heuristic audit report generator.
  - `tools/known_issues.json`: Allowlist for known non-200 official pages (e.g., expected 404s).

## Build, Test, and Development Commands

- Update sources + rebuild indexes: `python3 tools/update_all.py`
- Offline rebuild/check only: `python3 tools/update_all.py --no-fetch`
- Update + generate audit report: `python3 tools/update_all.py --audit --audit-report AUDIT.md`
- Audit only (fail on warnings): `python3 tools/audit_kb.py --fail-on warn --write-report AUDIT.md`
- Quick sanity for scripts: `python3 -m py_compile tools/update_all.py tools/audit_kb.py`

## Coding Style & Naming Conventions

- Language: Python 3 and Markdown.
- Prefer clear, small scripts; keep output deterministic.
- Folder naming: `<country>-immigration/`.
- Source filenames: stable, descriptive slugs (avoid dates in filenames unless the official page is date-scoped).

## Testing Guidelines

- No dedicated test framework currently.
- Validate changes by running `tools/update_all.py` (and `--audit` where appropriate).

## Commit & Pull Request Guidelines

- Commit messages in this repo are short and imperative (e.g., “update all”). Keep them concise; include scope when helpful (e.g., “spain: refresh sources manifest”).
- PRs should include:
  - What changed (countries/files),
  - How it was verified (commands + exit codes),
  - Any known issues added to `tools/known_issues.json`.

## Legal/Factual Review (Required)

Automation does not prove legal correctness. Follow `tools/LEGAL_REVIEW.md` and ensure topic claims are traceable to official sources.
