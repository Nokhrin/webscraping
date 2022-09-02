from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()

BASE_URL = 'https://www.webscraper.io'
URL = BASE_URL + '/test-sites/e-commerce/static/computers/laptops'

def get_data(url):
    """connect and get full page content"""
    response = s.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_next_page(soup):
    page = soup.find('ul', {'class': 'pagination'})
    # find 'next' button
    # page.a['rel'] = ['next']
    is_next_activated = page.find('li', {'class': 'disabled'})
    # is_next_activated
    print(is_next_activated)
    # if page.a:
    #     next_url = BASE_URL + page.a['href']
    #     return next_url
    # else:
    #     return None


# retrieve data
# url = URL
# while True:
#     pages_count = 0
#     page_data = get_data(url)
#     url = get_next_page(page_data)
#     if not get_next_page(page_data):
#         break
#     pages_count += 1
#     # print(url)
#
# print(f'number of pages found: {pages_count}')

page_data = get_data('https://www.webscraper.io/test-sites/e-commerce/static/computers/laptops?page=19')
get_next_page(page_data)