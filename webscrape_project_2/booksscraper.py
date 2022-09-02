# make the proof of concept
# get the data about the books

#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup


"""
from https://pypi.org/project/requests/

>>> import requests
>>> r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"authenticated": true, ...'
>>> r.json()
{'authenticated': True, ...}
"""
url = 'https://www.humblebundle.com/bundles'

# make get request
http_response = requests.get(url)
# print(http_response.status_code)

# parse the request with BeautifulSoup lib
soup = BeautifulSoup(http_response.text, 'html.parser')
# print(soup.prettify())

bundle_names = soup.select('div.landing-mosaic-section')
print(bundle_names)
for bundle_name in bundle_names:
    print(bundle_name.text)
