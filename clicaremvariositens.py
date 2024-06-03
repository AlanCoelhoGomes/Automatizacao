import pyautogui
import time

# Aguarda alguns segundos para você posicionar o cursor onde deseja clicar
time.sleep(5)

# Lista de imagens a serem encontradas na tela
itens_para_clicar = ['item1.png', 'item2.png', 'item3.png']

# Loop para clicar em cada item encontrado na tela
for item in itens_para_clicar:
    coord_x, coord_y = pyautogui.locateCenterOnScreen(item)
    pyautogui.click(coord_x, coord_y)
