from direct_keys import PressKey, ReleaseKey
from dict_keys import dict as keyCode
import time
import random
from apis import gerarNumAleatorio

def raikyuu():
    PressKey(keyCode['IGUAL'])

    PressKey(keyCode['Q'])
    time.sleep(0.08)
    ReleaseKey(keyCode['Q'])
    PressKey(keyCode['SHIFT'])
    time.sleep(0.08)
    ReleaseKey(keyCode['SHIFT'])
    PressKey(keyCode['E'])
    time.sleep(0.08)
    ReleaseKey(keyCode['E'])

    ReleaseKey(keyCode['IGUAL'])

    time.sleep(gerarNumAleatorio() + 0.05)

def arashi():
    PressKey(keyCode['IGUAL'])

    PressKey(keyCode['E'])
    time.sleep(0.08)
    ReleaseKey(keyCode['E'])
    PressKey(keyCode['SHIFT'])
    time.sleep(0.08)
    ReleaseKey(keyCode['SHIFT'])
    PressKey(keyCode['E'])
    time.sleep(0.08)
    ReleaseKey(keyCode['E'])
    ReleaseKey(keyCode['IGUAL'])

    time.sleep(gerarNumAleatorio() + 0.05)

def clone():
    PressKey(keyCode['IGUAL'])

    PressKey(keyCode['SHIFT'])
    time.sleep(0.08)
    ReleaseKey(keyCode['SHIFT'])
    PressKey(keyCode['C'])
    time.sleep(0.08)
    ReleaseKey(keyCode['C'])
    ReleaseKey(keyCode['IGUAL'])

    time.sleep(gerarNumAleatorio() + 0.05)