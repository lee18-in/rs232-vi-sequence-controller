# LLM_MEMORY.md — 工作記憶(agent 讀寫;規則見 AGENTS.md,勿在此重複)

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.

## A. 目前狀態(每次交接必更新)

- 目前階段: build
$12026-10-22 11:15 / 當時階段: maintain
- 交接基準 commit: 26ce48f [maintain] 更新 LLM_MEMORY.md 最新狀態
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

### 2026-10-22 11:15 [maintain] 使用工具: Cursor Auto

- 完成了什麼: 依 AI_AGENT_Playbook_Online.md 將本目錄 AGENTS.md 自 v10 整份覆蓋升級至 v11（online）。覆蓋前 AGENTS.md hash: 9be043f（可用 `git show .md` 找回）。v11 重點：§0 接手環境自檢／驗證方式必填／待審下壓保護；§2.1 使用者簽結與批次審閱。
- 驗證方式: 讀檔確認開頭 `<!-- Playbook-Version: 11 -->` 與 `<!-- Playbook-Variant: online -->`；內容含「接手環境自檢」「驗證方式」「待審下壓」「使用者簽結」。
- 下一個 agent 該做什麼: 無（純憲法升級；若接手請依 §0 做 hooksPath 自檢）
- 地雷警告: 無

### 2026-09-14 10:20 [maintain] 使用工具: Antigravity

- 完成了什麼: 依使用者指示，將 AGENTS.md 升級至 Playbook v10（三層架構規範、防膨脹門檻改為 10KB、單筆長度上限約 1200 bytes、Review Loop 排除 COMPONENT_MAP.md）。
- 下一個 agent 該做什麼: 使用者明示推送到 GitHub（豁免本次審閱）。請後續接手的 agent 依各自專案階段推進任務。
- 地雷警告: 無

### 2026-08-25 17:14 [maintain] 使用工具: Claude Code

- 完成了什麼: 依 Playbook Online v9 執行分支 C 升級（原版本 v2，無 `Playbook-Variant` 標記，§2 使用 commit 為交接機制，判定為 online 變體）：`AGENTS.md` 整份覆蓋至 v9 模板（新增交接基準 commit 機制、Review Loop 順序條款、巢狀範圍條款 §4、語言與編碼規範等；§5 早已指向 LLM_MEMORY，無需再搬遷）；A 區「最新 commit」欄改名為「交接基準 commit」；`scripts/hooks/pre-commit`、`commit-msg` 整份覆蓋為最新版，並執行 `git config core.hooksPath scripts/hooks`（先前檔案存在但從未啟用，等同 hook 從未真正生效過）；新增 `.gitattributes` 的 `scripts/hooks/* text eol=lf`；README.md 頂端補上語言與編碼規範引導行。覆蓋前 `AGENTS.md` 的舊版可用 `git show a61843d:AGENTS.md` 找回。
- 下一個 agent 該做什麼: 無（純框架升級，無程式碼邏輯變更）
- 地雷警告: 無

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
