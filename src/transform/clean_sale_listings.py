import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]

input_path = project_root / "data" / "raw" / "all_sale_listings_raw.csv"
output_path = project_root / "data" / "cleaned" / "sale_listings_cleaned.csv"

df = pd.read_csv(input_path)

columns_to_keep = [
    "id",
    "formattedAddress",
    "addressLine1",
    "city",
    "state",
    "zipCode",
    "county",
    "latitude",
    "longitude",
    "propertyType",
    "bedrooms",
    "bathrooms",
    "squareFootage",
    "lotSize",
    "yearBuilt",
    "status",
    "price",
    "listingType",
    "listedDate",
    "removedDate",
    "createdDate",
    "lastSeenDate",
    "daysOnMarket",
    "mlsName",
    "mlsNumber",
    "source_zip",
    "hoa",
    "history"
]

existing_columns = [col for col in columns_to_keep if col in df.columns]
df = df[existing_columns].copy()

numeric_columns = [
    "bedrooms",
    "bathrooms",
    "squareFootage",
    "lotSize",
    "yearBuilt",
    "price",
    "daysOnMarket",
    "latitude",
    "longitude"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

date_columns = ["listedDate", "removedDate", "createdDate", "lastSeenDate"]

for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

if "price" in df.columns and "squareFootage" in df.columns:
    df["price_per_sq_ft"] = df["price"] / df["squareFootage"]

current_year = pd.Timestamp.now().year
if "yearBuilt" in df.columns:
    df["property_age"] = current_year - df["yearBuilt"]

df.to_csv(output_path, index=False)

print("Cleaned file saved to:", output_path)
print("Rows:", len(df))
print("Columns:", list(df.columns))