import pyautogui
import time

# Aguarda alguns segundos para você posicionar o cursor onde deseja clicar
time.sleep(5)

# Localiza o botão na tela e obtém suas coordenadas
coord_x, coord_y = pyautogui.locateCenterOnScreen('botao.png')

# Move o cursor para as coordenadas do botão e clica
pyautogui.moveTo(coord_x, coord_y)
pyautogui.click()

