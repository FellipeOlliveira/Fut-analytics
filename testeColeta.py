from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup

def telaInvisivel():
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")

    return option


if __name__ == '__main__':
    url = 'https://www.soccerstats.com/pmatch.asp?'