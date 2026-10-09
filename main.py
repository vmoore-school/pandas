import pandas as pd

df = pd.read_csv('pixel_cafe_sales.csv')

# print(df)

# print(df.shape)

# print(df.columns)

# print(df[["Product", "Quantity"]])

# print(df[(df["Category"] == "Food") & (df["Product"] == "Crisps")])

# df["Revenue"] = df["Price"] * df["Quantity"]
# print(df[["Price", "Quantity", "Revenue"]])

# print(f"Total potential revenue = £{(df["Price"] * df["Quantity"]).sum()}")
