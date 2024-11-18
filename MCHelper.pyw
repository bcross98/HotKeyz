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
#Simple Cobblestone Function
#Runs infinitely
def SimpleCobblestoneGenerator():
    time.sleep(11)
    pyautogui.mouseDown()
    time.sleep(188)


#Complex Cobblestone Function
#Breaks stone and switches picks, however many you have.
complex = True
def ComplexCobble():
    global complex
    while True:
        picks = complexEntry.get()
        if picks in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            toLoadingFrame()
            TimerConnector()
            time.sleep(11)

            i = 0
            while complex:
                pyautogui.press(str(i + 1))
                time.sleep(0.5)
                pyautogui.mouseDown()
                time.sleep(188)
                i = i + 1
                if i == int(picks):
                    pyautogui.mouseUp()
                    break

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
def SimpleCobblestoneListener():
    t = Thread(target=SimpleCobblestoneGenerator)
    t.daemon = True
    t.start()
    while True:
        if keyboard.is_pressed('e'):
            pyautogui.mouseUp()
            labelFull()
            toSelectionFrame()
            break

def ComplexCobblestoneListener():
    global cobble
    t = Thread(target=ComplexCobble)
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

def ComplexCobblestoneConnector():
    global cobble
    cobble = True
    s = Thread(target=ComplexCobblestoneListener)
    s.daemon = True
    s.start()

def SimpleCobblestoneConnector():
    s = Thread(target=SimpleCobblestoneListener)
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

#Selection Frame
#Text
selectionLabel = Label(selectionFrame, text="Pick your poison.\n\n")
selectionLabel.grid(row=1, column=2)
#Cobblestone Button
cobbleButton = Button(selectionFrame, text='Cobblestone', command=toCobbleFrame)
cobbleButton.grid(row=2, column=1)
#XP Farm Button
#todo: link to xp function
xpButton = Button(selectionFrame, text='XP Farm', command=lambda: [toLoadingFrame(), XpFarmConnector(), TimerConnector()])
xpButton.grid(row=2, column=2)
#Exit Button
selectionGold = Button(selectionFrame, text="Gold", command=lambda: [toLoadingFrame(), GoldFarmConnector(), TimerConnector()])
selectionGold.grid(row=2, column=3)

#Cobble Frame
#Text
cobbleLabel = Label(cobbleFrame, text="Pick your poison.\n\n")
cobbleLabel.grid(row=1, column=2)
#Simple Button
simpleCobble = Button(cobbleFrame, text="1 pick", command=lambda: [toLoadingFrame(), SimpleCobblestoneConnector(), TimerConnector()])
simpleCobble.grid(row=2, column=1)
#Complex Button
#TODO: fix ComplexCobble
#complexCobble = Button(cobbleFrame, text='Multiple picks', command=toComplexFrame)
#complexCobble.grid(row=2, column=2)
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