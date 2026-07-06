# LLM_MEMORY.md — 工作記憶(agent 讀寫;規則見 AGENTS.md,勿在此重複)

## A. 目前狀態(每次交接必更新)

- 目前階段: build
- 最後更新: 2026-07-05 21:15 / 當時階段: build
- 最新 commit: 78f9766 Please provide the diff or a description of the changes so I can generate the commit message for you.
- 進行中任務: 測試中
- 阻塞點: 無

## B. 規劃(規劃階段 [plan] 專屬區;狀態: 草稿 | 已定案)

### B1. 架構決策(已定案後鎖定,建置/維運階段不得改)

| # | 決策 | 理由 | 狀態 |
|---|------|------|------|

### B2. 短期目標(本週)

- [ ]

### B3. 中期目標(本月)

- [ ]

### B4. 長期目標

- [ ]

## C. 交接日誌(只追加,不刪改;最新在最上,每筆一個小節)

### 2026-07-06 16:45 [maintain] 使用工具: Claude Code

- 完成了什麼: 升級 Playbook 到 v2 版本
  - AGENTS.md：整份覆蓋為 v2 模板，新增 §0 交接日誌書寫規範、§2.1 Review Loop，§5 純化為憲法條文（移除依專案填寫的技術脈絡）
  - LLM_MEMORY.md：新增〈E. 專案技術脈絡〉區塊，遷入舊 AGENTS.md §5 已填的建置指令、測試指令、程式碼慣例
  - scripts/hooks/：新建 pre-commit 與 commit-msg 兩支 hook，強制檢查 commit 訊息格式與 LLM_MEMORY.md 變更
  - git config core.hooksPath 已設為 scripts/hooks，hook 已啟用
- 下一個 agent 該做什麼: 無（本次純粹升級框架，無程式碼邏輯變更；使用者需自行 commit，訊息格式：`[maintain] 升級 AI agent 工作流至 Playbook v2`）
- 地雷警告: 無

<!-- 範例格式,新條目複製此結構插入在本註解下方:

### YYYY-MM-DD HH:MM [plan / build / maintain 擇一] 使用工具: <agent 名稱>

- 完成了什麼:
- 下一個 agent 該做什麼:
- 地雷警告: 無
-->

## D. 已封存結論(自〈總結封存〉搬入,唯讀)

## E. 專案技術脈絡(依專案填寫,agent 得隨專案實況更新,保持精簡)

- 建置指令: `pip install -r requirements.txt` (包含 pyserial, numpy)
- 測試指令: `python 232.py`
- 程式碼慣例: 標準 Python 3.x 語法與 Tkinter GUI 開發。
