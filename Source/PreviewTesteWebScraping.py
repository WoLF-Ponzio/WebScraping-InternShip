import csv
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
import mysql.connector

#Reconeção com o banco de dados
conexao = mysql.connector.connect(host='localhost', database= 'Raspagem',user='root', password='root')
cursor = conexao.cursor()

#Raspagem Oficial
#Setup para a raspagem
url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=&location=Brasil&locationId=&geoId=106057199&f_TPR=&f_E=5&start=0'
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary, executable_path="C:\\geckodriver.exe",)

#Raspagem
vagas = []
#A plataforma permite a visualização de 1000 páginas de vagas, depois da 1000 ele apresenta erro 404
for page in range (0, 351, 25):
    url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=&location=Brasil&locationId=&geoId=106057199&f_TPR=&f_E=5&start='+ str(page)
    driver.get(url)
    time.sleep(4)
    
    #Cada Página apresenta 25 vagas
    for i in range(1, 26):
        try:
            #Obtendo os dados da vaga
            time.sleep(2)
            NomeVaga = driver.find_element(By.XPATH, '/html/body/li[' + str(i) + ']/div/div[2]/h3').text
            Empresa = driver.find_element(By.XPATH, '/html/body/li[' + str(i) + ']/div/div[2]/h4/a').text
            Local = driver.find_element(By.XPATH, '/html/body/li['  + str(i) + ']/div/div[2]/div/span').text 
            Data = driver.find_element(By.XPATH, '/html/body/li['   + str(i) + ']/div/div[2]/div/time').get_attribute('datetime')

            #Acessa o Descritivo da Vaga e obtem a descrição dela
            driver.find_element(By.XPATH, '/html/body/li['+ str(i) + ']/div/a/span').click() 
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/button[1]').click()
            Desc = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/div').text
            driver.back()
            time.sleep(2)
            
            #Verifica se a vaga já está cadastrada
            testador = False
            cursor.execute('SELECT * FROM Vagas WHERE Vaga = %s AND Empresa = %s AND Local = %s AND Data = %s AND descricao = %s', (NomeVaga, Empresa, Local, Data, Desc))
            result = cursor.fetchone()
            if result:
                print(f"A vaga {NomeVaga} já está cadastrada.")
                testador = True

            #Valida e caso não esteja, registra a vaga no banco
            if testador == False:
                vagas.append({'Vaga' : NomeVaga, 'Empresa' : Empresa, 'Local' : Local, 'Data' : Data, 'Desc' : Desc})       
                cursor.execute('INSERT INTO Vagas (Vaga, Empresa, Local, Data, descricao, TipoVaga) VALUES (%s, %s, %s, %s, %s, 4)', (NomeVaga, Empresa, Local, Data, Desc))  
                conexao.commit()
            
        #Tratamento de erros
        #Caso ocorra algum erro de carregamento ou redirecionamento da página, ele recomeça a raspagem da vaga atual
        except Exception as e:
            print(f"Erro ao obter dados da vaga {i}. Tentando novamente...")
            print('erro: ', e)
            i -= 1
            driver.get(url)
            time.sleep(2)
            continue
