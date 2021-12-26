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

def get_videos(driver):
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  driver.get(YOUTUBE_TRENDING_URL)
  videos = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
  return videos

if __name__ == "__main__":
  driver = get_driver()
  videos = get_videos(driver)
  
  video = videos[0]
  title_tag = video.find_element(By.ID, 'video-title')
  
  title = title_tag.text
  url = title_tag.get_attribute('href')

  print(f'Found {len(videos)} Videos')
  print('First Video Title: ', title)
  print('First Video URL: ', url)
