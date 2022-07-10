from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep
import getpass
import random

# Setup para usar webdriver 
s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)

# Pegando a página desejada
insta = 'https://www.instagram.com'
driver.get(insta)
sleep(3)

# Selecionando os campos para preencher
user_camp = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')

password_camp = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

# Selecionando o campo do botão do enter para clique
button_enter = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')

# Função do login
def login():

  print('| Sorteio do Instagram! ><\n\nCarregando Instagram\nPor favor aguarde...\n')

  user_values = input(str('Informe seu usúario: '))

  password_values = getpass.getpass('\n(Por segurança, não conseguimos ver a sua senha)\nInforme sua senha: ')

  user_camp.send_keys(user_values)
  sleep(1)

  password_camp.send_keys(password_values)
  sleep(1)

  button_enter.click()

  print("\nLogando, aguarde... \ / \ / \ / \ /\n")
  sleep(6)

# Tentando logar
try:
  login()
    
# Em caso de erro no login, apagará os campos já preenchidos e tentará novamente
except:
  print("Algo deu errado! Seu login deve estar incorreto, por favor, insira-o novamente.\n")

  user_camp.send_keys(Keys.CONTROL + "a")

  user_camp.send_keys(Keys.DELETE)
  sleep(1)

  password_camp.send_keys(Keys.CONTROL + "a")
  password_camp.send_keys(Keys.DELETE)
  sleep(1)

  user_camp.send_keys(Keys.ENTER)

  login()
  sleep(6)

# Depois do login realizado
try:

  # Pega a url do sorteio
  url = input(str('Login realizado com sucesso!\n\nInforme a url da publicação do sorteio:\n>>> '))
  driver.get(url)
  sleep(2)

  print('\nEstamos carregando o post, por favor aguarde.\n')
  sleep(5)

  # Pega e clica em todos os + para exibir todos os comentários
  btn_plus = driver.find_element(By.CLASS_NAME, '_abl-')

  # Enquanto o botão for visivel para o usuario, clique nele
  while btn_plus.is_displayed():
    btn_plus.click()
    sleep(4)
    btn_plus = driver.find_element(By.CLASS_NAME, '_abl-')

  # Quando nao for mais possivel clicar, o programa continuará normalmente
except Exception:
  pass
  sleep(3)

print('Terminamos de carregar todos os comentários!\nAgora vamos pegar todos os usuários e apagar os duplicados para o sorteio,\nPor favor, aguarde mais um pouco...\n')

# Pegando todos os comentarios
comments = driver.find_elements(By.CLASS_NAME, '_a9zr')

# Criando uma lista vazia para adicionar os nomes dos usuarios aqui depois do loop
list_users = []

# Fazendo o loop, pra pegar o nome dos usuarios
for comment in comments:
  username = comment.find_element(By.CLASS_NAME, '_a9zc').text

# Pegando usuarios únicos e adicionando na lista
  if username not in list_users:
    list_users.append(username)

# Sorteando um usuario
winner = random.choice(list_users)[1:]

print(f'Carregamos todos os comentários, tiramos os duplicados e sorteamos o vencedor.\n\nO vencedor do sorteio é {winner} !!!\n\nObrigado por utilizar nosso programa, volte sempre! ;)')

