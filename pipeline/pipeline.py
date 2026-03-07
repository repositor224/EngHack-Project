import serial
import json
import time
import requests

PORT = "/dev/cu.usbmodem101"
BAUD = 9600

SERVER_URL = "http://127.0.0.1:8000/data"

ser = serial.Serial(PORT, BAUD)

BUFFER = []
WINDOW = 30   # 30条数据≈1分钟

print("Pipeline started")


def send_command(cmd):
    ser.write((cmd + "\n").encode())


while True:

    line = ser.readline().decode().strip()

    try:
        data = json.loads(line)

        BUFFER.append(data)

        print("sensor:", data)

        if len(BUFFER) >= WINDOW:

            avg_temp = sum(d["temperature"] for d in BUFFER) / len(BUFFER)
            avg_light = sum(d["light"] for d in BUFFER) / len(BUFFER)

            payload = {
                "device_id": "scanner_01",
                "timestamp": time.time(),
                "temperature": avg_temp,
                "light": avg_light
            }

            r = requests.post(SERVER_URL, json=payload)

            result = r.json()

            print("AI:", result)

            # ---------- Reverse pipeline ----------

            advice = result.get("rule_based_comfort", "")

            if advice == "too hot":
                send_command("LED_ON")

            elif advice == "low light":
                send_command("LED_ON")

            else:
                send_command("LED_OFF")

            BUFFER.clear()

    except:
        pass