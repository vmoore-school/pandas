import pandas as pd

df = pd.read_csv('pixel_cafe_sales.csv')
# print(df)
# print(df.shape)
# print(df.columns)
# print(df[["Product", "Quantity"]])
print(df[(df["Category"] == "Food") & (df["Product"] == "Crisps")])
