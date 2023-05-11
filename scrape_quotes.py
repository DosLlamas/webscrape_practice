from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"
response = requests.get(url)
doc = BeautifulSoup(response.text, "html.parser")
# print(doc.prettify())
# quotes = doc.find_all(class_="text")
quote_containers = doc.find_all(class_="quote")
for quote_container in quote_containers:
    print("----------------------------------------")
    print("Quote:")
    print(quote_container.find(class_="text").text)
    print("Author:")
    print(quote_container.find("span").find_next()
        .find(class_="author").text)
    print("Tag(s):")
    tags = lambda tags: [print(tag.text) for tag in tags]
    print(tags(quote_container.find_all(class_="tag")))
    print("URL:")
    print(url)
    print()


# quote_text = quote.

