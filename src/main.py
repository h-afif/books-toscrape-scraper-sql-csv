import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv
import sqlite3


url = "https://books.toscrape.com/catalogue/page-1.html"
base_url = "https://books.toscrape.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
}

data = []
page_number = 1

while True:

    print("Page Number:", page_number)
    time.sleep(1)
    
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")

    info_books = soup.find_all("article", class_="product_pod")

    for info in info_books:
        book_link = info.find("a").get("href")
        img_link = info.find("img").get("src")
        rating = info.p["class"][1]
        title = info.h3.find("a").get("title")
        price = info.find("p", class_="price_color").text
        stock = info.find("p", class_="instock availability").text.strip()

        data.append({
            "Book link": base_url + book_link,
            "Img link": base_url + img_link,
            "Rating": rating,
            "Title": title,
            "Price": price,
            "Stock": stock
        })

    next_button = soup.find("li", class_="next")
    if next_button:
        next_url = next_button.find("a").get("href")
        url = urljoin(base_url + "/catalogue/page-1.html", next_url)
        print(url)
        print(next_url)
    else:
        print("End Of The Pages")
        break
    page_number += 1


with open("outputs/books_info.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Book link", "Img link", "Rating", "Title", "Price", "Stock"])

    for item in data:
        writer.writerow([
            item["Book link"],
            item["Img link"],
            item["Rating"],
            item["Title"],
            item["Price"],
            item["Stock"]
        ])

conn = sqlite3.connect("outputs/books_sql.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
               title TEXT,
               price TEXT,
               rating TEXT,
               stock TEXT,
               book_url TEXT,
               image_url TEXT
)
""")

cursor.executemany("""
INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)
""", [
    (
        item["Title"],
        item["Price"],
        item["Rating"],
        item["Stock"],
        item["Book link"],
        item["Img link"]
    )
    for item in data
])

conn.commit()
conn.close()

