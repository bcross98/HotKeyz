#Imports
#This tells Python what Libraries you want to use.
#Think of Libraries like tool kits.
#Pyautogui lets you control mouse clicks/keyboard clicks
#Keyboard lets you control keyboard clicks and it can listen for a specific key to be clicked
#Threading lets you have multiple processes running at the same time. Normally you only get defaulted 1, this lets you run two things at the same time.
#Time has a function called sleep, this is essentially a pause function.
#OS lets you control things about the Operating System. In this case we're using it to exit the program with os._exit(1)
import pyautogui
import keyboard
from threading import Thread
import time
import os

#Functions
#These are like making drawers for your tools to go in. They help keep things nice and tidy plus you can test things easier.
#Def is the keyword to let the computer know you're using a function. Don't ask me why it's like this.
#
#os.system('cls||clear') clears the command prompt window of any text. I use this to keep it looking pretty.
#
#print is pretty obvious. It displays text in the command prompt window.
#
#time.sleep(10) is a timeout function. This tells the program to wait before doing anything else.
#
#pyautogui.mouseDown() tells the program to press down the left mouse button (left is default, you'll have to specify if you want a different result)
#
#While True: is a loop that you can use in Python. It will run the code inside of it (everything indented) as long as it stays True. Break is the keyword to get out of it, usually you set up and if statement to look for a way to stop the loop or else it runs forever. You can also add elif to your if statement, this just means "else if" think of it as a second way to stop or check for something.
#
#EX.
#While JerettIsGay:
#   He sucks dick
#
#   if JerettIsGay == False:
#       break
#   elif JerettIsBi == True:
#       break
#
#input is used to get something from the user. In this program, it asks how many iron picks you have and stores it in a value called 'picks'. You can name values almost anything you want, as long as it doesn't exist in a library you're using. You'll know if a library is using that word because it's blue.
#
#When you get something from the user, it's stored in a 'string' which is a fancy way of saying the computer is reading it like a word. Sometimes you have to change it from a word to a number (integer). To do that you'll use something like int(picks) to turn it into a number or str(picks) to turn it into a "word".
#
#keyboard.is_pressed('e') is really simple to understand. It's essentially paying attention to if the user presses the 'e' key
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
    print("Loading XP Farm afk...\nMake sure you're in your Minecraft window.")
    time.sleep(10)
    os.system('cls||clear')
    print('Press e to exit.')
    while True:
        pyautogui.click()
        time.sleep(0.5)

#These functions set up a second thread listening for the escape key
#todo: make it smaller
#
#Don't worry about any of these. I just recently learned this, I don't know if I can properly explain it in a way that'll make sense.
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

#Start Program
#
#I'm calling the ComplexCobblestoneListener, this will run that program that also runs the ComplexCobblestoneGenerator function.
#This is the only function I'm calling, this is the one that needs the most testing and work.
#Later I'm going to connect the ui to this script and the UI will start the program.
ComplexCobblestoneListener()
