import pyautogui as pg
import time as tm
import pyperclip
pg.PAUSE = 2
resposta = str(input("Deseja iniciar um curriculo? (  )sim (  )nao\n"))
resposta= resposta.upper()
if resposta== "SIM":
    print("vamos lá!")
    nome= str(input("SEU NOME:"))
    pg.hotkey('win')
    tm.sleep(3)

    pg.write('explorador de arquivos')
    tm.sleep(2)
    pg.press('enter')
    tm.sleep(2)
    pg.click(x = 1669, y = 142)
    pg.write('curriculo modelo py')
    pg.press('enter')
    tm.sleep(2)
    pg.click(x=757, y=191, clicks=2)
    pg.click(x=786, y=436, clicks=4)
    #pg.press('delete')
    pg.write(nome)

else:
    print("encerrando...")