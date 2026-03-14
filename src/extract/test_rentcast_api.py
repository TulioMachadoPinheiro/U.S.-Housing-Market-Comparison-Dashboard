import os
import requests
from dotenv import load_dotenv
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
env_path = project_root / ".env"

load_dotenv(env_path)

api_key = os.getenv("RENTCAST_API_KEY")

print("API key loaded:", bool(api_key))

url = "https://api.rentcast.io/v1/listings/sale"
headers = {
    "X-Api-Key": api_key
}
params = {
    "zipCode": "02108",
    "limit": 5
}

response = requests.get(url, headers=headers, params=params)

print("Status code:", response.status_code)
print("Response preview:", response.text[:500])