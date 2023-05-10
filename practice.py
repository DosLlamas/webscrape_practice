import requests
from bs4 import BeautifulSoup
from csv import writer

# find() or find_all() to return div(s) with that id or class 
# select() to return return div(s) with that id or class in a list
# when navigating soup.body.content, account for the line breaks
# with find_next_sibling() find_previous_sibling()
response = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(response.text, 'html.parser')

# To get a list of items with the same class
quote_container = soup.find_all(class_='quote')
print(quote_container)
# for item in quote_container:
#     print(item)

# with open('posts.csv', 'w') as csv_file:
#     csv_writer = writer(csv_file)
#     headers = ['Title', 'Link', 'Date']
#     csv_writer.writerow(headers)

#     for post in posts:
#         title = post.find(class_='post-title').get_text().replace('\n', '')
#         link = post.find('a')['href']
#         date = post.select('.post-date')[0].get_text()
#         csv_writer.writerow([title, link, date])

        