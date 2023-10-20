import pytesseract
from pesca import pescar
from jutsus import *
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

while True:
    pescar()
    # Se for so pra usar jutsu, comenta o pescar() e coloca os jutsus embaixo
    # time.sleep(5)
    # print('5s iniciais')
    # cachorro()
    # time.sleep(4)
    # sharingan()
