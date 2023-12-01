from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep as slp

def telaInvisivel():
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")

    return option

def analise(url):
    driver = webdriver.Chrome()

    driver.get(url)

    try:
        driver.find_element(By.XPATH, "//div[2]/div/button[3]").click()
    except Exception as e:
        print("sem ads iniciais")

    slp(1)
    timeCasa = driver.find_element(By.XPATH,'//div[@class="row"]/div[@class="six columns"][1]/h3[1]').text
    timeFora = driver.find_element(By.XPATH,'//div[@class="row"]/div[@class="six columns"][2]/h3[1]').text

    print(timeCasa,timeFora)


if __name__ == '__main__':
    url = 'https://www.soccerstats.com/leagueview_team.asp?league=uefa&team1id=24&team2id=23&fmid=67'

    analise(url)

