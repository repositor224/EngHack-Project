from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SensorData(BaseModel):
    device_id: str
    timestamp: float
    temperature: float
    light: float

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/data")
def receive_data(data: SensorData):

    print("received:", data)

    comfort = "normal"

    if data.temperature > 25:
        comfort = "too hot"

    if data.light < 150:
        comfort = "low light"

    return {
        "status": "ok",
        "comfort": comfort
    }