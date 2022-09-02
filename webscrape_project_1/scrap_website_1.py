"""
get video links from the web page
"""

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')  # contains complete html code of the page

csv_output_file = open('output/scraped_data_1.csv', 'w')
csv_writer = csv.writer(csv_output_file)# add headers to csv
csv_writer.writerow(['headline', 'summary', 'video_link'])


# list of all articles
articles = soup.find_all('article')
for article in articles:
    try:
        # get fields data
        headline = article.header.h2.a.text
        summary = article.find('div', class_='entry-content').p.text
        video_link = article.find('iframe', class_='youtube-player')['src']

        # get id from url (between last '/' and '?')
        id_start_index = video_link.rindex('/') + 1
        video_id = video_link[id_start_index:].split('?')[0]

        youtube_link = f'https://www.youtube.com/watch?v={video_id}'
    except TypeError as TE:
        # print("can't process the link, set to None")
        youtube_link = None

    # save scraped data to csv
    csv_writer.writerow([headline, summary, youtube_link])

csv_output_file.close()
