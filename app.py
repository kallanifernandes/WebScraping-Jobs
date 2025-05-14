from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

key_word = "Programador" #armazena a palavra-chave da vaga(função)
localization = "Santos" #localização da vaga 
url = "https://www.infojobs.com.br/" #armazena a url do site selecionado

navegador = webdriver.Chrome() #driver do navegador
navegador.get(url) #navegador pega a url selecionada

#antes de iniciar qualquer bloco de codigo, espera 5 segundo para carregamento total do site
time.sleep(5)

#armazena o ID do input de pesquisa, passando como parametro 'Programador' -> key_word
search = navegador.find_element(By.ID, "keywordsCombo")
search.send_keys(key_word) #envia info
#armazena cidade selecionada
city = navegador.find_element(By.ID, "city")
city.clear() #limpa o campo antes de passar o parametro
city.send_keys(localization) #envia info
city.send_keys(u'\ue007') #pressiona ENTER

#poderia colocar CSS_NAME, pois é uma classe css o nome completo
vagas = navegador.find_elements(By.CLASS_NAME, "card.card-shadow.card-shadow-hover.text-break.mb-16.grid-row.js_rowCard")

lista = [] #lista vazia onde sera feito o direcionamento do titulo, empresa e link
#laço onde vai atribuindo e verificando cada index das variaveis e adicionando na lista 
for vaga in vagas:
  try:
    tittle  = vaga.find_element(By.CLASS_NAME, "h3.font-weight-bold.text-body.mb-8").text
  except:
    tittle = "N/A"
  
  try:
    company = vaga.find_element(By.CLASS_NAME, "text-body text-decoration-none").text
  except:
    company = "N/A"
  
  try: 
    link = vaga.find_element(By.TAG_NAME, "a").get_attribute("href")
  except:
    link = "N/A"
  #append add no final 
  lista.append({
    "Titulo da vaga" : tittle,
    "Empresa"        : company,
    "Link da vaga"   : link
  })
#quita do servidor 
navegador.quit()
#cria um DATAFRAME passando como parametro a nossa lista, transforma em CSV
df = pd.DataFrame(lista)
df.to_csv("vagas_abertas.csv", index=False, encoding="utf-8")
print("Arquivo salvo com sucesso!")

