# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 16:02:16 2021

@author: Yusef Quinlan
"""

# API SOURCES : https://medium.com/@vicbergquist/18-fun-apis-for-your-next-project-8008841c7be9

#Imports
import requests
from tkinter import *

# Welcome text for the interface.
apf = """Welcome to the API Fun python file, below there will be buttons that
    allow you to open up some fun api functions in new windows.
    There will be further text informing you what they are for and the buttons
    will have descriptions to help aid you.
"""
"""
    Creates the window that allows users to interact with the maths API. Users
    can basically input a number into an Entry widget and click a button, the 
    button will return a fact associated with whatever number they entered. No
    error handling as this is just a short fun program.
"""
def mathWindow():
    mWind = Tk()
    mWind.title("Maths facts!")
    mWindText = """
                The input box below requires a number, that number must be
                in number form and not word form i.e. it should be 2 and not
                'two', otherwise the program will not work. Upon inputting the
                number, press the button below the input to recieve a math fact
                about that number.
    """
    mWindLabel = Label(mWind, text =mWindText).grid(row=0,column=0)
    mWindEnt = Entry(mWind)
    mWindEnt.grid(row=1,column=0)
    mWindLabel2 = Label(mWind, text="").grid(row=2,column=0)
    mwindLabel4 = Label(mWind, text="")
    mwindLabel4.grid(row=5,column=0)
    mWindBtn = Button(mWind, text="Recieve math fact!",command=lambda xx = (mWindEnt,mwindLabel4): mathClick(xx)).grid(row=3,column=0)
    mwindLabel3 = Label(mWind, text="").grid(row=4,column=0)
    mWind.mainloop()

#The click function that returns facts to the maths window for users.
def mathClick(x):
    #item = x.grid_slaves(row=1,column=0)
    val = x[0].get()
    text1 = requests.get("http://numbersapi.com/di".replace('di',str(val))).text
    x[1].config(text=text1)

"""
    Creates a window that allows users to generate random Chuck Norris jokes.
"""
def ChuckWindow():
    cWind = Tk()
    cWind.title("Chuck Norris Jokes!")
    cWindText = """
                Simply click the button below and a Chuck norris joke will
                appear below the button itself
    """
    cWindLabel = Label(cWind, text =cWindText).grid(row=0,column=0)
    cWindLabel2 = Label(cWind, text="").grid(row=1,column=0)
    cwindLabel4 = Label(cWind, text="")
    cwindLabel4.grid(row=4,column=0)
    cWindBtn = Button(cWind, text="Generate Chuck Norris Joke!",command=lambda xx = cwindLabel4: genJoke(xx)).grid(row=2,column=0)
    cwindLabel3 = Label(cWind, text="").grid(row=3,column=0)
    cWind.mainloop()
    
# generates a radnom Chuck Norris joke.
def genJoke(lbl):
    jokejs = requests.get('https://api.chucknorris.io/jokes/random')
    jsonfile = jokejs.json()
    lbl.config(text=jsonfile['value'])
    
"""
    Creates a window that allows users to enter a pokemons name and recieve an
    id number for that specific pokemon.
"""  
def pokeWindow():
    pWind = Tk()
    pWind.title("Maths facts!")
    pWindText = """
                The input box below requires the name of a pokemon and returns
                the id of the pokemon, must be a real pokemon name otherwise 
                the program won't work.
    """
    pWindLabel = Label(pWind, text =pWindText).grid(row=0,column=0)
    pWindEnt = Entry(pWind)
    pWindEnt.grid(row=1,column=0)
    pWindLabel2 = Label(pWind, text="").grid(row=2,column=0)
    pwindLabel4 = Label(pWind, text="")
    pwindLabel4.grid(row=5,column=0)
    pWindBtn = Button(pWind, text="Recieve Pokemon Id!",command=lambda xx = (pWindEnt,pwindLabel4): pokeClick(xx)).grid(row=3,column=0)
    pwindLabel3 = Label(pWind, text="").grid(row=4,column=0)
    pWind.mainloop()

# Generates an id based on the pokemon enter when button was clicked.
def pokeClick(x):
    #item = x.grid_slaves(row=1,column=0)
    val = x[0].get()
    req = requests.get("https://pokeapi.co/api/v2/pokemon/er".replace('er',str(val)))
    jsfile = req.json()
    text1 = str(jsfile['id']) + " is the id number of pokemon:  " + val 
    x[1].config(text=text1)    
"""
    Creation of the main Window that opens new windows via button-clicks to 
    allow users to have fun with the public API's this program uses. Basically
    several buttons open up new windows and these new windows contain the 
    functions to interact with an API of some kind, dependant upon what is
    selected.
"""    
Window = Tk()
Window.title('API Fun')
welcome = Label(Window, text=apf).grid(row=0,column=0)
fill1 = Label(Window, text="").grid(row=1,column=0)
fill2 = Label(Window, text="").grid(row=2,column=0)
MathText = """button below will take you to a maths window that gives you facts
              based on a number you select"""
Math = Label(Window, text=MathText).grid(row=3,column=0)
Mathbtn = Button(Window,text="Click for math window",command=mathWindow).grid(row=4,column=0)
chuckText = """Button below will take you to a Chuck norris window that can 
                produce random Chuck norris jokes for your entertainment!
                """
Chuck = Label(Window, text=chuckText).grid(row=5,column=0)
Chuckbtn = Button(Window,text="Click for Chuck Norris window",command=ChuckWindow).grid(row=6,column=0)
pokeText = """Button below will let you search for a pokemon and get the id
              of that pokemon after searching.
                """
Pokemon = Label(Window, text=pokeText).grid(row=8,column=0)
pokebtn = Button(Window,text="Click for Pokemon window",command=pokeWindow).grid(row=9,column=0)

Window.mainloop()