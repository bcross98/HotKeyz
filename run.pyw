#Imports
import pyautogui
import keyboard
from threading import Thread
import time
import os

#Functions
#
#
#
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
    time.sleep(10)
    while True:
        pyautogui.click()
        time.sleep(0.5)

#These functions set up a second thread listening for the escape key
#todo: make it more compact
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

def XpFarmConnector():
    s = Thread(target=XpFarmListener)
    s.daemon = True
    s.start()

def ComplexCobblestoneConnector():
    s = Thread(target=ComplexCobblestoneListener)
    s.daemon = True
    s.start()

def SimpleCobblestoneConnector():
    s = Thread(target=SimpleCobblestoneListener)
    s.daemon = True
    s.start()



#GUI
#
#
#
from tkinter import *

#The window
window = Tk()
window.title('MC Helper')
window.geometry('400x150')

#Frame
cobbleFrame = Frame(window)
loadingFrame = Frame(window)
complexFrame = Frame(window)
selectionFrame = Frame(window)
selectionFrame.pack()

#Change to Cobblestone Frame
def toCobbleFrame():
    cobbleFrame.pack(fill='both', expand=1)
    selectionFrame.pack_forget()
    loadingFrame.pack_forget()
    complexFrame.pack_forget()

#Change to Selection Frame
def toSelectionFrame():
    selectionFrame.pack(fill='both', expand=1)
    cobbleFrame.pack_forget()
    loadingFrame.pack_forget()
    complexFrame.pack_forget()

#Change to Loading Frame.
def toLoadingFrame():
    loadingFrame.pack(fill='both', expand=1)
    cobbleFrame.pack_forget()
    selectionFrame.pack_forget()
    complexFrame.pack_forget()

#Change to Complex Frame.
def toComplexFrame():
    complexFrame.pack(fill='both', expand=1)
    cobbleFrame.pack_forget()
    selectionFrame.pack_forget()
    loadingFrame.pack_forget()

#Selection Frame
#Text
selectionLabel = Label(selectionFrame, text="Pick your poison.\n\n")
selectionLabel.pack(side=TOP)
#Cobblestone Button
cobbleButton = Button(selectionFrame, text='Cobblestone', command=toCobbleFrame)
cobbleButton.pack(side=LEFT)
#XP Farm Button
#todo: link to xp function
xpButton = Button(selectionFrame, text='XP Farm', command=lambda: [toLoadingFrame(), XpFarmConnector()])
xpButton.pack(side=LEFT)

#Cobble Frame
#Text
cobbleLabel = Label(cobbleFrame, text="Pick your poison.\n\n")
cobbleLabel.pack(side=TOP)
#Simple Button
simpleCobble = Button(cobbleFrame, text="1 pick", command=lambda: [toLoadingFrame(), SimpleCobblestoneConnector()])
simpleCobble.pack(side=LEFT)
#Complex Button
complexCobble = Button(cobbleFrame, text='Multiple picks', command=toComplexFrame)
complexCobble.pack(side=LEFT)
#Back Button
cobbleExit = Button(cobbleFrame, text='Back', command=toSelectionFrame)
cobbleExit.pack(side=RIGHT)

#Complex Cobble Frame
#Text
#Entry
#Back Button
complexExit = Button(complexFrame, text='Back', command=toCobbleFrame)
complexExit.pack(side=RIGHT)

#Loading Frame
#Text
loadingLabel = Label(loadingFrame, text="Loading...\n\nMake sure you're in\nyour Minecraft window.\n\nPress e to quit.")
loadingLabel.pack()


#Start page
window.mainloop()