import pandas as pd

# Read dataset
df = pd.read_csv("books_dataset.csv")

# Remove £ symbol and convert Price to number
df["Price"] = df["Price"].str.replace("£", "").astype(float)

print("Data types after cleaning:")
print(df.dtypes)

print("\nAverage price:")
print(df["Price"].mean())

print("\nMinimum price:")
print(df["Price"].min())

print("\nMaximum price:")
print(df["Price"].max())

print("\nMost expensive book:")
print(df.loc[df["Price"].idxmax(), "Title"])

print("\nCheapest book:")
print(df.loc[df["Price"].idxmin(), "Title"])

print("\nPrice statistics:")
print(df["Price"].describe())