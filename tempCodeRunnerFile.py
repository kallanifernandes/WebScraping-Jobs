from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

key_word = "Analista de dados"
localization = "Santos"
url = "https://www.infojobs.com.br/"

navegador = webdriver.Chrome()
navegador.get(url)

time.sleep(5)

search = navegador.find_element(By.ID, "keywordsCombo")
search.send_keys(key_word)

city = navegador.find_element(By.ID, "city")
city.clear()
city.send_keys(localization)

enter = navegador.find_element(By.CLASS_NAME, "jsButton")
enter.click()

input("Pressione Enter para fechar...")
