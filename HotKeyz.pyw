#Checks if the host computer has the proper packages installed
#If not, it installs them
def PackageCheck():
    import os

    try:
        import keyboard
    except:
        os.system('pip install keyboard')
        import keyboard
    
    try:
        import pyautogui
    except:
        os.system('pip install pyautogui')
        import pyautogui

PackageCheck()

#Imports
import pyautogui
import keyboard
from threading import Thread
import time
import os

#MAIN FUNCTIONS
#
#
#
connector = True

#W key Function
def wKeyFunction():
    global connector
    time.sleep(6)
    while connector:
        pyautogui.keyDown('w')
        time.sleep(0.5)

#Right click and hold function
def rHoldFunction():
    global connector
    time.sleep(6)
    while connector:
        pyautogui.mouseDown(button='right')

#Right click and hold function
def rClickFunction():
    global connector
    time.sleep(6)
    while connector:
        pyautogui.rightClick()
        time.sleep(0.5)

#Left click and hold function
def lHoldFunction():
    global connector
    time.sleep(6)
    while connector:
        pyautogui.mouseDown(button='left')

#Left click function
def lClickFunction():
    global connector
    time.sleep(6)
    while connector:
        pyautogui.leftClick()

#Reset all keys
#TODO: Properly reset the mouse down and hold functions
def resetKeys():
    pyautogui.keyUp('w')
    #Not 100% sure these actually work yet
    pyautogui.mouseUp(button='right')
    pyautogui.mouseUp(button='left')

#Timer function
def TimerText():
    global connector
    i = 5
    while connector:
        loadingCount.config(text=i)
        time.sleep(1)
        i -= 1
        if i < 0:
            labelEmpty()
            break

#Array of functions
mainFunctions = [wKeyFunction, rHoldFunction, rClickFunction, lHoldFunction, lClickFunction]

#THREADING FUNCTIONS
#
#
#
def listenerFunction(whatFunction):
    global connector
    t = Thread(target=mainFunctions[whatFunction])
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            resetKeys()
            labelFull()
            toSelectionFrame()
            connector = False
            t.join()
            break

def connectorFunction(whatFunction):
    global connector
    connector = True
    s = Thread(target=listenerFunction, args=(whatFunction,))
    s.daemon = True
    s.start()

#TODO: figure out how to better implement multiple threads at the same time
def timerListener():
    global timer
    t = Thread(target=TimerText)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            labelFull()
            toSelectionFrame()
            timer = False
            t.join()
            break

def timerConnector():
    global timer
    timer = True
    s = Thread(target=timerListener)
    s.daemon = True
    s.start()

#ASSORTED TKINTER FUNCTIONS
#
#
#
#Function to set tkinter labels
def labelFull():
    #Set loadingCount
    loadingLabel.config(text='Loading...')
    #Set warningLabel
    warningLabel.config(text="Make sure you're in your game window")
    
    quitLabel.grid(row=4, column=2)

#Function to set tkinter labels to empty
def labelEmpty():
    #Set loadingCount to empty
    loadingCount.config(text="")
    #Set warningLabel to empty
    warningLabel.config(text="")
    #Set loadingLabel to empty
    loadingLabel.config(text="")

    quitLabel.grid(row=1, column=2)

#Change to Selection Frame
def toSelectionFrame():
    selectionFrame.grid(row=0, column=0, sticky="")
    mouseFrame.grid_forget()
    keyboardFrame.grid_forget()
    loadingFrame.grid_forget()

#Change to Loading Frame
def toLoadingFrame():
    loadingFrame.grid(row=0, column=0, sticky="")
    mouseFrame.grid_forget()
    keyboardFrame.grid_forget()
    selectionFrame.grid_forget()

#Change to Mouse Frame
def toMouseFrame():
    mouseFrame.grid(row=0, column=0, sticky="")
    keyboardFrame.grid_forget()
    loadingFrame.grid_forget()
    selectionFrame.grid_forget()

#Change to Keyboard Frame
def toKeyboardFrame():
    keyboardFrame.grid(row=0, column=0, sticky="")
    mouseFrame.grid_forget()
    loadingFrame.grid_forget()
    selectionFrame.grid_forget()

#TKINTER GUI
#
#
#
from tkinter import *

#The window
window = Tk()
window.title('')

#Always on top
window.wm_attributes('-topmost', 1)

#Frame
loadingFrame = Frame(window)
mouseFrame = Frame(window)
keyboardFrame = Frame(window)
selectionFrame = Frame(window)
selectionFrame.grid()

#Selection Frame
#Text
selectionLabel = Label(selectionFrame, text="HotKeyz.")
selectionLabel.grid(row=1, column=2, pady=10)
#Mouse Button
mouseButton = Button(selectionFrame, text='Mouse keys', command=toMouseFrame)
mouseButton.grid(row=2, column=1, padx=5, pady=5)
#Keyboard Button
keyboardButton = Button(selectionFrame, text='Keyboard keys', command=toKeyboardFrame)
keyboardButton.grid(row=2, column=3, padx=5, pady=5)

#Keyboard Frame
#w key
wKeyLabel = Button(keyboardFrame, text='w key', command=lambda:[toLoadingFrame(), timerConnector(), connectorFunction(0)])
wKeyLabel.grid(row=2, column=1)
#Keyboard back
keyboardBack = Button(keyboardFrame, text='Back', command=toSelectionFrame)
keyboardBack.grid(row=1, column=2)

#Mouse Frame
#Right Hold
rHoldLabel = Button(mouseFrame, text='R hold', command=lambda:[toLoadingFrame(), timerConnector(), connectorFunction(1)])
rHoldLabel.grid(row=2, column=3, padx=5, pady=5)
#Right Click
rClickLabel = Button(mouseFrame, text='R click', command=lambda:[toLoadingFrame(), timerConnector(), connectorFunction(2)])
rClickLabel.grid(row=3, column=3, padx=5, pady=5)
#Left Hold
lHoldLabel = Button(mouseFrame, text='L hold', command=lambda:[toLoadingFrame(), timerConnector(), connectorFunction(3)])
lHoldLabel.grid(row=2, column=1, padx=5, pady=5)
#Left Click
lClickLabel = Button(mouseFrame, text='L click', command=lambda:[toLoadingFrame(), timerConnector(), connectorFunction(4)])
lClickLabel.grid(row=3, column=1, padx=5, pady=5)
#Back button
mouseBack = Button(mouseFrame, text='Back', command=toSelectionFrame)
mouseBack.grid(row=1, column=1, pady=10)

#Loading Frame
#Warning Text
loadingLabel = Label(loadingFrame, text='Loading...')
loadingLabel.grid(row=1, column=2)
#Countdown
loadingCount = Label(loadingFrame, text='')
loadingCount.grid(row=2, column=2)
#Game window warning sign
warningLabel = Label(loadingFrame, text="Make sure you're in your game window.")
warningLabel.grid(row=3, column=2)
#Quit label
quitLabel = Label(loadingFrame, text='Press e to quit.')
quitLabel.grid(row=4, column=2)

#Start window
toSelectionFrame()
window.mainloop()