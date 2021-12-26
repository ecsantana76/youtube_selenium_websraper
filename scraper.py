from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

if __name__ == "__main__":
  print('Creating Driver')
  driver = get_driver()

  print('Fetching the Page')
  driver.get(YOUTUBE_TRENDING_URL)

  print('Getting the Video Divs')
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  get_video_divs = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)

  print(f'Found {len(get_video_divs)} Videos')
