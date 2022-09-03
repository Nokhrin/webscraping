from bs4 import BeautifulSoup
import requests
import openpyxl
import config

# create Excel workbook object
workbook = openpyxl.Workbook()
spreadsheet = workbook.active
spreadsheet.title = 'Top Raited Movies'
# headers
spreadsheet.append(['Rank', 'Name', 'Year', 'Raiting'])



try:
    page_source = requests.get(f'{config.URL}')
    page_source.raise_for_status()

    soup = BeautifulSoup(page_source.text, 'html.parser')

    movies = soup.find('tbody', class_=config.TBODY_CLASS)
    movies_list = movies.find_all('tr')

    for movie in movies_list:
        movie_name = movie.find('td', class_=config.NAME_CLASS).a.text
        movie_rank_dirty = movie.find('td', class_=config.NAME_CLASS).text
        movie_rank = movie_rank_dirty.split('.')[0].strip()
        movie_year_dirty = movie.find('td', class_=config.NAME_CLASS).find('span', class_=config.YEAR_CLASS).text
        movie_year = movie_year_dirty.strip('()')
        movie_raiting = movie.find('td', class_=config.RAITING_CLASS).strong.text

        # write row to excel file
        spreadsheet.append([movie_rank, movie_name, movie_year, movie_raiting])

except Exception as e:
    print(e)

# save and close spreadsheet
workbook.save(filename=config.FILENAME)
