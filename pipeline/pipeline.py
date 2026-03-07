import serial
import json
import time
import requests

PORT = "/dev/cu.usbmodem101"
BAUD = 9600

SERVER_URL = "http://127.0.0.1:8000/data"

BUFFER = []
WINDOW = 60


ser = serial.Serial(PORT, BAUD)


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

            print("AI response:", r.json())

            BUFFER.clear()

    except:
        pass