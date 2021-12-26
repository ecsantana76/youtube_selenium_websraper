import requests as req
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

response = req.get(YOUTUBE_TRENDING_URL)

if response.status_code == 200:
  print('Request Successful')
else:
  print('Request Unsuccessful')

with open('trending.html', 'w') as f:
  f.write(response.text)



