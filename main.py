import time
from selenium import webdriver

url = "https://www.soccerstats.com/"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(10)