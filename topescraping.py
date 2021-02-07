import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bellanaija.com/")
html = response.text


soup = BeautifulSoup(html, "html.parser")

titles = soup.find_all("h2")
titles_str = []
for item in titles:
    titles_str.append(str(item).lstrip("<h2>").rstrip("</h2"))


print(titles_str)


