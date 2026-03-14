import os
import json
import requests
from dotenv import load_dotenv
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
env_path = project_root / ".env"
output_path = project_root / "data" / "raw" / "sale_listings_02108.json"

load_dotenv(env_path)

api_key = os.getenv("RENTCAST_API_KEY")

url = "https://api.rentcast.io/v1/listings/sale"
headers = {
    "X-Api-Key": api_key
}
params = {
    "zipCode": "02108",
    "limit": 10
}

response = requests.get(url, headers=headers, params=params)

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("File saved to:", output_path)
    print("Number of records returned:", len(data) if isinstance(data, list) else "Not a list")
else:
    print("Response preview:", response.text[:1000])