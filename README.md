# 📚 Books Scraper – End-to-End Data Project

## 📌 Project Overview

This project is a Python web scraping tool that extracts book data from [https://books.toscrape.com](https://books.toscrape.com).

It collects structured data such as title, price, rating, stock availability, image URL, and book URL, and stores it in CSV and SQLite database for analysis.

---

## 🎯 Features

* Scrapes multiple pages automatically (pagination)
* Extracts book details:

  * Title
  * Price
  * Rating
  * Stock availability
  * Book URL
  * Image URL
* Saves data into:

  * CSV file
  * SQLite database

---

## ⚙️ Tech Stack

* Python
* Requests
* BeautifulSoup4
* SQLite3
* CSV
* urllib

---

## 🚀 How to Run

### 1. Clone repo

git clone [https://github.com/your-username/books-scraper.git](https://github.com/your-username/books-scraper.git)
cd books-scraper

---

### 2. Create virtual environment

python -m venv .venv
source .venv/bin/activate

---

### 3. Install dependencies

pip install requests beautifulsoup4

---

### 4. Run script

python scraper_books.py

---

## 🗄️ SQLite Table

CREATE TABLE books (
title TEXT,
price TEXT,
rating TEXT,
stock TEXT,
book_url TEXT,
image_url TEXT
);

---

## 📁 Output Files

* books_info.csv
* books_sql.db

---

## 📈 Future Improvements

* Data cleaning
* Streamlit dashboard
* API version
* Store in PostgreSQL

---

## 👨‍💻 Author

Your Name

---

إلى بغيتي نخليه **أكثر احترافي (GitHub ready 100%) مع badges و screenshots** قولها 👍
