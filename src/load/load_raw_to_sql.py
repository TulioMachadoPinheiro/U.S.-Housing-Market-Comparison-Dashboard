import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

csv_path = "data/raw/sample_properties.csv"

params = quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=housing_market_db;"
    "Trusted_Connection=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

df = pd.read_csv(csv_path)

df.to_sql("raw_properties", engine, if_exists="append", index=False)

print("Loaded raw data into SQL Server.")
print(df)