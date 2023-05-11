from bs4 import BeautifulSoup
import requests

# Colors for print statemts
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

url = "https://quotes.toscrape.com/"
response = requests.get(url)
doc = BeautifulSoup(response.text, "html.parser")
# print(doc.prettify())
quote_containers = doc.find_all(class_="quote")
for quote_container in quote_containers:
    print(f"{bcolors.WARNING}----------------------------------------{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Quote: {bcolors.ENDC}")
    print(quote_container.find(class_="text").text)
    print(f"{bcolors.OKBLUE}Author: {bcolors.ENDC}")
    print(quote_container.find("span").find_next()
        .find(class_="author").string)
    print(f"{bcolors.OKBLUE}Tag(s): {bcolors.ENDC}")
    tags = lambda tags: [print(tag.text) for tag in tags]
    print(tags(quote_container.find_all(class_="tag")))
    print(f"{bcolors.OKBLUE}URL: {bcolors.ENDC}")
    print(url)
    print()

