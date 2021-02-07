pip install BeautifulSoup4

import requests
from bs4 import BeautifulSoup

# pull html from website
response = requests.get("https://https://covid19.ncdc.gov.ng/")
html = response.text

# extract data from html

soup = BeautifulSoup(html, "html.parser")
# get the table headings e,g states affected, cases confirmed. headings are in the 'th' in source code
headings = soup.find_all("th")
headings_str = []
for item in headings:
    headings_str.append(str(item).lstrip("<th>").rstrip("</th>"))

print(headings_str)
# get table rows
rows = soup.find_all("td")
rows_str = []
for item in rows:
    rows_str.append(str(item).lstrip("<td>").rstrip("</td>"))
print(rows_str)
