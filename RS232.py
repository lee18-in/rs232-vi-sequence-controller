import tkinter as tk
import serial
import time
import threading
import numpy as np

SERIAL_PORT = 'COM3'
BAUDRATE = 115200
stop_flag = False

def send_command(ser, cmd):
    ser.write((cmd + '\n').encode())
    if '?' in cmd:
        return ser.readline().decode().strip()

def ramp_va(ser, v_start, a_start, v_end, a_end, duration_ms, steps=50):
    # 若轉換小於50ms，直接跳終點
    if duration_ms < 50:
        send_command(ser, f':SOUR:CURR {a_end:.3f}')
        send_command(ser, f':SOUR:VOLT {v_end:.3f}')
        return
    v_list = np.linspace(v_start, v_end, steps)
    a_list = np.linspace(a_start, a_end, steps)
    delay = duration_ms / steps / 1000.0
    for v, a in zip(v_list, a_list):
        if stop_flag:
            return
        send_command(ser, f':SOUR:CURR {a:.3f}')
        send_command(ser, f':SOUR:VOLT {v:.3f}')
        time.sleep(delay)

def emergency_stop():
    global stop_flag
    stop_flag = True
    try:
        with serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1) as ser:
            send_command(ser, ':SOUR:CURR 0')
            send_command(ser, ':SOUR:VOLT 0')
            send_command(ser, ':OUTP OFF')
    except Exception as e:
        print(f"Serial Error in stop: {e}")
    status_label.config(text="🛑 已緊急停止")

def execute_loop():
    global stop_flag
    try:
        V1 = float(entry_v1.get())
        A1 = float(entry_a1.get())
        T1 = float(entry_t1.get())
        Trise12 = float(entry_trise12.get())
        V2 = float(entry_v2.get())
        A2 = float(entry_a2.get())
        T2 = float(entry_t2.get())
        Trise23 = float(entry_trise23.get())
        V3 = float(entry_v3.get())
        A3 = float(entry_a3.get())
        T3 = float(entry_t3.get())
        Trise31 = float(entry_trise31.get())
        loop_count = int(entry_loop.get())
        steps = 50

        stop_flag = False
        status_label.config(text="⚙️ 執行...")

        with serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1) as ser:
            send_command(ser, ':OUTP ON')
            for i in range(loop_count):
                if stop_flag: break
                status_label.config(text=f"🔁 第 {i+1} 次")
                # 1
                send_command(ser, f':SOUR:CURR {A1}')
                send_command(ser, f':SOUR:VOLT {V1}')
                time.sleep(T1/1000.0)
                if stop_flag: break
                # 1→2
                ramp_va(ser, V1, A1, V2, A2, Trise12, steps)
                if stop_flag: break
                # 2
                send_command(ser, f':SOUR:CURR {A2}')
                send_command(ser, f':SOUR:VOLT {V2}')
                time.sleep(T2/1000.0)
                if stop_flag: break
                # 2→3
                ramp_va(ser, V2, A2, V3, A3, Trise23, steps)
                if stop_flag: break
                # 3
                send_command(ser, f':SOUR:CURR {A3}')
                send_command(ser, f':SOUR:VOLT {V3}')
                time.sleep(T3/1000.0)
                if stop_flag: break
                # 3→1
                ramp_va(ser, V3, A3, V1, A1, Trise31, steps)

            send_command(ser, ':SOUR:CURR 0')
            send_command(ser, ':SOUR:VOLT 0')
            send_command(ser, ':OUTP OFF')
        if not stop_flag:
            status_label.config(text="✅ 結束，已關閉輸出")
    except Exception as e:
        status_label.config(text=f"❌ 錯誤: {e}")

def start_loop():
    threading.Thread(target=execute_loop).start()

# ==== GUI ====
root = tk.Tk()
root.title("rs232-vi-sequence-controller")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="1. 電壓(V)").grid(row=0,column=0); entry_v1 = tk.Entry(frame,width=7); entry_v1.grid(row=0,column=1)
tk.Label(frame, text="1. 電流(A)").grid(row=0,column=2); entry_a1 = tk.Entry(frame,width=7); entry_a1.grid(row=0,column=3)
tk.Label(frame, text="1. 持續(ms)").grid(row=0,column=4); entry_t1 = tk.Entry(frame,width=7); entry_t1.grid(row=0,column=5)
tk.Label(frame, text="1→2變(ms)").grid(row=1,column=0); entry_trise12 = tk.Entry(frame,width=7); entry_trise12.grid(row=1,column=1)
tk.Label(frame, text="2. 電壓(V)").grid(row=2,column=0); entry_v2 = tk.Entry(frame,width=7); entry_v2.grid(row=2,column=1)
tk.Label(frame, text="2. 電流(A)").grid(row=2,column=2); entry_a2 = tk.Entry(frame,width=7); entry_a2.grid(row=2,column=3)
tk.Label(frame, text="2. 持續(ms)").grid(row=2,column=4); entry_t2 = tk.Entry(frame,width=7); entry_t2.grid(row=2,column=5)
tk.Label(frame, text="2→3變(ms)").grid(row=3,column=0); entry_trise23 = tk.Entry(frame,width=7); entry_trise23.grid(row=3,column=1)
tk.Label(frame, text="3. 電壓(V)").grid(row=4,column=0); entry_v3 = tk.Entry(frame,width=7); entry_v3.grid(row=4,column=1)
tk.Label(frame, text="3. 電流(A)").grid(row=4,column=2); entry_a3 = tk.Entry(frame,width=7); entry_a3.grid(row=4,column=3)
tk.Label(frame, text="3. 持續(ms)").grid(row=4,column=4); entry_t3 = tk.Entry(frame,width=7); entry_t3.grid(row=4,column=5)
tk.Label(frame, text="3→1變(ms)").grid(row=5,column=0); entry_trise31 = tk.Entry(frame,width=7); entry_trise31.grid(row=5,column=1)
tk.Label(frame, text="循環次數").grid(row=6,column=0); entry_loop = tk.Entry(frame,width=7); entry_loop.grid(row=6,column=1)

btn_start = tk.Button(root, text="▶️ 開始循環", command=start_loop, bg="lightblue", width=20)
btn_start.pack(pady=5)
btn_stop = tk.Button(root, text="⛔ 緊急停止", command=emergency_stop, bg="red", fg="white", width=20)
btn_stop.pack(pady=5)
status_label = tk.Label(root, text="🕹 等待中", fg="blue")
status_label.pack()

# 預設值
entry_v1.insert(0, "0"); entry_a1.insert(0, "0"); entry_t1.insert(0, "500")
entry_trise12.insert(0, "500")
entry_v2.insert(0, "16"); entry_a2.insert(0, "2.15"); entry_t2.insert(0, "500")
entry_trise23.insert(0, "500")
entry_v3.insert(0, "24"); entry_a3.insert(0, "2.15"); entry_t3.insert(0, "500")
entry_trise31.insert(0, "500")
entry_loop.insert(0, "10")

root.mainloop()
