from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

app = FastAPI()


class SensorData(BaseModel):
    device_id: str
    timestamp: float
    temperature: float
    light: float


def call_gemini(prompt: str):

    if not API_KEY:
        print("No API key")
        return "AI offline", ""

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

        if response.status_code != 200:
            print("Gemini HTTP error:", response.status_code)
            print(response.text)
            return "AI error", ""

        result = response.json()

        # 安全获取文本
        text = result["candidates"][0]["content"]["parts"][0]["text"]

        # 清理 markdown
        text = text.strip()
        text = text.replace("```json", "")
        text = text.replace("```", "")

        try:
            parsed = json.loads(text)

            line1 = parsed.get("AIadvice1", "")[:16]
            line2 = parsed.get("AIadvice2", "")[:16]

            return line1, line2

        except Exception as parse_error:
            print("JSON parse failed:", parse_error)
            print("Raw Gemini output:", text)

            return "AI parse fail", ""

    except Exception as e:
        print("Gemini request error:", e)
        return "AI failed", ""


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
You are an embedded device assistant.

Temperature: {data.temperature} C
Light level: {data.light}

Return ONLY valid JSON.

Rules:
1. Output must be JSON
2. Two fields only: AIadvice1 and AIadvice2
3. Each line MAX 16 characters including spaces
4. No explanation text
5. No markdown

Example format:
{{
"AIadvice1": "Good lighting",
"AIadvice2": "Temp is normal"
}}
"""

    line1, line2 = call_gemini(prompt)

    return {
        "status": "ok",
        "rule_based_comfort": comfort,
        "AIadvice1": line1,
        "AIadvice2": line2
    }