import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
df = pd.read_csv("books_dataset.csv")

# Clean price
df["Price"] = df["Price"].str.replace("£", "").astype(float)

# -------------------------------
# Graph 1: Price Distribution
# -------------------------------

plt.figure(figsize=(10, 5))

sns.histplot(df["Price"], bins=8)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.savefig("price_distribution.png", bbox_inches="tight")

plt.show()


# -------------------------------
# Graph 2: Top 10 Expensive Books
# -------------------------------

top_books = df.sort_values("Price", ascending=False).head(10)

plt.figure(figsize=(10, 6))

sns.barplot(data=top_books, x="Price", y="Title")

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")

plt.savefig("top_10_expensive_books.png", bbox_inches="tight")

plt.show()