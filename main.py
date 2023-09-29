import pytesseract
from pesca import pescar

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

while True:
    pescar()
    # cachorro()
