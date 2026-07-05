<!-- AI AGENTS: Read ./AGENTS.md first, then ./LLM_MEMORY.md.
     Do NOT write planning content into this file. -->
# rs232-vi-sequence-controller (三段式電壓/電流時序控制器)

這是一個基於 Python 與 Tkinter 開發的圖形化介面工具，主要用於透過 RS232 控制可程式化直流電源供應器（Programmable DC Power Supply）。
This is a graphical tool built with Python and Tkinter for controlling a programmable DC power supply via RS232.

它允許使用者定義三個階段的電壓、電流以及持續時間，並能平滑地進行階段間的斜坡過渡（Ramp），最後以指定的次數重複循環。
It lets users define voltage, current, and duration for three stages, supports smooth ramp transitions between stages, and repeats the sequence for a specified number of cycles.

## 功能特色 / Features

- **三段式設定 / 3-stage setup**：可獨立設定階段 1、階段 2、階段 3 的目標電壓 (V)、電流 (A) 與持續時間 (ms)。
  Set target voltage (V), current (A), and duration (ms) independently for stage 1, stage 2, and stage 3.
- **線性轉換 (Ramping) / Smooth ramps**：支援設定段落間（1→2, 2→3, 3→1）的轉換時間。若時間大於 50ms，程式會自動產生平滑的階梯式過渡；小於 50ms 則瞬間跳躍。
  Supports setting transition time between stages (1→2, 2→3, 3→1). If the time is greater than 50ms, the program automatically generates smooth step ramps; if less, the change happens immediately.
- **SCPI 指令通訊 / SCPI command support**：使用標準儀器控制指令（如 `:SOUR:VOLT`, `:SOUR:CURR`, `:OUTP ON/OFF`），相容於多數支援 SCPI 的電源供應器。
  Uses standard instrument control commands (such as `:SOUR:VOLT`, `:SOUR:CURR`, `:OUTP ON/OFF`) and is compatible with most SCPI-enabled power supplies.
- **緊急停止功能 / Emergency stop**：隨時可以中斷循環，並將電壓電流歸零、強制關閉電源輸出，確保實驗安全。
  Allows interrupting the sequence at any time, setting voltage and current to zero, and forcing the output off to ensure safety.
- **非同步執行 / Asynchronous execution**：控制迴圈運行於獨立執行緒，確保執行期間 GUI 不會凍結。
  Runs the control loop in a separate thread so the GUI remains responsive during execution.

## 環境需求 / Requirements

請確保您的系統已安裝 Python 3.x，並安裝以下依賴套件：
Please make sure Python 3.x is installed and then install the required packages:

```bash
pip install pyserial numpy
```

## 使用說明 / Usage

1. **硬體連接 / Hardware connection**：將您的電源供應器透過 RS232 傳輸線連接至電腦。
   Connect your power supply to the computer via RS232 cable.
2. **確認通訊埠 (COM Port) / Confirm COM port**：
   請開啟 `RS232.py` 原始碼，將第 7 行的 `SERIAL_PORT` 修改為您的實際連接埠（例如 `COM3` 或 `/dev/ttyUSB0`）。並確認 `BAUDRATE` (預設 115200) 與硬體設定一致。
   Open `RS232.py` and update `SERIAL_PORT` on line 7 to your actual port (for example `COM3` or `/dev/ttyUSB0`). Also verify `BAUDRATE` (default 115200) matches your hardware.
3. **啟動程式 / Run the script**：
   ```bash
   python RS232.py
   ```
4. **操作介面 / Interface**：
   - 輸入各階段所需的電壓、電流與時間參數。
     Enter the voltage, current, and time values for each stage.
   - 設定循環次數。
     Set the number of cycles.
   - 點擊「▶️ 開始循環」執行。
     Click “▶️ Start” to begin the sequence.
   - 若遇突發狀況，可隨時點選「⛔ 緊急停止」。
     Use “⛔ Emergency Stop” if you need to interrupt the operation immediately.

## 授權條款 / License

本專案採用 MIT License 授權。
This project is licensed under the MIT License.
