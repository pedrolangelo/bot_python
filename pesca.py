import pyautogui
from apis import pegar_peixe, checar, comer_beber

def pescar():
    pesquei     = pyautogui.locateOnScreen('imagens/pesquei1.png', grayscale=True, confidence=0.4)
    checagem    = pyautogui.locateOnScreen('imagens/checagem.png', grayscale=True, confidence=0.4)
    comida      = pyautogui.locateOnScreen('imagens/comida_vermelha.png', grayscale=True, confidence=0.4)
    agua        = pyautogui.locateOnScreen('imagens/agua_vermelha.png', grayscale=True, confidence=0.4)

    if pesquei is not None:
        pegar_peixe(pesquei)
        if comida is not None or agua is not None:
            for i in range(3):
                comer_beber()
        
    elif checagem is not None:
        checar(checagem)
    else:
        return
    