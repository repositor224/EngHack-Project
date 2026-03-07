from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

app = FastAPI()


class SensorData(BaseModel):
    device_id: str
    timestamp: float
    temperature: float
    light: float


def call_gemini(prompt: str) -> str:
    if not API_KEY:
        return "AI unavailable: missing API key"

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(
            url,
            params={"key": API_KEY},
            json=payload,
            timeout=20
        )

        result = response.json()

        if response.status_code != 200:
            print("Gemini HTTP error:", response.status_code, result)
            return "AI analysis failed"

        return result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        print("Gemini error:", e)
        return "AI analysis failed"


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

    prompt = f"""
You are an indoor environment assistant.

Temperature: {data.temperature} C
Light level: {data.light}

Give one short suggestion about whether this room is comfortable for studying or working.
"""

    ai_advice = call_gemini(prompt)

    return {
        "status": "ok",
        "rule_based_comfort": comfort,
        "ai_advice": ai_advice
    }