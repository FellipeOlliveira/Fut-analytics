#pip install selenium
#pip install requests2
#pip install lxml
#pip install pandas
#pip install beautifulsoup4

import datetime
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#parametros iniciais
def iniciando(selector):
    url = "https://www.soccerstats.com/"

    dataAtual = datetime.date.today()
    dataFutura = dataAtual + datetime.timedelta(days=3)
    if selector == "url":
        return url

    elif selector == "dataFutura":
        return dataFutura
    else:
        print("Deu merda")

#pagina invisivel
def telaInvisivel():
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")

    return option
#iniciando pagina
def criandoPagina():
#1°Variaveis de inicialização
    url = iniciando("url")
    data = iniciando("dataFutura")
    driver = webdriver.Chrome() #passar parametro options=telaInvisivel()

    driver.get(url)

    return driver
def caminhoDados():

    driver = criandoPagina()
    time.sleep(5)#pra ter ctz de q os dados foram devidamente carregados na pagina

    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button[3]").click()


#3°Passo : Simulando o Click de entrada na area desejada do site(times por data)
    driver.find_element(By.CLASS_NAME,'ui-datepicker-trigger').click() #clicando no button data

    time.sleep(2)

    time.sleep(8)
    driver.quit()

if __name__ == '__main__':

    caminhoDados()