from bs4 import BeautifulSoup
import requests


with open('pages_examples/simple.html') as html_file:
    # beautiful soup object of parsed html file
    soup = BeautifulSoup(html_file, 'lxml') # contains all html code

# looping through all articles
for article in soup.find_all('div', class_='article'):
    # print(article)

    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary, '\n')

