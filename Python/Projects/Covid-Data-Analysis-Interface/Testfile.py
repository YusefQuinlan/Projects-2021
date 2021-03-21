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
df1 = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

df2 = df1[['location','date','total_cases']]

df3 = df2.loc[df2['location'] == 'Chile']

datetimes = []
for i in df3['date']:
    datetimes.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
deet = True
for i in datetimes:
    if isinstance(i, datetime.datetime):
        print(9)
    else:
        deet = False
plt.plot_date(datetimes,df3['total_cases'])
plt.gcf().autofmt_xdate()
date_format = DateFormatter('%m, %Y')
plt.gca().xaxis_date()
plt.gca().xaxis.set_major_formatter(date_format)
plt.show()