# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:28:39 2021

@author: Yusef Quinlan
"""
#imports
from time import sleep
from tkinter import *
import winsound
"""
 The order that the following functions is executed in is as follows:
     makeWindow(), onClick(), haveBreak(). What this program does is allow
     users to schedule breaks, an obnoxious noise plays when a user should
     take a break (that they scheduled), and asks the user if they'd like
     to schedule another, if so then the functions are executed again in
     the order previously stated, this continues until a user no longer
     wants any breaks.
"""


"""
    Plays the obnoxious noise and sends an alert letting the user know
    that its time for them to have a break. Asks user if they want to
    have another break and if so executes the makeWindow() function.
    Otherwise it closes the Window made and the code stops running.
"""
def haveBreak():
    winsound.PlaySound('breaktime.wav',winsound.SND_FILENAME)
    messagebox.showwarning("BREAKTIME!!!", "ITS TIME FOR YOU TO HAVE A BREAK, ONCE YOU'VE HAD A BREAK, PRESS THE OK BUTTON!")
    answer = messagebox.askyesno(title='Continue?',
                      message='Would you like to schedule another break?')
    if answer:
        Window.destroy()
        makeWindow()
    else:
        Window.destroy()
"""
    When the minutes option is entered and the button in makeWindow()'s Tkinter
    Window is clicked, this function is called. Function gets the input, if the
    input can be converted to an integer then the program sleeps for the 
    integer inputted in minutes. After sleeping the haveBreak() function is 
    called. Hides the Window made in makeWindow()
"""    
def onClick():
    inputted = inputwidget.get()
    print(inputted)
    try:
        inputted = int(inputted)
        Window.withdraw()
        sleep(inputted * 60)
        haveBreak()
    except Exception as e:
        messagebox.showinfo("Error","You have entered a word or a decimal number, please enter a whole number")
        
"""
    Creates and runs a Tkinter Window that allows users to enter the amount of
    minutes till they wish to have a break. Upon entering this information and
    clicking a button they are prompted to click, the onClick() function is 
    called.
"""
def makeWindow():
    global inputwidget
    global Window
    Window = Tk()
    Window.title('BreakScheduler')
    aLabel = Label(Window, text="Enter how many minutes till you have a break below")
    aLabel.grid(row=0, column=0)
    inputwidget = Entry(Window)
    inputwidget.grid(row=1,column=0)
    aButton = Button(Window, text="Click to confirm the amount of minutes!", command=onClick)
    aButton.grid(row=2, column=0)
    Window.mainloop()

#Start the loop.
makeWindow()