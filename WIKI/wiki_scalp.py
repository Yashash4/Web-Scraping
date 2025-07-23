import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Step 1: Load the webpage
url = 'https://en.wikipedia.org/wiki/Comparison_of_programming_languages'
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")

# Step 2: Find the data table
table = soup.find('table', {'class': 'wikitable'})
rows = table.find_all('tr')

# Step 3: Open CSV file to write
with open('programming.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Write the header
    writer.writerow([
        "Language", "Original Purpose", "Imperative", "Object-oriented",
        "Functional", "Procedural", "Generic", "Reflective", "Other Paradigms"
    ])

    # Step 4: Loop through table rows and write data
    for row in rows[1:]:
        cols = row.find_all(['td', 'th'])
        if len(cols) >= 9:
            data = [col.text.strip().replace(',', '') for col in cols[:9]]
            writer.writerow(data)
