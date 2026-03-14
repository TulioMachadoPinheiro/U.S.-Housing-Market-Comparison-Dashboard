import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
csv_path = project_root / "data" / "raw" / "zip_reference.csv"

params = quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=housing_market_db;"
    "Trusted_Connection=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

df = pd.read_csv(csv_path)

df.to_sql("zip_reference", engine, if_exists="replace", index=False)

print("Loaded ZIP reference into SQL Server.")
print("Rows:", len(df))
print("Columns:", list(df.columns))