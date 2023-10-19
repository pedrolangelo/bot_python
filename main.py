import pytesseract
from pesca import pescar
from jutsus import *
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

while True:
    # pescar()
    print('5s iniciais')
    time.sleep(5)
    cachorro()
    time.sleep(4)
    sharingan()
