import pyautogui
import pytesseract
from apis import pescar, checar

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

while True:
    pesquei     = pyautogui.locateOnScreen('imagens/pesquei.png', grayscale=True, confidence=0.4)
    checagem    = pyautogui.locateOnScreen('imagens/checagem.png', grayscale=True, confidence=0.4)

    if pesquei is not None:
        pescar(pesquei)
        
    elif checagem is not None:
        checar(checagem)
    else:
        continue