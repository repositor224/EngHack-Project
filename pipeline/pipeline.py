import serial
import json
import time
import requests
import re

PORT = "/dev/cu.usbmodem101"
BAUD = 9600

SERVER_URL = "http://127.0.0.1:8000/data"
JSONL_FILE = "sensor_stream.jsonl"

ser = serial.Serial(PORT, BAUD)

BUFFER = []
WINDOW = 120

print("Pipeline started")

JSON_PATTERN = re.compile(
    r'^\{"light":-?\d+,"temperature":-?\d+\}$'
)

def send_command(cmd):
    ser.write((cmd + "\n").encode())


while True:

    line = ser.readline().decode(errors="ignore").strip()

    if not line:
        continue

    if not JSON_PATTERN.match(line):
        continue

    try:
        data = json.loads(line)

        BUFFER.append(data)

        print("sensor:", data)

        with open(JSONL_FILE, "a") as f:
            f.write(json.dumps(data) + "\n")

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

            advice = result.get("rule_based_comfort", "")

            if advice == "too hot":
                send_command("LED_ON")
            elif advice == "low light":
                send_command("LED_ON")
            else:
                send_command("LED_OFF")

            BUFFER.clear()

    except Exception as e:
        print("pipeline error:", e)