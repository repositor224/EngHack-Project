import serial
import json

ser = serial.Serial("/dev/cu.usbmodem101",9600)

while True:

    line = ser.readline().decode(errors="ignore").strip()

    if not line.startswith("{"):
        continue

    try:
        data = json.loads(line)
        print("data:", data)

    except Exception:
        print("invalid data:", line)