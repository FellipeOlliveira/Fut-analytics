from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep as slp

def caminho(liga):
    games = []
    contador = 1
    driver = webdriver.Chrome()

    driver.get("https://www.soccerstats.com/matches.asp?matchday=4")

    try:
        # Fechando o Ad inicial
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[3]").click()
    except Exception as e:
        print("Ele n possui ads iniciais")

    table_game = encontrando_jogos(driver,liga)

    for i in table_game :
        driver.get("https://www.soccerstats.com/"+ i)
        try:
            try:
                driver.find_element(By.XPATH,"//*[@id='dismiss-button']/div/span").click()
            except Exception as e:
                print("sem ads iniciais")


            timeCasa = driver.find_element(By.XPATH,'//td/font/a[1]').text
            timeFora = driver.find_element(By.XPATH,'//td/font/a[2]').text
            partida = Partida(driver,liga,timeCasa,timeFora)
            partida.homeAway = partida.requisito_Home_Away_Table(timeCasa,timeFora,driver)

            driver.find_element(By.XPATH, '//table[4]/tbody/tr[6]/td/span/a[@class="myButton"]').click()

            slp(3)
            #partida.result = partida.requisito_Results_Table(timeCasa,timeFora,driver)
            #partida.leading = partida.requisito_Leading_Table(timeCasa,timeFora,driver)
            #partida.goalScorred = partida.requisito_Goal_Scorred(timeCasa,timeFora,driver)
            #partida.stts = partida.requisitos_Stts_Times(timeCasa,timeFora,driver)

            games.append(partida)
            print(partida)

        except Exception as e:
            print("deu merda " , e)
    print(len(games))

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
    def __init__(self,driver,liga,casa,fora):
        self.driver = driver
        self.liga = liga
        self.casa = casa
        self.fora = fora

        self.homeAway = []
        self.result = []
        self.leading = []
        self.goalScorred = []
        self.stts = []

    def requisito_Home_Away_Table(self, casa, fora, driver):
        # definições iniciais
        resultado = []
        valores = []
        times = ["Casa", "Visitante"]
        colunas = ["nome", "GP", "Pts"]

        # coletando os dados do time casa
        casa_content = driver.find_element(By.XPATH,
                                           '//div[2]/table[1]/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[@class="trow7"]').text
        casa_content = casa_content.split()
        resultado.append([casa,casa_content[-2],casa_content[-1]])


if __name__ == '__main__':
    liga = "England - Premier League"
    caminho(liga)
