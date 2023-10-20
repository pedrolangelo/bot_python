import pyautogui
from apis import *
from jutsus import *

def pescar():
    pesquei     = pyautogui.locateOnScreen('imagens/pesquei.png', grayscale=True, confidence=0.4)
    checagem    = pyautogui.locateOnScreen('imagens/checagem.png', grayscale=True, confidence=0.7)

    if pesquei is not None:
        pegar_peixe(pesquei)

        sharingan()
        time.sleep(random.uniform(0.5, 1))

        PressKey(keyCode['H'])
        time.sleep(0.1)
        ReleaseKey(keyCode['H'])
        
    elif checagem is not None:
        checar(checagem)
    else:
        return