from bs4 import BeautifulSoup
import requests
from csv import writer

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

# scrape site logic
url = "https://quotes.toscrape.com/"
response = requests.get(url)
doc = BeautifulSoup(response.text, "html.parser")
quote_containers = doc.find_all(class_="quote")

with open('nathan_quotes.csv', 'w') as csv_file:
    # helper function for tags
    def get_csv_tag_texts(tags):
        tag_texts = []
        for tag in tags:
            tag_texts.append(tag.text)
        return tag_texts
    csv_writer = writer(csv_file)
    headers = ['Quote', 'Author', 'Tags', 'URL']
    csv_writer.writerow(headers)
    for quote_container in quote_containers:
        # All print logic
        print(f"{bcolors.WARNING}----------------------------------------{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}Quote: {bcolors.ENDC}")
        quote = quote_container.find(class_="text").text
        print(quote)
        print(f"{bcolors.OKBLUE}Author: {bcolors.ENDC}")
        author = quote_container.find("span").find_next().find(class_="author").string
        print(author)
        print(f"{bcolors.OKBLUE}Tag(s): {bcolors.ENDC}")
        each_tag = lambda tags: [print(tag.text) for tag in tags]
        all_tags = quote_container.find_all(class_="tag")
        print(each_tag(all_tags))
        print(f"{bcolors.OKBLUE}URL: {bcolors.ENDC}")
        print(url)
        print()
        # All csv file logic
        csv_writer.writerow([quote, author, get_csv_tag_texts(all_tags), url])



