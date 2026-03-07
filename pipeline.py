import serial
import json
import requests

ser = serial.Serial('/dev/ttyUSB0', 9600)

API_URL = "https://your-api-endpoint"

while True:
    line = ser.readline().decode().strip()

    try:
        data = json.loads(line)

        r = requests.post(API_URL, json=data)

        print("sent:", data, r.status_code)

    except:
        print("invalid data:", line)