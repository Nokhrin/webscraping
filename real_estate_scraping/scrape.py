from bs4 import BeautifulSoup
import requests
from csv import writer

BASE_URL = 'https://www.pararius.com/apartments/amsterdam'
URL = 'https://www.pararius.com/apartments/amsterdam'

page = requests.get(url=URL)
# print(page)
# print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

lists = soup.find_all('section', class_='listing-search-item')

with open('output/appartments.csv', 'w', encoding='utf-8', newline='') as f:
    the_writer = writer(f)
    header = [
            'title',
            'location',
            'price',
            'area',
            'link'
        ]
    the_writer.writerow(header)

    for listing in lists:
        title = listing.find('a', class_='listing-search-item__link--title')
        title_clean = title.text.strip()

        location = listing.find('div', class_='listing-search-item__sub-title')
        location_clean = location.text.strip()

        price = listing.find('div', class_='listing-search-item__price')
        price_clean = price.text.strip()

        area = listing.find('li', class_='illustrated-features__item--surface-area')
        area_clean = area.text.strip()

        link = BASE_URL + title['href']
        listing_data = [
            title_clean,
            location_clean,
            price_clean,
            area_clean,
            link
        ]
        # print(listing_data)
        the_writer.writerow(listing_data)
