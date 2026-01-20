#!/usr/bin/env python3
"""Unified CLI for this repository.

This CLI wraps the repo tools with proper subcommands and full help output:
- update: tools/update_all.py
- audit:  tools/audit_kb.py

It also supports bootstrapping an isolated Python environment via `uv`.

Examples:
  ./tools/uniimmi.py env --python 3.12
  ./tools/uniimmi.py update --no-fetch --audit --audit-report AUDIT.md
  ./tools/uniimmi.py audit --fail-on warn --write-report AUDIT.md
  ./tools/uniimmi.py doctor
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys


def _find_repo_root(start: str):
    cur = os.path.abspath(start)
    while True:
        tools_dir = os.path.join(cur, 'tools')
        if os.path.isdir(tools_dir) and os.path.exists(os.path.join(tools_dir, 'update_all.py')):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return None
        cur = parent


def _prepare_imports(repo_root: str) -> None:
    os.chdir(repo_root)
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)


def _is_running_in_venv(venv_python: str) -> bool:
    try:
        return os.path.realpath(sys.executable) == os.path.realpath(venv_python)
    except Exception:
        return False


def _maybe_reexec_into_venv(venv_dir: str, argv) -> None:
    venv_python = os.path.join(venv_dir, 'bin', 'python')
    if not os.path.exists(venv_python):
        return
    if _is_running_in_venv(venv_python):
        return
    os.execv(venv_python, [venv_python] + argv)


def cmd_env(args: argparse.Namespace) -> int:
    uv = shutil.which('uv')
    if not uv:
        print('ERROR: `uv` not found on PATH.', file=sys.stderr)
        print('Install: https://docs.astral.sh/uv/getting-started/installation/', file=sys.stderr)
        return 1

    venv_dir = os.path.join(os.getcwd(), args.venv)
    req = os.path.join(os.getcwd(), args.requirements)

    if args.recreate and os.path.isdir(venv_dir):
        shutil.rmtree(venv_dir)

    if not os.path.isdir(venv_dir):
        cmd = [uv, 'venv', '--python', args.python, venv_dir]
        print('+', ' '.join(cmd))
        subprocess.run(cmd, check=True)

    if os.path.exists(req):
        cmd = [uv, 'pip', 'sync', '-r', req]
        print('+', ' '.join(cmd))
        subprocess.run(cmd, check=True)
    else:
        print(f'WARN: requirements file not found: {req}', file=sys.stderr)

    print('OK: environment ready')
    print(f'- Activate: `source {args.venv}/bin/activate`')
    print(f'- Or run: `{args.venv}/bin/python ./tools/uniimmi.py doctor`')
    return 0


def cmd_doctor(_args: argparse.Namespace) -> int:
    import json
    import platform
    import ssl

    root = os.getcwd()
    ok = True

    print(f'Repo root: {root}')
    print(f'Python: {sys.executable}')
    print(f'Python version: {platform.python_version()}')
    print(f'SSL: {ssl.OPENSSL_VERSION}')

    required = [
        'tools/update_all.py',
        'tools/audit_kb.py',
        'tools/known_issues.json',
        'tools/LEGAL_REVIEW.md',
    ]
    for p in required:
        if not os.path.exists(p):
            ok = False
            print(f'ERROR: missing `{p}`')

    if os.path.exists('tools/known_issues.json'):
        try:
            json.load(open('tools/known_issues.json', 'r', encoding='utf-8'))
            print('known_issues.json: OK')
        except Exception as e:
            ok = False
            print(f'ERROR: known_issues.json invalid JSON: {e}')

    countries = [d for d in os.listdir(root) if d.endswith('-immigration') and os.path.isdir(d)]
    print(f'Countries: {len(countries)}')
    for c in sorted(countries):
        src = os.path.join(c, 'sources')
        fetch = os.path.join(c, 'tools', 'fetch_sources.py')
        src_count = 0
        if os.path.isdir(src):
            try:
                src_count = len([x for x in os.listdir(src) if x.endswith('.md')])
            except Exception:
                src_count = 0
        print(f'- {c}: sources={src_count} fetcher={"yes" if os.path.exists(fetch) else "no"}')

    return 0 if ok else 1


def cli(argv=None) -> int:
    repo_root = _find_repo_root(os.getcwd())
    if not repo_root:
        print('Error: could not locate repo root (expected tools/update_all.py).', file=sys.stderr)
        return 2

    _prepare_imports(repo_root)

    # Early parse just to decide whether to re-exec into .venv.
    argv_list = list(sys.argv[1:] if argv is None else argv)
    cmd = argv_list[0] if argv_list else None
    if cmd not in (None, 'env', 'doctor', '--help', '-h'):
        _maybe_reexec_into_venv(os.path.join(repo_root, '.venv'), [os.path.join(repo_root, 'tools', 'uniimmi.py')] + argv_list)

    from tools import audit_kb, update_all

    parser = argparse.ArgumentParser(prog='uniimmi', description='uniimmi knowledge-base tools')
    sub = parser.add_subparsers(dest='command', required=True)

    p_env = sub.add_parser('env', help='Bootstrap an isolated venv using uv')
    p_env.add_argument('--python', default='3.12', help='Python version for uv venv (e.g., 3.12)')
    p_env.add_argument('--venv', default='.venv', help='Venv directory (default: .venv)')
    p_env.add_argument('--requirements', default='requirements.txt', help='Requirements file to sync')
    p_env.add_argument('--recreate', action='store_true', help='Delete and recreate the venv directory')
    p_env.set_defaults(_handler=cmd_env)

    p_update = sub.add_parser('update', help='Fetch sources, rebuild indexes, and run checks')
    update_all.add_arguments(p_update)
    p_update.set_defaults(_handler=lambda ns: update_all.run(ns))

    p_audit = sub.add_parser('audit', help='Run heuristic audit report')
    audit_kb.add_arguments(p_audit)
    p_audit.set_defaults(_handler=lambda ns: audit_kb.run(ns))

    p_doctor = sub.add_parser('doctor', help='Check environment and repo structure')
    p_doctor.set_defaults(_handler=cmd_doctor)

    args = parser.parse_args(argv)
    return int(args._handler(args))


if __name__ == '__main__':
    raise SystemExit(cli())
