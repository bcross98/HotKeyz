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

#MAIN
#
#
#
#W key Function
wKey = True
def wKeyFunction():
    global wKey
    time.sleep(6)
    while wKey:
        pyautogui.keyDown('w')
        time.sleep(0.5)

#Right click and hold function
rHold = True
def rHoldFunction():
    global rHold
    time.sleep(6)
    while rHold:
        pyautogui.mouseDown(button='right')

#Right click function
rClick = True
def rClickFunction():
    global rClick
    time.sleep(6)
    while rClick:
        pyautogui.rightClick()
        time.sleep(0.5)

#Left click and hold function
lHold = True
def lHoldFunction():
    global lHold
    time.sleep(6)
    while lHold:
        pyautogui.mouseDown(button='left')

#Left click function
lClick = True
def lClickFunction():
    global lClick
    time.sleep(6)
    while lClick:
        pyautogui.leftClick()
        time.sleep(0.5)

#Timer function
timer = True
def TimerText():
    global timer
    i = 5
    while timer:
        loadingCount.config(text=i)
        time.sleep(1)
        i -= 1
        if i < 0:
            labelEmpty()
            break

#Threads to quit action
#TODO: refactor this jumble of mess
def wKeyListener():
    global wKey
    t = Thread(target=wKeyFunction)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            pyautogui.keyUp('w')
            labelFull()
            toSelectionFrame()
            wKey = False
            t.join()
            break

def rHoldListener():
    global rHold
    t = Thread(target=rHoldFunction)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            labelFull()
            toSelectionFrame()
            rHold = False
            t.join()
            break

def rClickListener():
    global rClick
    t = Thread(target=lClickFunction)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            labelFull()
            toSelectionFrame()
            rClick = False
            t.join()
            break

def lHoldListener():
    global lHold
    t = Thread(target=lHoldFunction)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            labelFull()
            toSelectionFrame()
            lHold = False
            t.join()
            break

def lClickListener():
    global lClick
    t = Thread(target=lClickFunction)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            labelFull()
            toSelectionFrame()
            lClick = False
            t.join()
            break

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

#Connector threads to run tkinter at the same time as the listener and function
#TODO: refactor this mess also
def wKeyConnector():
    global wKey
    wKey = True
    s = Thread(target=wKeyListener)
    s.daemon = True
    s.start()

def rHoldConnector():
    global rHold
    rHold = True
    s = Thread(target=rHoldListener)
    s.daemon = True
    s.start()

def rClickConnector():
    global rClick
    rClick = True
    s = Thread(target=rClickListener)
    s.daemon = True
    s.start()

def lHoldConnector():
    global lHold
    lHold = True
    s = Thread(target=lHoldListener)
    s.daemon = True
    s.start()

def lClickConnector():
    global lClick
    lClick = True
    s = Thread(target=lClickListener)
    s.daemon = True
    s.start()

def timerConnector():
    global timer
    timer = True
    s = Thread(target=timerListener)
    s.daemon = True
    s.start()

#Assorted Tkinter functions
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
wKeyLabel = Button(keyboardFrame, text='w key', command=lambda:[toLoadingFrame(), wKeyConnector(), timerConnector()])
wKeyLabel.grid(row=2, column=1)
#Keyboard back
keyboardBack = Button(keyboardFrame, text='Back', command=toSelectionFrame)
keyboardBack.grid(row=1, column=2)

#Mouse Frame
#Right Hold
rHoldLabel = Button(mouseFrame, text='R hold', command=lambda:[toLoadingFrame(), rHoldConnector(), timerConnector()])
rHoldLabel.grid(row=2, column=3, padx=5, pady=5)
#Right Click
rClickLabel = Button(mouseFrame, text='R click', command=lambda:[toLoadingFrame(), rClickConnector(), timerConnector()])
rClickLabel.grid(row=3, column=3, padx=5, pady=5)
#Left Hold
lHoldLabel = Button(mouseFrame, text='L hold', command=lambda:[toLoadingFrame(), lHoldConnector(), timerConnector()])
lHoldLabel.grid(row=2, column=1, padx=5, pady=5)
#Left Click
lClickLabel = Button(mouseFrame, text='L click', command=lambda:[toLoadingFrame(), lClickConnector(), timerConnector()])
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