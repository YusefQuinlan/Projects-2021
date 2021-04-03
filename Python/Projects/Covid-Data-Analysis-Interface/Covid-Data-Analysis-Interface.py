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
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import datetime

df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

#Putting the columns into a variable, can view it with Spyder IDE
cols = df.columns

"""
    This function takes a location and saves a chart of that locations
    total Covid cases over time, in that locations respective folder.
"""
def total_cases(location):
    df2 = df[['location','date','total_cases']]

    df3 = df2.loc[df2['location'] == location]

    datetimes = []
    for i in df3['date']:
        datetimes.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
    fig = plt.figure(figsize=(30,20))
    plt.plot_date(datetimes,df3['total_cases'])
    plt.xlabel("Dates")
    plt.ylabel("Total COVID cases")
    plt.title("Total COVID cases for location by date".replace("location",location))
    plt.gcf().autofmt_xdate() 
    plt.gca().xaxis_date()
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m, %Y'))
    if df3['total_cases'].max() > 900000:
        ylabels = [x for x in plt.gca().get_yticks() /150000 * 150000]
        plt.gca().set_yticklabels(ylabels)
    path = os.getcwd()
    if location in Countries:
        fig.savefig(path + "/Countries/location/location_total_cases.png".replace("location",location))
    elif location in Grouped_locs:
        fig.savefig(path + "/Regions/location/location_total_cases.png".replace("location",location))
    plt.close()

"""
    This function takes a location and saves a chart of that locations total
    COVID cases per million people, in that locations folder.
"""    
def cases_million(location):
    df2 = df[['location','date','total_cases_per_million']]

    df3 = df2.loc[df2['location'] == location]

    datetimes = []
    for i in df3['date']:
        datetimes.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
    fig = plt.figure(figsize=(30,20))
    plt.plot_date(datetimes,df3['total_cases_per_million'])
    plt.xlabel("Dates")
    plt.ylabel("Total COVID cases per million")
    plt.title("Total COVID cases per million for location by date".replace("location",location))
    plt.gcf().autofmt_xdate() 
    plt.gca().xaxis_date()
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m, %Y'))
    if df3['total_cases_per_million'].max() > 900000:
        ylabels = [x for x in plt.gca().get_yticks() /150000 * 150000]
        plt.gca().set_yticklabels(ylabels)
    path = os.getcwd()
    if location in Countries:
        fig.savefig(path + "/Countries/location/location_million_cases.png".replace("location",location))
    elif location in Grouped_locs:
        fig.savefig(path + "/Regions/location/location_million_cases.png".replace("location",location))
    plt.close()

"""
    This function takes a location and saves a chart of that locations positive
    COVID rate, in that locations folder.
"""       
def pos_rate(location):
    df2 = df[['location','date','positive_rate']]

    df3 = df2.loc[df2['location'] == location]

    datetimes = []
    for i in df3['date']:
        datetimes.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
    fig = plt.figure(figsize=(30,20))
    plt.plot_date(datetimes,df3['positive_rate'])
    plt.xlabel("Date")
    plt.ylabel("Positive rate of COVID")
    plt.title("Positive COVID rate for location by date".replace("location",location))
    plt.gcf().autofmt_xdate() 
    plt.gca().xaxis_date()
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m, %Y'))
    path = os.getcwd()
    if location in Countries:
        fig.savefig(path + "/Countries/location/location_positive_rate.png".replace("location",location))
    elif location in Grouped_locs:
        fig.savefig(path + "/Regions/location/location_positive_rate.png".replace("location",location))
    plt.close()

"""
    This function takes a location and saves a chart of that locations total
    COVID deaths, in that locations folder.
"""       
def total_deaths(location):
    df2 = df[['location','date','total_deaths']]

    df3 = df2.loc[df2['location'] == location]

    datetimes = []
    for i in df3['date']:
        datetimes.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
    fig = plt.figure(figsize=(30,20))
    plt.plot_date(datetimes,df3['total_deaths'])
    plt.xlabel("Date")
    plt.ylabel("Total deaths caused by COVID")
    plt.title("Total deaths caused by Covid for location by date".replace("location",location))
    plt.gcf().autofmt_xdate() 
    plt.gca().xaxis_date()
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m, %Y'))
    if df3['total_deaths'].max() > 900000:
        ylabels = [x for x in plt.gca().get_yticks() /150000 * 150000]
        plt.gca().set_yticklabels(ylabels)
    path = os.getcwd()
    if location in Countries:
        fig.savefig(path + "/Countries/location/location_total_deaths.png".replace("location",location))
    elif location in Grouped_locs:
        fig.savefig(path + "/Regions/location/location_total_deaths.png".replace("location",location))
    plt.close()

"""
    This function takes a location and saves a chart of that locations total
    COVID vaccinations per hundred people, in that locations folder.
"""   
def total_vacs(location):
    df2 = df[['location','date','total_vaccinations_per_hundred']]

    df3 = df2.loc[df2['location'] == location]

    datetimes = []
    for i in df3['date']:
        datetimes.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
    fig = plt.figure(figsize=(30,20))
    plt.plot_date(datetimes,df3['total_vaccinations_per_hundred'])
    plt.xlabel("Date")
    plt.ylabel("Total COVID Vaccinations per hundred people")
    plt.title("Total COVID Vaccinations per hundred people in location by date".replace("location",location))
    plt.gcf().autofmt_xdate() 
    plt.gca().xaxis_date()
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m, %Y'))
    path = os.getcwd()
    if location in Countries:
        fig.savefig(path + "/Countries/location/location_total_vaccinations.png".replace("location",location))
    elif location in Grouped_locs:
        fig.savefig(path + "/Regions/location/location_total_vaccinations.png".replace("location",location))
    plt.close()

"""
Commented out now, but used to make a countries directory and regions directory
and put the regions and countries sub-directories in those main directories.
Charts will be output as image files to these directories. import os not 
commented out just in case relevant later.
You'll need to uncomment the path stuff to make the folders needed for the file
storage database configuration, you'll then need to comment it out again so
that the folders don't get replaced by empty folders.
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

# List of all the Regions
Grouped_locs = ['Africa','Asia', 'European Union', 'International',
                'North America','Oceania','South America','World']

#List of all the Countries
Countries = [i for i in locs if i not in Grouped_locs]

"""
    The following function opens the region window i.e. a window that contains
    a listbox full of regions and a button to open a region. It also contains
    the function to open a regions window. And a regions window allows a user 
    to create various charts for a region and save them to that specific 
    regions folder.
"""
def regionWindow():
    def openRegion():
        Region = Listb.get(Listb.curselection())
        wind = Tk()
        wind.title(Region)
        tx1 = """
            Press the following button to save a chart that shows the total
            COVID-19 cases by date for {Region}
                """.format(Region = Region)
        l1 = Label(wind, text=tx1)
        l1.pack()
        btn1 = Button(wind, text="Total cases Chart!",command=lambda loc=Region: total_cases(loc))
        btn1.pack()
        tx2 = """
            Press the following button to save a chart that shows the total
            COVID-19 cases per million people by date for {Region}
                """.format(Region = Region)
        l2 = Label(wind, text=tx2)
        l2.pack()
        btn2 = Button(wind, text="Cases per million Chart!", command=lambda loc=Region: cases_million(loc))
        btn2.pack()
        tx3 = """
            Press the following button to save a chart that shows the positive
            rate by date for {Region}
                """.format(Region = Region)
        l3 = Label(wind, text=tx3)
        l3.pack()
        btn3 = Button(wind, text="Positive rate Chart!", command=lambda loc=Region: pos_rate(loc))
        btn3.pack()
        tx4 = """
            Press the following button to save a chart that shows the total
            COVID-19 death by date for {Region}
                """.format(Region = Region)
        l4 = Label(wind, text=tx4)
        l4.pack()
        btn4 = Button(wind, text="Total Deaths Chart!", command=lambda loc=Region: total_deaths(loc))
        btn4.pack()
        tx5 = """
            Press the following button to save a chart that shows the total
            COVID-19 vaccinations per hundred people by date for {Region}
                """.format(Region = Region)
        l5 = Label(wind, text=tx5)
        l5.pack()
        btn5 = Button(wind, text="Vaccinations per hundred people Chart!", command=lambda loc=Region: total_vacs(loc))
        btn5.pack()
        wind.mainloop()
        
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
    for i in Grouped_locs:
        Listb.insert(END,i)
    regF.pack(side=TOP)
    regF2 = Frame(regF)
    Btn = Button(regF2, text="Open Region's window!",command=openRegion)
    Btn.pack()
    regF2.pack(side=TOP)
    Wind.mainloop()

"""
    The following function opens the Country window i.e. a window that contains
    a listbox full of Countries and a button to open a Country. It also contains
    the function to open a Country's window. And a Country's window allows a user 
    to create various charts for a Country and save them to that specific 
    Country's folder.
"""
def countryWindow():
    def openCountry():
        Country = Listb.get(Listb.curselection())
        wind = Tk()
        wind.title(Country)
        tx1 = """
            Press the following button to save a chart that shows the total
            COVID-19 cases by date for {Country}
                """.format(Country = Country)
        l1 = Label(wind, text=tx1)
        l1.pack()
        btn1 = Button(wind, text="Total cases Chart!",command=lambda loc=Country: total_cases(loc))
        btn1.pack()
        tx2 = """
            Press the following button to save a chart that shows the total
            COVID-19 cases per million people by date for {Country}
                """.format(Country = Country)
        l2 = Label(wind, text=tx2)
        l2.pack()
        btn2 = Button(wind, text="Cases per million Chart!", command=lambda loc=Country: cases_million(loc))
        btn2.pack()
        tx3 = """
            Press the following button to save a chart that shows the positive
            rate by date for {Country}
                """.format(Country = Country)
        l3 = Label(wind, text=tx3)
        l3.pack()
        btn3 = Button(wind, text="Positive rate Chart!", command=lambda loc=Country: pos_rate(loc))
        btn3.pack()
        tx4 = """
            Press the following button to save a chart that shows the total
            COVID-19 death by date for {Country}
                """.format(Country = Country)
        l4 = Label(wind, text=tx4)
        l4.pack()
        btn4 = Button(wind, text="Total Deaths Chart!", command=lambda loc=Country: total_deaths(loc))
        btn4.pack()
        tx5 = """
            Press the following button to save a chart that shows the total
            COVID-19 vaccinations per hundred people by date for {Country}
                """.format(Country = Country)
        l5 = Label(wind, text=tx5)
        l5.pack()
        btn5 = Button(wind, text="Vaccinations per hundred  people Chart!", command=lambda loc=Country: total_deaths(loc))
        btn5.pack()
        wind.mainloop()
    Wind = Tk()
    Wind.title("Country Select")
    regF = Frame(Wind)
    scroller = Scrollbar(regF)
    Listb = Listbox(regF)
    scroller.pack(side=RIGHT, fill=Y)
    Listb.pack(side=LEFT, fill=Y)
    Listb.config(width=0)
    scroller['command'] = Listb.yview
    Listb['yscrollcommand'] = scroller.set
    for i in Countries:
        Listb.insert(END,i)
    regF.pack(side=TOP)
    regF2 = Frame(regF)
    Btn = Button(regF2, text="Open Country's window!",command=openCountry)
    Btn.pack()
    regF2.pack(side=TOP)
    Wind.mainloop()
    

"""
    These functions basically call the different chart-creation functions
    and call them for every Region and Country in the locs array.
"""    
def all_total_cas():
    for i in locs:
        total_cases(i)
def all_cases_mil():
    for i in locs:
        cases_million(i)
def all_pos_rate():
    for i in locs:
        pos_rate(i)
def all_total_det():
    for i in locs:
        total_deaths(i)
def all_total_vacs():
    for i in locs:
        total_vacs(i)
        
"""
    The allwindow() function creates a window that allows a user to click
    the chart commands and use them to create various charts 
    (see chartmaking functions). But when clicked rather than making the chart
    for an individual Region/Country, the chart creator makes and saves a chart
    of the specified type for every country/region.
"""        
def allWindow():
        wind = Tk()
        wind.title("All Regions/Countries")
        tx1 = """
            Press the following button to save several charts that show the total
            COVID-19 cases by date for all countries/regions 
            (saves one for each Country/Region)
                """
        l1 = Label(wind, text=tx1)
        l1.pack()
        btn1 = Button(wind, text="Total cases Chart!",command=all_total_cas)
        btn1.pack()
        tx2 = """
            Press the following button to save several charts that show the total
            COVID-19 cases per million people by date for all countries/regions
            (saves one for each Country/Region)
                """
        l2 = Label(wind, text=tx2)
        l2.pack()
        btn2 = Button(wind, text="Cases per million Chart!",command=all_cases_mil)
        btn2.pack()
        tx3 = """
            Press the following button to save several charts that show the positive
            rate by date for all countries/regions
            (saves one for each Country/Region)
                """
        l3 = Label(wind, text=tx3)
        l3.pack()
        btn3 = Button(wind, text="Positive rate Chart!",command=all_pos_rate)
        btn3.pack()
        tx4 = """
            Press the following button to save several charts that show the total
            COVID-19 death by date for all countries/regions
            (saves one for each Country/Region)
                """
        l4 = Label(wind, text=tx4)
        l4.pack()
        btn4 = Button(wind, text="Total Deaths Chart!",command=all_total_det)
        btn4.pack()
        tx5 = """
            Press the following button to save several charts that show the total
            COVID-19 vaccinations per hundred people by date for all countries/regions
            (saves one for each Country/Region)
                """
        l5 = Label(wind, text=tx5)
        l5.pack()
        btn5 = Button(wind, text="Vaccinations per hundred  people Chart!",command=all_total_vacs)
        btn5.pack()
        wind.mainloop()


"""
    This is the main window and allows users to open up either a regions window
    , a country window or an all window. The regions window allows users to
    select regions that they can make charts for, the Countries window allows
    users to select Countries that they can make charts for and the all window
    allows users to make specified charts for all regions/countries.
"""
Window = Tk()
Window.title("COVID Area Selections")
lbText = """
            This program allows you the user to recieve charts that depict 
            various things in regards to the COVID-19 data sourced from
            https://covid.ourworldindata.org/data/owid-covid-data.csv .
            This data shows various things for various countries and regions
            such as the total cases for particular date ranges, population
            vaccinated for particular date ranges, infection rate, total 
            deaths etc. Charts use these data point to help users gain
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
regText = "Click this button to open up the Regions window!"
lab1 = Label(Window,text=" ")
lab1.grid(row=1,column=0)
RegionBtn = Button(Window,text=regText,command=regionWindow)
RegionBtn.grid(row=2,column=0)
lab2 = Label(Window,text=" ")
lab2.grid(row=3,column=0)
CountryText = "Click this button to open up the Countries Window!"
CountryBtn = Button(Window,text=CountryText, command=countryWindow)
CountryBtn.grid(row=4,column=0)
lab3 = Label(Window,text=" ")
lab3.grid(row=5,column=0)
AllText = "Click this button to open up the all Regions/Countries Window!"
AllBtn = Button(Window,text=AllText,command=allWindow)
AllBtn.grid(row=6,column=0)
Window.mainloop()