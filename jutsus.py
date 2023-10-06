from direct_keys import PressKey, ReleaseKey
from dict_keys import dict as keyCode
import time
import random

def gerarNumAleatorio():
    numero_aleatorio = random.uniform(0.03, 0.07)
    return numero_aleatorio

def raikyuu():
    print('raikyuu')
    PressKey(keyCode['DEL'])
    PressKey(keyCode['Q'])
    time.sleep(0.08)
    ReleaseKey(keyCode['Q'])
    PressKey(keyCode['SHIFT'])
    time.sleep(0.08)
    ReleaseKey(keyCode['SHIFT'])
    PressKey(keyCode['E'])
    time.sleep(0.08)
    ReleaseKey(keyCode['E'])

    ReleaseKey(keyCode['DEL'])

    time.sleep(gerarNumAleatorio() + 0.05)

def arashi():
    print('arashi')

    PressKey(keyCode['DEL'])

    PressKey(keyCode['E'])
    time.sleep(0.08)
    ReleaseKey(keyCode['E'])
    PressKey(keyCode['SHIFT'])
    time.sleep(0.08)
    ReleaseKey(keyCode['SHIFT'])
    PressKey(keyCode['E'])
    time.sleep(0.08)
    ReleaseKey(keyCode['E'])
    ReleaseKey(keyCode['DEL'])

    time.sleep(gerarNumAleatorio() + 0.05)

def clone():
    print('clone')

    PressKey(keyCode['DEL'])

    PressKey(keyCode['SHIFT'])
    time.sleep(0.08)
    ReleaseKey(keyCode['SHIFT'])
    PressKey(keyCode['C'])
    time.sleep(0.08)
    ReleaseKey(keyCode['C'])
    ReleaseKey(keyCode['DEL'])
    time.sleep(gerarNumAleatorio() + 0.05)