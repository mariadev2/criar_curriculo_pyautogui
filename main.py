
import pyautogui as pg
import time as tm
import pyperclip
resposta = str(input("Deseja iniciar um curriculo? (  )sim (  )nao\n"))
if resposta== "sim":
    print("vamos lá!")
    pg.hotkey('win')
    tm.sleep(3)
    pg.write('word')
    pg.press('enter')
else:
    print("encerrando...")