#GUI
#
#
#
import tkinter as tk

def mainWindow():
    #Window
    window = tk.Tk()
    window.title('MC Helper')

    #Simple Cobblestone Button
    #todo: link to function
    simpleButton = tk.Button(window, text="Simple Cobble afk",)
    simpleButton.grid(row=1, column=0)

    #Complex Cobblestone Button
    #todo: link to function
    complexButton = tk.Button(window, text="Complex Cobble afk",)
    complexButton.grid(row=1, column=1)

    #XP Farm Button
    #todo: link to function
    xpFarmButton = tk.Button(window, text='XP Farm afk',)
    xpFarmButton.grid(row=1, column=2)

    #Exit Button
    simpleButton = tk.Button(window, text='Exit', command=window.destroy)
    simpleButton.grid(row=1, column=3)

    #Starts program
    window.mainloop()

#Start Program
mainWindow()