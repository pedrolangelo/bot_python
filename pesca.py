import pyautogui
from apis import *

def pescar():
    pesquei     = pyautogui.locateOnScreen('imagens/pesquei.png', grayscale=True, confidence=0.4)
    checagem    = pyautogui.locateOnScreen('imagens/checagem.png', grayscale=True, confidence=0.4)

    if pesquei is not None:
        pegar_peixe(pesquei)

        raiton()

        PressKey(keyCode['H'])
        time.sleep(0.1)
        ReleaseKey(keyCode['H'])
        
    elif checagem is not None:
        checar(checagem)
    else:
        return