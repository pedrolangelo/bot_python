from direct_keys import PressKey, ReleaseKey
from dict_keys import dict as keyCode
import time
import random
import pyautogui


def gerarNumAleatorio():
    numero_aleatorio = random.uniform(0.03, 0.07)
    return numero_aleatorio

def raikyuu():
    print('raikyuu')
    pyautogui.mouseDown(button="right")

    time.sleep(0.08)
    PressKey(keyCode['Q'])
    time.sleep(0.08)
    ReleaseKey(keyCode['Q'])
    time.sleep(0.08)
    PressKey(keyCode['SHIFT'])
    time.sleep(0.08)
    ReleaseKey(keyCode['SHIFT'])
    time.sleep(0.08)
    PressKey(keyCode['E'])
    time.sleep(0.08)
    ReleaseKey(keyCode['E'])
    time.sleep(5)
    pyautogui.mouseDown(button="right")

    time.sleep(gerarNumAleatorio() + 0.05)

def arashi():
    print('arashi')

    pyautogui.mouseDown(button="right")

    PressKey(keyCode['E'])
    time.sleep(0.08)
    ReleaseKey(keyCode['E'])
    PressKey(keyCode['SHIFT'])
    time.sleep(0.08)
    ReleaseKey(keyCode['SHIFT'])
    PressKey(keyCode['E'])
    time.sleep(0.08)
    ReleaseKey(keyCode['E'])

    pyautogui.mouseUp(button="right")

    time.sleep(gerarNumAleatorio() + 0.05)

def nagashi():
    print('nagashi')

    pyautogui.mouseDown(button="right")

    PressKey(keyCode['Q'])
    time.sleep(0.08)
    ReleaseKey(keyCode['Q'])
    PressKey(keyCode['R'])
    time.sleep(0.08)
    ReleaseKey(keyCode['R'])
    PressKey(keyCode['Q'])
    time.sleep(0.08)
    ReleaseKey(keyCode['Q'])

    pyautogui.mouseUp(button="right")

    time.sleep(gerarNumAleatorio() + 0.05)

def iwakai():
    print('iwakai')

    pyautogui.mouseDown(button="right")

    PressKey(keyCode['Q'])
    time.sleep(0.08)
    ReleaseKey(keyCode['Q'])
    PressKey(keyCode['V'])
    time.sleep(0.08)
    ReleaseKey(keyCode['V'])
    PressKey(keyCode['Q'])
    time.sleep(0.08)
    ReleaseKey(keyCode['Q'])

    pyautogui.mouseUp(button="right")

    time.sleep(gerarNumAleatorio() + 0.05)

def dorojigoku():
    print('dorojigoku')

    pyautogui.mouseDown(button="right")

    PressKey(keyCode['Q'])
    time.sleep(0.08)
    ReleaseKey(keyCode['Q'])
    PressKey(keyCode['V'])
    time.sleep(0.08)
    ReleaseKey(keyCode['V'])
    PressKey(keyCode['Q'])
    time.sleep(0.08)
    ReleaseKey(keyCode['Q'])
    PressKey(keyCode['V'])
    time.sleep(0.08)
    ReleaseKey(keyCode['V'])

    pyautogui.mouseUp(button="right")

    time.sleep(gerarNumAleatorio() + 0.05)

def sharingan():
    for i in range(1, 2):
        print('SHARINGAN ' + str(i))
        pyautogui.mouseDown(button="right")
        PressKey(keyCode['SHIFT'])
        time.sleep(0.08)
        ReleaseKey(keyCode['SHIFT'])
        pyautogui.mouseUp(button="right")

        PressKey(keyCode['N'])
        time.sleep(0.08)
        ReleaseKey(keyCode['N'])
        # if i != 9:
        #     time.sleep(gerarNumAleatorio() + 15)

def clone():
    print('clone')

    pyautogui.mouseDown(button="right")

    PressKey(keyCode['SHIFT'])
    time.sleep(0.08)
    ReleaseKey(keyCode['SHIFT'])
    PressKey(keyCode['C'])
    time.sleep(0.08)
    ReleaseKey(keyCode['C'])

    pyautogui.mouseUp(button="right")
    time.sleep(gerarNumAleatorio() + 0.05)

def cachorro():
    time.sleep(gerarNumAleatorio() + 2)
    print('CACHORRO')
    pyautogui.mouseDown(button="right")
    PressKey(keyCode['Q'])
    time.sleep(0.08)
    ReleaseKey(keyCode['Q'])
    time.sleep(0.5)
    PressKey(keyCode['SHIFT'])
    time.sleep(0.08)
    ReleaseKey(keyCode['SHIFT'])
    pyautogui.mouseUp(button="right")