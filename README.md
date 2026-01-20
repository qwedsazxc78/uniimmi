# uniimmi

移民規定/流程知識庫（可更新、可追溯、可審查）。

## 資料結構（每個國家資料夾）

- `*-immigration/sources/*.md`：官方來源原文抽取（含 Source URL、Fetched(UTC)、HTTP status）
- `*-immigration/*.md`：主題整理/解讀（硬性規則/數字/期限/禁止/義務/罰則 → 同段落附近引用 `sources/...`）
- `*-immigration/99-sources-index.md`：來源索引（自動生成；請勿手改）

## Runbook（更新/審查）

主要入口：`./tools/uniimmi.py`

建議先建立隔離環境（避免系統 Python / user-site 套件造成不一致）：

- 建立/同步 venv（需要先安裝 uv）：`./tools/uniimmi.py env --python 3.12`
- 健檢環境：`./tools/uniimmi.py doctor`

- 看全部選項：`./tools/uniimmi.py --help`
- 更新（抓 sources + 重建索引 + 檢查）：`./tools/uniimmi.py update`
- 指定國家：`./tools/uniimmi.py update --countries hong-kong-immigration taiwan-immigration`
- 離線模式（不抓 sources）：`./tools/uniimmi.py update --no-fetch`
- 更新後產出審查報告：`./tools/uniimmi.py update --no-fetch --audit --audit-report AUDIT.md`

只跑審查（不更新 sources）：

- 基本審查：`./tools/uniimmi.py audit --write-report AUDIT.md`
- 更嚴格（有 WARN 就失敗）：`./tools/uniimmi.py audit --fail-on warn --write-report AUDIT.md`


審查流程建議見：`tools/LEGAL_REVIEW.md`

## Known Issues（允許清單）

當官方來源暫時 404/改版，但仍希望保留追溯線索時，可加入：`tools/known_issues.json`
