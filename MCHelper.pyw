#Checks if the host computer has the proper packages installed
#If not, it installs them
def PackageCheck():
    import os

    try:
        import keyboard
    except:
        os.system("pip install keyboard")
        import keyboard

    try:
        import pyautogui
    except:
        os.system("pip install pyautogui")
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
#Auto Walk Function
#Runs infinitely
walk = True
def AutoWalk():
    global walk
    time.sleep(11)
    while walk:
        pyautogui.keyDown('w')
        time.sleep(0.5)
    

#Simple Cobblestone Function
cobble = True
def cobblestoneGenerator():
    global cobble
    time.sleep(11)
    while cobble:
        pyautogui.mouseDown()

#XP farm function
#Attacks in a 0.5 sec interval
xp = True
def XPFarm():
    global xp
    time.sleep(11)
    while xp:
        pyautogui.click()
        time.sleep(0.5)

#Gold farm function
#Right clicks to heal the iron golem in a 0.5 sec interval
gold = True
def GoldFarm():
    global gold
    time.sleep(11)
    while gold:
        pyautogui.rightClick()
        time.sleep(0.5)

#Function to display a dynamic timer
timer = True
def TimerText():
    global timer
    i = 10
    while timer:
        loadingCount.config(text=i)
        time.sleep(1)
        i -= 1
        if i < 0:
            labelEmpty()
            break

#These functions set up a second thread listening for the e key
def AutoWalkListener():
    global walk
    t = Thread(target=AutoWalk)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            pyautogui.keyUp('w')
            labelFull()
            toSelectionFrame()
            walk = False
            t.join()
            break

def cobblestoneListener():
    global cobble
    t = Thread(target=cobblestoneGenerator)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            pyautogui.mouseUp()
            labelFull()
            toSelectionFrame()
            cobble = False
            t.join()
            break

def XpFarmListener():
    global xp
    t = Thread(target=XPFarm)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            labelFull()
            toSelectionFrame()
            xp = False
            t.join()
            break

def GoldFarmListener():
    global gold
    t = Thread(target=GoldFarm)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            labelFull()
            toSelectionFrame()
            gold = False
            t.join()
            break

def TimerListener():
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

def AutoWalkConnector():
    global walk
    walk = True
    s = Thread(target=AutoWalkListener)
    s.daemon = True
    s.start()

def TimerConnector():
    global timer
    timer = True
    s = Thread(target=TimerListener)
    s.daemon = True
    s.start()

def GoldFarmConnector():
    global gold
    gold = True
    s = Thread(target=GoldFarmListener)
    s.daemon = True
    s.start()

def XpFarmConnector():
    global xp
    xp = True
    s = Thread(target=XpFarmListener)
    s.daemon = True
    s.start()

def cobblestoneConnector():
    global cobble
    cobble = True
    s = Thread(target=cobblestoneListener)
    s.daemon = True
    s.start()


#Function to set tkinter labels
def labelFull():
    #Set loadingCount
    loadingLabel.config(text="Loading...")

    #Set warningLabel
    warningLabel.config(text="Make sure you're in your Minecraft window.")

    quitLabel.grid(row=4, column=2)

#Function to set tkinter labels to empty
def labelEmpty():
    #Set loadingCount to empty
    loadingCount.config(text="")

    #Set warningLabel to empty
    warningLabel.config(text="")

    #Set loadingLabel to empty
    loadingLabel.config(text='')

    quitLabel.grid(row=1, column=2)


#Change to Selection Frame
def toSelectionFrame():
    selectionFrame.grid(row=0, column=0, sticky="")
    loadingFrame.grid_forget()

#Change to Loading Frame.
def toLoadingFrame():
    loadingFrame.grid(row=0, column=0, sticky="")
    selectionFrame.grid_forget()



#GUI
#
#
#
from tkinter import *

#The window
window = Tk()
window.title('MC Helper')

#Always on top
window.wm_attributes('-topmost', 1)

#Frame
loadingFrame = Frame(window)
selectionFrame = Frame(window)
selectionFrame.grid()

#Selection Frame
#Text
selectionLabel = Label(selectionFrame, text="Pick your poison.\n\n")
selectionLabel.grid(row=1, column=2)
#Cobblestone Button
cobbleButton = Button(selectionFrame, text='Cobblestone', command=lambda: [toLoadingFrame(), cobblestoneConnector(), TimerConnector()])
cobbleButton.grid(row=2, column=1, padx=10)
#XP Farm Button
xpButton = Button(selectionFrame, text='XP Farm', command=lambda: [toLoadingFrame(), XpFarmConnector(), TimerConnector()])
xpButton.grid(row=2, column=2, padx=10)
#Auto Walk Button
walkButton = Button(selectionFrame, text='Auto Walk', command=lambda: [toLoadingFrame(), AutoWalkConnector(), TimerConnector()])
walkButton.grid(row=2, column=3, padx=10)
#Gold Button
selectionGold = Button(selectionFrame, text="Gold", command=lambda: [toLoadingFrame(), GoldFarmConnector(), TimerConnector()])
selectionGold.grid(row=2, column=4, padx=10)

#Loading Frame
#WarningText
loadingLabel = Label(loadingFrame, text="Loading...")
loadingLabel.grid(row=1, column=2)
#Countdown
loadingCount = Label(loadingFrame, text='')
loadingCount.grid(row=2, column=2)
#Minecraft window warning sign
warningLabel = Label(loadingFrame, text="Make sure you're in your Minecraft window.")
warningLabel.grid(row=3, column=2)
#Quit label
quitLabel = Label(loadingFrame, text="Press e to quit.")
quitLabel.grid(row=4, column=2)

#Start page
window.mainloop()
