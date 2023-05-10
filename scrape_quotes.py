from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"
response = requests.get(url)
doc = BeautifulSoup(response.text, "html.parser")
# print(doc.prettify())
quotes = doc.find_all(class_="text")
for quote in quotes:
    print(quote.text)