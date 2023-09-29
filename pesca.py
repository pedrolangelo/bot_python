import pyautogui
from apis import pegar_peixe, checar

def pescar():
    pesquei     = pyautogui.locateOnScreen('imagens/pesquei.png', grayscale=True, confidence=0.4)
    checagem    = pyautogui.locateOnScreen('imagens/checagem.png', grayscale=True, confidence=0.4)

    if pesquei is not None:
        pegar_peixe(pesquei)
        
    elif checagem is not None:
        checar(checagem)
    else:
        return