import pandas as pd

data = [
    {
        "state": "Massachusetts",
        "city": "Boston",
        "zip_code": "02108",
        "price": 950000,
        "year_built": 1890,
        "sq_ft": 1200
    },
    {
        "state": "Texas",
        "city": "Austin",
        "zip_code": "78701",
        "price": 675000,
        "year_built": 2008,
        "sq_ft": 980
    },
    {
        "state": "Florida",
        "city": "Miami",
        "zip_code": "33131",
        "price": 820000,
        "year_built": 2015,
        "sq_ft": 1105
    }
]

df = pd.DataFrame(data)

output_path = "data/raw/sample_properties.csv"
df.to_csv(output_path, index=False)

print("File saved to:", output_path)
print(df)