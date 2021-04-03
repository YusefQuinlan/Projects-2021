# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 21:34:33 2021

@author: User
"""

import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import datetime
import os
df1 = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

#Total cases
df2 = df1[['location','date','total_cases']]

df3 = df2.loc[df2['location'] == 'Chile']

datetimes = []
for i in df3['date']:
    datetimes.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
fig = plt.figure()
plt.plot_date(datetimes,df3['total_cases'])
plt.xlabel("Dates")
plt.ylabel("Total cases")
plt.title("Total cases for Chile by date")
plt.gcf().autofmt_xdate() 
plt.gca().xaxis_date()
plt.gca().xaxis.set_major_formatter(DateFormatter('%m, %Y'))
if df3['total_cases'].max() > 900000:
    ylabels = [x for x in plt.gca().get_yticks() /150000 * 150000]
    plt.gca().set_yticklabels(ylabels)
fig.savefig('chilecases.png')
plt.show()


df2 = df1[['location','date','total_cases_per_million']]

df3 = df2.loc[df2['location'] == 'Chile']

datetimes = []
for i in df3['date']:
    datetimes.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
fig = plt.figure()
plt.plot_date(datetimes,df3['total_cases_per_million'])
plt.xlabel("Dates")
plt.ylabel("Total cases per million")
plt.title("Total cases per million for Chile by date")
plt.gcf().autofmt_xdate() 
plt.gca().xaxis_date()
plt.gca().xaxis.set_major_formatter(DateFormatter('%m, %Y'))
if df3['total_cases_per_million'].max() > 900000:
    ylabels = [x for x in plt.gca().get_yticks() /150000 * 150000]
    plt.gca().set_yticklabels(ylabels)
fig.savefig('chilecases.png')
plt.show()


#positive_rate

df2 = df1[['location','date','positive_rate']]

df3 = df2.loc[df2['location'] == 'United Kingdom']

datetimes = []
for i in df3['date']:
    datetimes.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
fig = plt.figure()
plt.plot_date(datetimes,df3['positive_rate'])
plt.xlabel("Date")
plt.ylabel("Positive rate of COVID")
plt.title("Positive rate for United Kingdom by date")
plt.gcf().autofmt_xdate() 
plt.gca().xaxis_date()
plt.gca().xaxis.set_major_formatter(DateFormatter('%m, %Y'))
fig.savefig('engrates.png')
plt.show()

df2 = df1[['location','date','total_deaths']]

df3 = df2.loc[df2['location'] == 'United Kingdom']

datetimes = []
for i in df3['date']:
    datetimes.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
fig = plt.figure()
plt.plot_date(datetimes,df3['total_deaths'])
plt.xlabel("Date")
plt.ylabel("Total deaths caused by COVID")
plt.title("Total deaths caused by Covid for United Kingdom by date")
plt.gcf().autofmt_xdate() 
plt.gca().xaxis_date()
plt.gca().xaxis.set_major_formatter(DateFormatter('%m, %Y'))
if df3['total_deaths'].max() > 900000:
    ylabels = [x for x in plt.gca().get_yticks() /150000 * 150000]
    plt.gca().set_yticklabels(ylabels)
fig.savefig('engdeaths.png')
plt.show()

df2 = df1[['location','date','total_vaccinations_per_hundred']]

df3 = df2.loc[df2['location'] == 'United Kingdom']

datetimes = []
for i in df3['date']:
    datetimes.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
fig = plt.figure()
plt.plot_date(datetimes,df3['total_vaccinations_per_hundred'])
plt.xlabel("Date")
plt.ylabel("Total Vaccinations per hundred people")
plt.title("Total Vaccinations per hundred people in United Kingdom by date")
plt.gcf().autofmt_xdate() 
plt.gca().xaxis_date()
plt.gca().xaxis.set_major_formatter(DateFormatter('%m, %Y'))
fig.savefig('engvacs.png')
plt.show()