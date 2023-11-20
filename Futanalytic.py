from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep as slp

def caminho(liga):
    driver = webdriver.Chrome()

    driver.get("https://www.soccerstats.com/matches.asp?matchday=4")

    try:
        # Fechando o Ad inicial
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[3]").click()
    except Exception as e:
        print("Ele n possui ads iniciais")

    slp(0.5)
    table_game = encontrando_jogos(driver,liga)

    for i in table_game :
        driver.get("https://www.soccerstats.com/"+ i)


#Retorna os links das partidas da liga
def encontrando_jogos(driver,liga):
    tabela_resultado = []

    slp(2)
    tabela = driver.find_element(By.XPATH,f"//div/table[3]/tbody/tr/td/table//font[@size=2][contains(text(),'{liga}')]/../../../..").get_attribute('outerHTML')
    soup = BeautifulSoup(tabela,"html.parser")

    for tabela_jogos in soup.findAll('a', {'class':'myButton'}):
        tabela_resultado.append(tabela_jogos.get('href'))

    return tabela_resultado

class Partida:
    def __init__(self,driver,liga):
        self.driver = driver
        self.liga = liga
        #self.timeCasa = driver.find_element(By.XPATH,'//td/font/a[1]').text
        #self.timeFora = driver.find_element(By.XPATH,'//td/font/a[1]').text


    def macaco(self):
        pass


if __name__ == '__main__':
    liga = "Albania - Abissnet Superiore"
    caminho(liga)
