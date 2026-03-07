import serial
import json

ser = serial.Serial("/dev/cu.usbmodem101",9600)

outfile = open("sensor_stream.jsonl","a")

while True:

    line = ser.readline().decode(errors="ignore").strip()

    if not line.startswith("{"):
        continue

    try:
        data = json.loads(line)

        data["timestamp"] = time.time()

        print("data:", data)

        outfile.write(json.dumps(data) + "\n")
        outfile.flush()

    except:
        print("invalid data:", line)