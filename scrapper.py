import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip()

    data.append({
        "Title": title,
        "Price": price
    })

df = pd.DataFrame(data)

df.to_csv("books_dataset.csv", index=False, encoding="utf-8-sig")

print("Dataset created successfully!")
print(df)