import pyautogui

# Obtém a posição atual do cursor do mouse
posicao_x, posicao_y = pyautogui.position()

# Exibe a posição atual do cursor
print(f'A posição atual do cursor é: X={posicao_x}, Y={posicao_y}')
