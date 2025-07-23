# Import Required Libraries
from urllib.request import urlopen as o
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd

# Step 1: Fetch and Parse the Website
url = "https://books.toscrape.com/"
book = o(url)
html = book.read()
soup = bs(html, "html.parser")

# Step 2: Find Book Containers
containers = soup.findAll("article", {"class": "product_pod"})

# Step 3: Create CSV File and Add Headers
filename = "books.csv"
f = open(filename, "w", encoding='utf-8')
header = "Title,Price,Availability,Rating,Link\n"
f.write(header)

# Step 4: Extract Data for Each Book and Write to CSV
for book in containers:
    title = book.h3.a.attrs['title'].replace(",", "")
    price = book.find("p", {"class": "price_color"}).text.strip()
    availability = book.find("p", {"class": "instock availability"}).text.strip()
    rating = book.p.attrs['class'][1]
    link = book.h3.a.attrs['href']
    f.write(f"{title},{price},{availability},{rating},{link}\n")

f.close()

# Step 5: Data Validation Using Pandas
df = pd.read_csv("books.csv")
print(df.head())
