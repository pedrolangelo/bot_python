from direct_keys import PressKey, ReleaseKey
from dict_keys import dict as keyCode
from PIL import Image, ImageEnhance
import pytesseract
import pyautogui
import time
import re
import random
from jutsus import *

def gerarNumAleatorio():
    numero_aleatorio = random.uniform(0.03, 0.07)
    return numero_aleatorio

def digitarSenha(senha_separada):
    PressKey(keyCode[senha_separada[1]])
    time.sleep(0.1)
    ReleaseKey(keyCode[senha_separada[1]])

    time.sleep(gerarNumAleatorio())

    PressKey(keyCode[senha_separada[2]])
    time.sleep(0.1)
    ReleaseKey(keyCode[senha_separada[2]])

    time.sleep(gerarNumAleatorio())

    PressKey(keyCode[senha_separada[3]])
    time.sleep(0.1)
    ReleaseKey(keyCode[senha_separada[3]])

    time.sleep(gerarNumAleatorio())

def pegar_peixe(pesquei):
    time.sleep(gerarNumAleatorio() + 0.05)
    for i in range(18):
        PressKey(keyCode['N'])
        time.sleep(0.08)
        ReleaseKey(keyCode['N'])
        time.sleep(gerarNumAleatorio())

    time.sleep(random.uniform(0.5, 2.5))

def checar(checagem):
    time.sleep(gerarNumAleatorio() + 0.5)
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
    print("--------------SENHA--------------")
    print(senha)
    if len(senha) == 1:
        senha = senha[0]
        senha_separada = {}
        for i, numero in enumerate(senha, start=1):
            senha_separada[i] = numero

        if len(senha_separada) == 3:
            digitarSenha(senha_separada)
        else:
            print('--- Achei mais de uma senha, bugou ---')
            PressKey(keyCode['ENTER'])
            time.sleep(0.1)
            ReleaseKey(keyCode['ENTER'])
            time.sleep(gerarNumAleatorio() + 0.5)
            return
    
        time.sleep(random.uniform(0.5, 2.5))
        print('---- ENTER ----')

        PressKey(keyCode['ENTER'])
        time.sleep(0.1)
        ReleaseKey(keyCode['ENTER'])
        time.sleep(1)

        checagem = pyautogui.locateOnScreen('imagens/checagem.png', grayscale=True, confidence=0.4)
        if checagem is None:
            PressKey(keyCode['H'])
            time.sleep(0.1)
            ReleaseKey(keyCode['H'])
    else:
        print('---- Nao achei nada na imagem ----')
        PressKey(keyCode['ENTER'])
        time.sleep(0.1)
        ReleaseKey(keyCode['ENTER'])
        time.sleep(gerarNumAleatorio())
        time.sleep(1)

def jutsuPolicial():
    PressKey(keyCode['H'])
    time.sleep(0.1)
    ReleaseKey(keyCode['H'])

def raiton():
    raikyuu()
    arashi()