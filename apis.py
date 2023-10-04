from direct_keys import PressKey, ReleaseKey
from dict_keys import dict as keyCode
from PIL import Image, ImageEnhance
import pytesseract
import pyautogui
import time
import re
import os
import random
import winsound

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

def pegar_peixe(pesquei):
    for i in range(17):
        time.sleep(gerarNumAleatorio())
        PressKey(keyCode['N'])
        time.sleep(0.08)
        ReleaseKey(keyCode['N'])
        time.sleep(gerarNumAleatorio())

    time.sleep(random.uniform(0.5, 2))

    PressKey(keyCode['H'])
    print("H")
    time.sleep(0.1)
    ReleaseKey(keyCode['H'])

def checar(checagem):
    screenshot = pyautogui.screenshot(region=(checagem.left, checagem.top, 400, 300))

    screenshot.save("print.png")
    image = Image.open('print.png')
    image = image.convert("L")  # Converte para escala de cinza
    image = image.point(lambda p: p > 80 and 255)  # Binarização
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)  # Aumenta o contraste (ajuste conforme necessário)
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(2.0)  # Aumenta a nitidez (ajuste conforme necessário)

    texto_extraido = pytesseract.image_to_string(image)

    padrao = r'\d+'  # Este padrão de regex corresponde a um ou mais dígitos

    senha = re.findall(padrao, texto_extraido)
    print("------------SENHA------------")
    print(senha)
    if len(senha) == 1:
        senha = senha[0]
        senha_separada = {}
        for i, numero in enumerate(senha, start=1):
            senha_separada[i] = numero

        if len(senha_separada) == 3:
            digitarSenha(senha_separada)
        else:
            PressKey(keyCode['ENTER'])
            time.sleep(0.1)
            ReleaseKey(keyCode['ENTER'])
            return
    
        time.sleep(1)
        PressKey(keyCode['ENTER'])
        time.sleep(0.1)
        ReleaseKey(keyCode['ENTER'])
        time.sleep(1)

        checagem = pyautogui.locateOnScreen('imagens/checagem.png', grayscale=True, confidence=0.4)
        if checagem is None:
            PressKey(keyCode['H'])
            time.sleep(0.1)
            ReleaseKey(keyCode['H'])
            print("H")
    else:
        time.sleep(1)
        PressKey(keyCode['ENTER'])
        time.sleep(0.1)
        ReleaseKey(keyCode['ENTER'])
        time.sleep(1)

def jutsuPolicial():
    PressKey(keyCode['H'])
    time.sleep(0.1)
    ReleaseKey(keyCode['H'])

def comer_beber():
    freq = 300
    duration = 500 # 0.5seg

    time.sleep(4)
    winsound.Beep(freq, duration)
    print("check")