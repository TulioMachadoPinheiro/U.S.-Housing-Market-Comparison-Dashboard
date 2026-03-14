import os
import json
import requests
from dotenv import load_dotenv
from pathlib import Path

NEW_STATE_ZIPS = {
    "Colorado": ["80219", "80013"],
    "Illinois": ["60629", "60632"],
    "Georgia": ["30044", "30349"]
}

project_root = Path(__file__).resolve().parents[2]
env_path = project_root / ".env"
output_dir = project_root / "data" / "raw" / "rentcast_sale_listings"

load_dotenv(env_path)
api_key = os.getenv("RENTCAST_API_KEY")

headers = {
    "X-Api-Key": api_key
}

url = "https://api.rentcast.io/v1/listings/sale"

output_dir.mkdir(parents=True, exist_ok=True)

total_requests = 0

for state, zip_list in NEW_STATE_ZIPS.items():
    for zip_code in zip_list:
        params = {
            "zipCode": zip_code,
            "limit": 10
        }

        response = requests.get(url, headers=headers, params=params)
        total_requests += 1

        print(f"{state} | {zip_code} | Status: {response.status_code}")

        output_path = output_dir / f"sale_listings_{zip_code}.json"

        if response.status_code == 200:
            data = response.json()

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)

            count = len(data) if isinstance(data, list) else "Not a list"
            print(f"Saved: {output_path.name} | Records: {count}")
        else:
            print("Error preview:", response.text[:500])

print("Finished.")
print("Total requests used:", total_requests)