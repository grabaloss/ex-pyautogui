import pyautogui
import time

nome = input('Digite seu nome e sobrenome: ')
email = input('Digite seu melhor e-mail: ')
num_ddd = input('Digite seu DDD: ')
num_celular = input('Digite seu número de telefone: ')

pyautogui.PAUSE = 0.3
time.sleep(3)
pyautogui.press('win')                      #abrir opera
pyautogui.write('opera')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://www.hashtagtreinamentos.com')
pyautogui.press('enter')


# clicar em "Matricule-se"
pyautogui.click(x=1389, y=140, clicks=2, duration=2)

#clicar em "Começar agora"
pyautogui.click(x=956, y=897, duration=2)

#clicar em "Fazer minha inscrição"
pyautogui.click(x=937, y=577, duration=1.5)

#preencher forms
pyautogui.click(x=969, y=506, duration=2)
pyautogui.write(nome)
pyautogui.click(x=816, y=536, duration=2)
pyautogui.write(email)
pyautogui.click(x=852, y=584, duration=2)
pyautogui.write(num_ddd)
pyautogui.click(x=1037, y=590, duration=2)
pyautogui.write(num_celular)

# clicar em "GARANTIR MINHA
pyautogui.click(x=870, y=636, duration=1.3)


