from direct_keys import PressKey, ReleaseKey
from dict_keys import dict as keyCode
import time
import random
import pyautogui

def gerarNumAleatorio():
    numero_aleatorio = random.uniform(120, 130)
    return numero_aleatorio

def cachorro():
    time.sleep(5)
    pyautogui.mouseDown(button='right')
    PressKey(keyCode['SHIFT'])
    time.sleep(0.08)
    ReleaseKey(keyCode['SHIFT'])
    PressKey(keyCode['Q'])
    time.sleep(0.08)
    ReleaseKey(keyCode['Q'])
    pyautogui.mouseDown(button='right')
    time.sleep(gerarNumAleatorio())