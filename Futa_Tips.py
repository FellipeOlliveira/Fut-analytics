from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup

def telaInvisivel():
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")

    return option
def path(url,driver):

    driver.get(url)
    try:
        # Fechando o Ad inicial
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[3]").click()
    except Exception as e:
        print("Ele n possui ads iniciais")

    # pegando o nome dos times
    nomeTimeCasa = driver.find_element(By.XPATH, '//td/font/a[1]').text
    nomeTimeFora = driver.find_element(By.XPATH, '//td/font/a[2]').text

    requisito_Home_Away = requisito_Home_Away_Table(nomeTimeCasa,nomeTimeFora,driver)

    #indo pra proxima pagina
    driver.find_element(By.XPATH,'//table[4]/tbody/tr[6]/td/span/a').click()

    # É UMA LISTA 0 = casa // 1 = fora
    requisitos_Stts = requisitos_Stts_Times(nomeTimeCasa,nomeTimeFora,driver)

    requisito_Results = requisito_Results_Table(nomeTimeCasa, nomeTimeFora, driver)

    #É UMA LISTA 0 = casa // 1 = fora
    requisito_Leading = requisito_Leading_Table(nomeTimeCasa, nomeTimeFora, driver)

    #É UMA LISTA 0 = casa // 1 = fora
    requisito_Goals = requisito_Goal_Scorred(nomeTimeCasa, nomeTimeFora, driver)

    driver.quit()

#Stts : Concluido
def requisito_Home_Away_Table(casa, fora , driver):
    #definições iniciais
    resultado = []
    times = ["Casa","Visitante"]
    colunas = ["nome","GP","Pts"]

    #coletando os dados do time casa
    casa_content = driver.find_element(By.XPATH,'//div[2]/table[1]/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[@class="trow7"]').text
    resultado.append(casa_content.split())
    resultado[0][0] = casa

    # coletando dados do time fora
    fora_content = driver.find_element(By.XPATH,'//div[2]/table[1]/tbody/tr/td[3]/table/tbody/tr[2]/td/table//tr[@class="trow5"]').text
    resultado.append(fora_content.split())
    resultado[1][0] = fora

    df_full = pd.DataFrame(resultado,columns=colunas)

    return df_full
#Stts:Concluido
def requisito_Results_Table(casa, fora, driver):
    resultado = []
    colunas = ['posição','nome','gp','pts']

    # coletando os dados do time casa
    results_casa = driver.find_element(By.XPATH,'//div[1]/table[13]/tbody/tr/td/table//tr[@class = "trow2"]').text
    resultado.append(results_casa.split())
    resultado[0][1] = casa

    # coletando os dados do time fora
    results_fora = driver.find_element(By.XPATH,'//div[2]/table[13]/tbody/tr/td/table//tr[@class = "trow2"]').text
    resultado.append(results_fora.split())
    resultado[1][1] = fora

    df_full = pd.DataFrame(resultado,columns=colunas)

    #print(df_full)
    return df_full

#Stts:Concluido
def requisito_Leading_Table(casa, fora, driver):
    resultado = []
    colunas = ['Lead stts(total)','por partida','por porcentagem',3,4]

    #coletando dados do time casa
    tabela_Casa_html_content = driver.find_element(By.XPATH,'//div[5]/div[1]/div[1]/div[1]/table[4]').get_attribute('outerHTML')
    soup_casa = BeautifulSoup(tabela_Casa_html_content,'html.parser')
    table_casa = soup_casa.find(name='table')

    df_full_casa = pd.read_html(str(table_casa))[0].head(4)
    df_full_casa.columns = colunas
    df_full_casa = df_full_casa.drop([0],axis=0)
    df_casa = df_full_casa.drop([3,4],axis=1)

    resultado.append(df_casa)
    #print(df_casa)

    #coletando dados do time fora
    tabela_fora_html_content = driver.find_element(By.XPATH,'//div[2]/div[1]/div[1]/table[4]').get_attribute('outerHTML')
    soup_fora = BeautifulSoup(tabela_fora_html_content, 'html.parser')
    table_fora = soup_fora.find(name='table')

    df_full_fora = pd.read_html(str(table_fora))[0].head(4)
    df_full_fora.columns = colunas
    df_full_fora = df_full_fora.drop([0], axis=0)
    df_fora = df_full_fora.drop([3, 4], axis=1)

    resultado.append(df_fora)
    #print(df_fora)

    return resultado

#Stts:Concluido
def requisito_Goal_Scorred(casa, fora, driver):
    colunas = ['GFs / GAs',casa,fora,3]
    resultado = []

    #coletando dados da tabela casa
    tabela_html_casa_content = driver.find_element(By.XPATH, '//div[5]/div[1]/table[17]').get_attribute('outerHTML')
    soup_casa = BeautifulSoup(tabela_html_casa_content, 'html.parser')
    table_casa = soup_casa.find(name='table')

    #Tratando a tabela casa
    df_full_casa = pd.read_html(str(table_casa))
    df_casa = df_full_casa[0].drop([0, 4, 5, 9, 10], axis=0)
    df_casa.columns = colunas
    df_casa = df_casa.drop([fora, 3], axis=1)
    resultado.append(df_casa)

    #coletando dados da tabela fora
    tabela_html_fora_content = driver.find_element(By.XPATH,'//div[5]/div[2]/table[17]').get_attribute('outerHTML')
    soup_fora = BeautifulSoup(tabela_html_fora_content, 'html.parser')
    table_fora = soup_fora.find(name='table')

    #Tratando a tabela fora
    df_full_fora = pd.read_html(str(table_fora))
    df_fora = df_full_fora[0].drop([0,4,5,9,10],axis=0)
    df_fora.columns = colunas
    df_fora = df_fora.drop([casa,3],axis=1)
    resultado.append(df_fora)

    return resultado

def requisitos_Stts_Times(casa, fora, driver):
    linha = ['Points per game','% Clean sheets','% Failed To Score','% Won To Nil','% Lost To Nil','Total goals per game','% over 1.5 goals','% over 3.5 goals']
    lista_casa = []
    lista_fora = []
    resultado = []

    #coletando dados time casa
    driver.find_element(By.XPATH,'//div[5]/div[1]/table[12]/tbody/tr[1]/td/div/label[2]').click()
    for i in linha:
        tupla_casa = driver.find_element(By.XPATH, f'//div[5]/div[1]/table[12]/tbody/tr[1]/td/div/div[2]/table[2]//table//td[contains(text(),"{i}")]/..').text
        tupla_casa = tupla_casa.split()
        lista_casa.append([tupla_casa[-2],tupla_casa[-1]])

    #tratando os dados do time casa
    df_full_casa = pd.DataFrame(lista_casa).transpose()
    df_full_casa.columns = linha
    resultado.append(df_full_casa)

    # coletando dados time fora
    driver.find_element(By.XPATH, '//div[5]/div[2]/table[12]/tbody/tr[1]/td/div/label[3]').click()
    for i in linha:
        tupla_fora = driver.find_element(By.XPATH,f'//div[5]/div[2]/table[12]/tbody/tr[1]/td/div/div[3]/table[2]//td[contains(text(),"{i}")]/..').text
        tupla_fora = tupla_fora.split()
        lista_fora.append([tupla_fora[-2], tupla_fora[-1]])

    # tratando os dados do time fora
    df_full_fora = pd.DataFrame(lista_fora).transpose()
    df_full_fora.columns = linha
    resultado.append(df_full_fora)

    return resultado

if __name__ == '__main__':
    path('https://www.soccerstats.com/pmatch.asp?league=italy&stats=282-19-14-2024')