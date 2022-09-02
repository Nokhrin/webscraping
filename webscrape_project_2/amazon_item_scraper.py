from bs4 import BeautifulSoup
import requests
import csv
import datetime
import re
import config


page = requests.get(url=config.URL, headers=config.HEADERS)
# print(page.status_code)

# get page content
soup_1 = BeautifulSoup(page.content, 'html.parser')
# print(soup_1.prettify())

# get title
title_obj = soup_1.find(id='productTitle').get_text()
title = title_obj.strip()
# remove all special characters - lazy way :)
title = re.sub(r'[^a-zA-Z0-9 ]', ' ', title)
# print(f'title: {title}')

# get price
# class = 'a-price aok-align-center'
price_obj = soup_1.find('span', class_='a-price')
price_obj = price_obj.find('span', class_='a-offscreen')
price = float(price_obj.text[1:])
# print(f'price: {price}')

# get color
color_obj = soup_1.find('div', id='variation_color_name')
color_obj = color_obj.find('span', class_='selection')
color = color_obj.text.lower()
# print(f'color: {color}')

# get timestamp
date_now = datetime.date.today()

# pack the data into list
header = ['title', 'price', 'color', 'date']
data = [title, price, color, date_now]
# print(f'{type(data)}: {data}')

# save data to csv file
with open(config.CSV_FILENAME, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
