import json
import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
input_dir = project_root / "data" / "raw" / "rentcast_sale_listings"
output_path = project_root / "data" / "raw" / "all_sale_listings_raw.csv"

all_records = []

for json_file in input_dir.glob("sale_listings_*.json"):
    zip_code = json_file.stem.replace("sale_listings_", "")

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        for record in data:
            if isinstance(record, dict):
                record["source_zip"] = zip_code
                all_records.append(record)

df = pd.DataFrame(all_records)

df.to_csv(output_path, index=False)

print("Combined file saved to:", output_path)
print("Rows:", len(df))
print("Columns:", list(df.columns))