import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

servico = Service(GeckoDriverManager().install())

navegador = webdriver.Firefox(service=servico)

# abrir navegador
navegador.get("https://app.snowflake.com/dl50892/gaa90132/w2C74kWqoZEM#query")

# clicar para realizar login
time.sleep(20)
navegador.find_element('xpath','//*[@id="base-button-1022-btnInnerEl"]').click()

# preencher email e clicar em próximo
time.sleep(10)
navegador.find_element('xpath','//*[@id="identifierId"]').send_keys('vinicius.almeida@cobli.co')
time.sleep(5)
navegador.find_element('xpath','/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span').click()

# preencher senha e clicar em próximo
time.sleep(5)
navegador.find_element('xpath','/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys('viniciuss1')
time.sleep(5)
navegador.find_element('xpath','/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span').click()

# botão de baixar
time.sleep(30)
navegador.find_element("xpath", '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div/div[1]/main/div[2]/div/div[2]/div[1]/div/div/div/div[3]/div[3]/span').click()

# botão de download
time.sleep(5)
navegador.find_element("xpath",'/html/body/div[3]/div/div/div/div[1]/div/div/div/div').click()

