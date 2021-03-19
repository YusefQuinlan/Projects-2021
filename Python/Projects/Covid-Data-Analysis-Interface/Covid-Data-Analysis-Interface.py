# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:01:14 2021

@author: Yusef Quinlan
"""

#import and getting the data into a DataFrame
import pandas as pd
from tkinter import *

df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

#Putting the columns into a variable, can view it with Spyder IDE
cols = df.columns

