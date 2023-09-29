from directKeys import PressKey, ReleaseKey, dict as keyCode
from PIL import Image, ImageEnhance
import pytesseract
import pyautogui
import time
import re
import os
import random

def gerarNumAleatorio():
    numero_aleatorio = random.uniform(0.03, 0.07)
    return numero_aleatorio

def digitarSenha(senha_separada):
    PressKey(keyCode[senha_separada[1]])
    time.sleep(0.1)
    ReleaseKey(keyCode[senha_separada[1]])

    PressKey(keyCode[senha_separada[2]])
    time.sleep(0.1)
    ReleaseKey(keyCode[senha_separada[2]])

    PressKey(keyCode[senha_separada[3]])
    time.sleep(0.1)
    ReleaseKey(keyCode[senha_separada[3]])

def pescar(pesquei):
    for i in range(20):
        PressKey(keyCode['N'])
        time.sleep(0.08)
        ReleaseKey(keyCode['N'])
        time.sleep(gerarNumAleatorio())

    time.sleep(random.uniform(0.5, 2))

    PressKey(keyCode['H'])
    time.sleep(0.1)
    ReleaseKey(keyCode['H'])

def checar(checagem):
    screenshot = pyautogui.screenshot(region=(checagem.left, checagem.top, 400, 300))

    screenshot.save("print.png")
    image = Image.open('print.png')
    image = image.convert("L")  # Converte para escala de cinza
    image = image.point(lambda p: p > 100 and 255)  # Binarização
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)  # Aumenta o contraste (ajuste conforme necessário)
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(2.0)  # Aumenta a nitidez (ajuste conforme necessário)

    texto_extraido = pytesseract.image_to_string(image)
    os.remove("print.png")

    padrao = r'\d+'  # Este padrão de regex corresponde a um ou mais dígitos

    senha = re.findall(padrao, texto_extraido)
    print("------------SENHA------------")
    print(senha)
    if senha:
        senha = senha[0]
        senha_separada = {}
        for i, numero in enumerate(senha, start=1):
            senha_separada[i] = numero

        digitarSenha(senha_separada)
    
        time.sleep(1)
        PressKey(keyCode['ENTER'])
        time.sleep(0.1)
        ReleaseKey(keyCode['ENTER'])
        time.sleep(1)
        PressKey(keyCode['H'])
        time.sleep(0.1)
        ReleaseKey(keyCode['H'])