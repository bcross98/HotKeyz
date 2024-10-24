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
#TODO: Detect when a pick breaks and stop the script
def SimpleCobblestoneGenerator():
    time.sleep(11)
    pyautogui.mouseDown()
    time.sleep(188)


#Complex Cobblestone Function
#Breaks stone and switches picks, however many you have.
#TODO: Detect when a pick breaks, detect how many picks, detect what kind of picks, calculate how long a pick will last
def ComplexCobblestoneGenerator():
    while True:
        picks = complexEntry.get()
        if picks in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            toLoadingFrame()
            timerThread()
            time.sleep(11)

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


#XP farm function
#Attacks in a 0.5 sec interval
#TODO: detect when the weapon breaks and stop the script
def XPFarm():
    time.sleep(11)
    while True:
        pyautogui.click()
        time.sleep(0.5)

#These functions set up a second thread listening for the e key
#TODO: make it more compact
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

#Function to display a dynamic timer
def timerText():
    i = 10
    while i >= 1:
        textTimer = i
        loadingCount.config(text=textTimer)
        time.sleep(1)
        i -= 1
    
    #Show 0
    loadingCount.config(text="0")
    time.sleep(1)

    #Set loadingCount to empty
    loadingCount.config(text="")

    #Set warningLabel to empty
    warningLabel.config(text="")

    #Set loadingLabel to empty
    loadingLabel.config(text='')

#Thread to run the timer at the same time as tkinter
def timerThread():
    timerThread = Thread(target=timerText)
    timerThread.daemon = True
    timerThread.start()



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
cobbleFrame = Frame(window)
loadingFrame = Frame(window)
complexFrame = Frame(window)
selectionFrame = Frame(window)
selectionFrame.grid()

#Change to Cobblestone Frame
def toCobbleFrame():
    cobbleFrame.grid(row=0, column=0, sticky="")
    selectionFrame.grid_forget()
    loadingFrame.grid_forget()
    complexFrame.grid_forget()

#Change to Selection Frame
def toSelectionFrame():
    selectionFrame.grid(row=0, column=0, sticky="")
    cobbleFrame.grid_forget()
    loadingFrame.grid_forget()
    complexFrame.grid_forget()

#Change to Loading Frame.
def toLoadingFrame():
    loadingFrame.grid(row=0, column=0, sticky="")
    cobbleFrame.grid_forget()
    selectionFrame.grid_forget()
    complexFrame.grid_forget()

#Change to Complex Frame.
def toComplexFrame():
    complexFrame.grid(row=0, column=0, sticky="")
    cobbleFrame.grid_forget()
    selectionFrame.grid_forget()
    loadingFrame.grid_forget()

#Selection Frame
#Text
selectionLabel = Label(selectionFrame, text="Pick your poison.\n\n")
selectionLabel.grid(row=1, column=2)
#Cobblestone Button
cobbleButton = Button(selectionFrame, text='Cobblestone', command=toCobbleFrame)
cobbleButton.grid(row=2, column=1)
#XP Farm Button
#todo: link to xp function
xpButton = Button(selectionFrame, text='XP Farm', command=lambda: [toLoadingFrame(), XpFarmConnector(), timerThread()])
xpButton.grid(row=2, column=2)
#Exit Button
selectionExit = Button(selectionFrame, text="Exit", command=window.destroy)
selectionExit.grid(row=2, column=3)

#Cobble Frame
#Text
cobbleLabel = Label(cobbleFrame, text="Pick your poison.\n\n")
cobbleLabel.grid(row=1, column=2)
#Simple Button
simpleCobble = Button(cobbleFrame, text="1 pick", command=lambda: [toLoadingFrame(), SimpleCobblestoneConnector(), timerThread()])
simpleCobble.grid(row=2, column=1)
#Complex Button
complexCobble = Button(cobbleFrame, text='Multiple picks', command=toComplexFrame)
complexCobble.grid(row=2, column=2)
#Back Button
cobbleExit = Button(cobbleFrame, text='Back', command=toSelectionFrame)
cobbleExit.grid(row=2, column=3)

#Complex Cobble Frame
#Text
complexLabel = Label(complexFrame, text='How many Iron Picks?\n\n')
complexLabel.grid(row=1, column=2)
#Entry
complexEntry = Entry(complexFrame)
complexEntry.grid(row=2, column=1)
#Enter Button
complexButton = Button(complexFrame, text="Enter", command=ComplexCobblestoneConnector)
complexButton.grid(row=2, column=2)
#Back Button
complexExit = Button(complexFrame, text='Back', command=toCobbleFrame)
complexExit.grid(row=2, column=3)

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