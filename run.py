import pyautogui
import keyboard
from threading import Thread
import time
import os

#Functions


#Simple Cobblestone Function
#Runs infinitely
#todo: Detect when a pick breaks and stop the script
def SimpleCobblestoneGenerator():
    os.system('cls||clear')
    print("Loading Simple Cobblestone afk...\nMake sure you're in your Minecraft window.")
    time.sleep(10)
    os.system('cls||clear')
    print('Press e to exit.')
    pyautogui.mouseDown()
    time.sleep(188)
    os.system('cls||clear')


#Complex Cobblestone Function
#Breaks stone and switches picks, however many you have.
#todo: Detect when a pick breaks, detect how many picks, detect what kind of picks, detect how long a pick will last
def ComplexCobblestoneGenerator():
    while True:
        picks = input('How many Iron Picks?\nPress e to exit.\n')
        os.system('cls||clear')
        if picks in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print("Loading Complex Cobblestone afk...\nMake sure you're in your Minecraft window.")
            time.sleep(10)
            os.system('cls||clear')
            print("Press e to exit.")

            i = 0
            while True:
                pyautogui.press(str(i + 1))
                time.sleep(0.5)
                pyautogui.mouseDown()
                time.sleep(188)
                i = i + 1
                if i == int(picks):
                    pyautogui.mouseUp()
                    os.system('cls||clear')
                    os._exit(1)

        elif picks in ('q', 'Q'):
            break

#XP farm function
#Attacks in a 0.5 sec interval
#todo: detect when the weapon breaks and stop the script
def XPFarm():
    print("Loading XP Farm afk...\nMake sure you're in your Minecraft window.")
    time.sleep(10)
    os.system('cls||clear')
    print('Press e to exit.')
    while True:
        pyautogui.click()
        time.sleep(0.5)

#These functions set up a second thread listening for the escape key
#todo: make it smaller
def SimpleCobblestoneListener():
    t = Thread(target=SimpleCobblestoneGenerator)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            pyautogui.mouseUp()
            os._exit(1)

def ComplexCobblestoneListener():
    t = Thread(target=ComplexCobblestoneGenerator)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            pyautogui.mouseUp()
            os._exit(1)

def XpFarmListener():
    t = Thread(target=XPFarm)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            os._exit(1)



#GUI
#todo: link the rest of the text to the gui
#
#
#
import tkinter as tk

#Window
window = tk.Tk()
window.title('MC Helper')

#Simple Cobblestone Button
#todo: link to function
simpleButton = tk.Button(window, text="Simple Cobble afk",command=SimpleCobblestoneListener)
simpleButton.grid(row=1, column=0)

#Complex Cobblestone Button
#todo: link to function
complexButton = tk.Button(window, text="Complex Cobble afk",command=ComplexCobblestoneListener)
complexButton.grid(row=1, column=1)

#XP Farm Button
#todo: link to function
xpFarmButton = tk.Button(window, text='XP Farm afk',command=XpFarmListener)
xpFarmButton.grid(row=1, column=2)

#Exit Button
simpleButton = tk.Button(window, text='Exit', command=window.destroy)
simpleButton.grid(row=2, column=1)

#Starts program
window.mainloop()