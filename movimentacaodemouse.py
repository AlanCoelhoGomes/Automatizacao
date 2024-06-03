import pyautogui
import time

# Movimenta o cursor do mouse para uma nova posição
pyautogui.moveTo(100, 100, duration=1)

# Move o cursor para uma posição relativa à sua posição atual
pyautogui.move(100, 100, duration=1)

# Move o cursor para a posição (0, 0) da tela
pyautogui.moveTo(0, 0, duration=1)
