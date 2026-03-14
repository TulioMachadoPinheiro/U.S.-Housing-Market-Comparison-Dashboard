import pandas as pd
from pathlib import Path

url = "https://raw.githubusercontent.com/scpike/us-state-county-zip/master/geo-data.csv"

project_root = Path(__file__).resolve().parents[2]
output_path = project_root / "data" / "raw" / "zip_reference.csv"

output_path.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(url)
df.to_csv(output_path, index=False)

print("ZIP reference downloaded.")
print("Saved to:", output_path)
print("Rows:", len(df))
print("Columns:", list(df.columns))