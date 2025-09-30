import pyautogui
import time

nome = input('Digite seu nome e sobrenome: ')
email = input('Digite seu melhor e-mail: ')
num_ddd = input('Digite seu DDD: ')
num_celular = input('Digite seu número de telefone: ')

time.sleep(3)
pyautogui.press('win')                      #abrir opera
pyautogui.write('opera')

time.sleep(3)
pyautogui.press('enter')
time.sleep(3)                                                          #entrar no site
pyautogui.write('https://www.hashtagtreinamentos.com')
pyautogui.press('enter')


# clicar em "Matricule-se"
pyautogui.click(x=1389, y=140, clicks=2, duration=2)


time.sleep(3)                               #clicar em "Começar agora"
pyautogui.click(x=956, y=897, duration=2)


time.sleep(2)                               #clicar em "Fazer minha inscrição"
pyautogui.click(x=937, y=577, duration=1.5)

#preencher forms
time.sleep(1)
pyautogui.click(x=969, y=506, duration=2)
pyautogui.write(nome)
time.sleep(1)
pyautogui.click(x=896, y=543, duration=2)
pyautogui.write(email)
time.sleep(1)
pyautogui.click(x=852, y=584, duration=2)
pyautogui.write(num_ddd)
time.sleep(1)
pyautogui.click(x=1037, y=590, duration=2)
time.sleep(1)
pyautogui.write(num_celular)
time.sleep(0.7)
pyautogui.click(x=1001, y=622, duration=1.3)


