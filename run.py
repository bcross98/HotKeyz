import pyautogui
import keyboard
import time
import sys
import os

#Functions
def SimpleCobblestoneGenerator():
    os.system('cls||clear')
    print("Loading Simple Cobblestone afk...\nMake sure you're in your Minecraft window.")
    time.sleep(10)
    pyautogui.mouseDown()
    os.system('cls||clear')

def ComplexCobblestoneGenerator():
    while True:
        picks = input('How many Iron Picks?\n')
        os.system('cls||clear')
        if picks in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print("Loading Complex Cobblestone afk...\nMake sure you're in your minecraft window.")
            time.sleep(10)
            i = 0
            while i < int(picks):
                pyautogui.press(str(i + 1))
                time.sleep(0.5)
                pyautogui.mouseDown()
                time.sleep(188)
                i += 1
            break
        elif picks in ('q', 'Q'):
            break

def XPFarm():
    print("Loading XP Farm afk...\nMake sure you're in your Minecraft window.")
    time.sleep(10)
    os.system('cls||clear')
    print('Press and hold 1 to exit.')
    while True:
        pyautogui.click()
        time.sleep(0.5)
        if keyboard.is_pressed('1'):
            os.system('cls||clear')
            sys.exit()


#Main
while True:
    selection = input("Enter 1 for a simple Cobblestone afk.\nEnter 2 for complex Cobblestone afk.\nEnter 3 for XP.\nPress q to leave\n")

    if selection == '1':
        os.system('cls||clear')
        SimpleCobblestoneGenerator()
        break
    elif selection == '2':
        os.system('cls||clear')
        ComplexCobblestoneGenerator()
        break
    elif selection == '3':
        os.system('cls||clear')
        XPFarm()
        break
    elif selection in ('q', 'Q'):
        os.system('cls||clear')
        break