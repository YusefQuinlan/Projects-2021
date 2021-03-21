# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:01:14 2021

@author: Yusef Quinlan
"""

#import and getting the data into a DataFrame
import pandas as pd
from tkinter import *
import os
import matplotlib.pyplot as plt

df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

#Putting the columns into a variable, can view it with Spyder IDE
cols = df.columns

"""
Commented out now, but used to make a countries directory and regions directory
and put the regions and countries sub-directories in those main directories.
Charts will be output as image files to these directories. import os not 
commented out just in case relevant later.
"""
"""
path = os.getcwd()
print(path)
os.makedirs(path + "/Countries/")
os.makedirs(path + "/Regions/")
pathCo = path + "/Countries/"
pathReg = path + "/Regions/"
for i in Grouped_locs:
    os.makedirs(pathReg + i)
for i in Countries:
    os.makedirs(pathCo + i)
"""

# Getting all the unique locations and checking them.
locs = df['location'].unique()
#print(locs)

Grouped_locs = ['Africa','Asia', 'European Union', 'International',
                'North America','Oceania','South America','World']
Countries = [i for i in locs if i not in Grouped_locs]
def regionWindow():
    Wind = Tk()
    Wind.title("Region Select")
    regF = Frame(Wind)
    scroller = Scrollbar(regF)
    Listb = Listbox(regF)
    scroller.pack(side=RIGHT, fill=Y)
    Listb.pack(side=LEFT, fill=Y)
    Listb.config(width=0)
    scroller['command'] = Listb.yview
    Listb['yscrollcommand'] = scroller.set
    Listb.insert(END,"KKccccccccccccccccccccK")
    regF.pack(side=TOP)
    regF2 = Frame(regF)
    Btn = Button(regF2, text="Play Audio")
    Btn.pack()
    regF2.pack(side=TOP)
    Wind.mainloop()


Window = Tk()
Window.title("COVID Area Selections")
lbText = """
            This program allows you the user to recieve charts that depict 
            various things in regards to the COVID-19 data sourced from
            https://covid.ourworldindata.org/data/owid-covid-data.csv .
            This data shows various things for various countries and regions
            such as the daily new cases for particular date ranges, total
            cases for particular date ranges, people vaccinated, total 
            vaccinations etc. Charts use these data point to help users gain
            an insight into the current situation with COVID-19.
            
            Below there are three buttons, the first will open a window that 
            will allow users to get COVID-19 data on various grouped regions 
            such as Asia or Africa. The second will open a window that will
            allow users to get COVID-19 data on various individual countries.
            The third allows users to get charts/analysis for all countries 
            and all regions simultaneously.
            When the second windows are opened users can make their choices 
            from a drop down list, that will take them to a new window that
            will give them options to make and save various charts to the
            different folders, except for the window made by the third button,
            this window will give options to produce different charts in all
            folders. 
         """    
MainLabel = Label(Window,text=lbText)
MainLabel.grid(row=0,column=0)
regText = "Click this button to open up the regions window!"
lab1 = Label(Window,text=" ")
lab1.grid(row=1,column=0)
RegionBtn = Button(Window,text=regText,command=regionWindow)
RegionBtn.grid(row=2,column=0)
lab2 = Label(Window,text=" ")
lab2.grid(row=3,column=0)
CountryText = "Click this button to open up the Countries Window!"
CountryBtn = Button(Window,text=CountryText)
CountryBtn.grid(row=4,column=0)
lab3 = Label(Window,text=" ")
lab3.grid(row=5,column=0)
AllText = "Click this button to open up the Countries Window!"
AllBtn = Button(Window,text=CountryText)
AllBtn.grid(row=6,column=0)
Window.mainloop()