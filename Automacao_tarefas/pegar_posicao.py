import time  # Importa o módulo time, que fornece funções para manipulação de tempo.
import pyautogui  # Importa o módulo pyautogui, que permite controlar o mouse e o teclado.

time.sleep(5)  # Pausa a execução do programa por 5 segundos, dando tempo para o usuário posicionar o cursor.
print(pyautogui.position())  # Imprime a posição atual do cursor do mouse (coordenadas x, y) no console.

pyautogui.scroll(200)  # Rola a tela para cima (ou para baixo, dependendo do sistema) em 200 unidades.
