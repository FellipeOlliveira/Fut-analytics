#pip install selenium
#pip install seleniumbase
#pip install requests2
#pip install lxml
#pip install pandas
#pip install beautifulsoup4

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
from seleniumbase import BaseCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Define a Url Inical do Projeto
def iniciando():
    url = "https://www.soccerstats.com/matches.asp?matchday=4"
    return url

#Coloca os parametros para fazer o WebScrapping sem abrir o navegador PS: Recomendo testar, é divertido
def telaInvisivel():
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")

    return option

#Junta as Duas funcoes anteriores em uma e cria o driver, que é o navegador q iremos ultilizar no projeto
def criandoPagina():
    #1°Variaveis de inicialização
    url = iniciando()
    driver = webdriver.Chrome() #passar parametro options=telaInvisivel() dentro do Chrome() para deixar ele invisivel

    driver.get(url)

    return driver

#Aq de fato começa o programa
def caminhoDados():

    driver = criandoPagina()
    time.sleep(1)#pra ter ctz de q os dados foram devidamente carregados na pagina

    try:
        #Fechando o Ad inicial
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button[3]").click()
    except Exception  as e:
        print("Ele n possui ads iniciais")

    #Pegar os elementos da tabela(Teste para fazer a raspagem dos dados
    element = driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/table[3]')
    html_content = element.get_attribute('outerHTML')
    print(html_content)


    #seleciona a liga
    #driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div/table[3]/tbody/tr/td/table[1]/tbody/tr[2]/td[1]/a').click()
    time.sleep(5)

    return driver

#Estou testando essa parte no Teste.py, aq eu comparo as ligas e escolho as partidas
def coletarDados():
    pass

if __name__ == '__main__':

    ini = time.time()
    caminhoDados()
    #coletarDados()
    final = time.time()
    total = final - ini
    print(total)
