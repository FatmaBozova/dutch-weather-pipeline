import json
from datetime import datetime
from pathlib import Path

import requests

URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {
    "latitude": 52.37,
    "longitude": 4.90,
    "hourly": "temperature_2m,precipitation,wind_speed_10m",
    "past_days": 7,
    "timezone": "Europe/Amsterdam",
}


def fetch_weather():
    response = requests.get(URL, params=PARAMS, timeout=30)
    response.raise_for_status()
    return response.json()


def save_raw(data):
    folder = Path("data/raw")
    folder.mkdir(parents=True, exist_ok=True)
    filename = folder / f"weather_{datetime.now():%Y%m%d_%H%M%S}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return filename


def main():
    data = fetch_weather()
    path = save_raw(data)
    print(f"Saved {len(data['hourly']['time'])} hourly rows to {path}")


if __name__ == "__main__":
    main()
