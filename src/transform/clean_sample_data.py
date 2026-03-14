import pandas as pd

input_path = "data/raw/sample_properties.csv"
output_path = "data/cleaned/sample_properties_cleaned.csv"

df = pd.read_csv(input_path)

df["price_per_sq_ft"] = df["price"] / df["sq_ft"]

df.to_csv(output_path, index=False)

print("Cleaned file saved to:", output_path)
print(df)