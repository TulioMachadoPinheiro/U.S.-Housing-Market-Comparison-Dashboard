import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
csv_path = project_root / "data" / "cleaned" / "sale_listings_cleaned.csv"

params = quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=housing_market_db;"
    "Trusted_Connection=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

df = pd.read_csv(csv_path)

date_columns = ["listedDate", "removedDate", "createdDate", "lastSeenDate"]

for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce", utc=True)
        df[col] = df[col].dt.tz_localize(None)

df.to_sql("sale_listings_cleaned", engine, if_exists="append", index=False)

print("Loaded cleaned sale listings into SQL Server.")
print("Rows loaded:", len(df))