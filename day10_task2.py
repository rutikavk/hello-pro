import pandas as pd
data = {
    "Product": ["A", "B", "C"],
    "Price": ["$120.50", "$300.00", "$45.99"],
    "Date": ["2025-01-05", "2025-02-10", "2025-03-15"]
}
df = pd.DataFrame(data)
print("Initial Data Types:")
print(df.dtypes)
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])
print("\nUpdated Data Types:")
print(df.dtypes)
print("\nCleaned Data:")
print(df)
