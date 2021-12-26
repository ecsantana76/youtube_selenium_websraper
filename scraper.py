from selenium import webdriver

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

driver.get(YOUTUBE_TRENDING_URL)
print('Page Title ', driver.title)