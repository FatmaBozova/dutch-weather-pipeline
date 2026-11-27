import json
from pathlib import Path

import pandas as pd


def load_latest_raw():
    files = sorted(Path("data/raw").glob("weather_*.json"))
    if not files:
        raise FileNotFoundError("No raw files found. Run fetch_weather.py first.")
    with open(files[-1], encoding="utf-8") as f:
        return json.load(f)


def to_dataframe(data):
    df = pd.DataFrame(data["hourly"])
    df = df.rename(
        columns={
            "time": "observed_at",
            "temperature_2m": "temperature_c",
            "precipitation": "precipitation_mm",
            "wind_speed_10m": "wind_speed_kmh",
        }
    )
    df["observed_at"] = pd.to_datetime(df["observed_at"])
    return df


def main():
    data = load_latest_raw()
    df = to_dataframe(data)
    print(df.head())
    print(df.shape)


if __name__ == "__main__":
    main()