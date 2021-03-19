# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:59:28 2021

@author: Yusef Quinlan
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# testing plt import
"""
plt.plot([1,2,3],[3,5,6])
plt.show()
"""

#reading the data and examining it briefly
trends = pd.read_csv('trends.csv')
trends.head()
trends.tail()

# getting the items at rank 1, Globally in 2001
glob_Trends = trends.loc[trends['location']=='Global']
trends_2001 = glob_Trends.loc[glob_Trends['year'] == 2001]
trends_num1 = trends_2001.loc[trends_2001['rank'] == 1]

# 12 categories seems low, lets check that
trend_cats = glob_Trends[['category']].unique()
"""
wow, upon checking it seems there were alot more categories introduced after
2001.
"""

#Getting all the number 1 ranked queries 
Popular = [i for i in trends_num1['query']]

# Make an empty list to put DataFrames into.
rows_Popular = []

"""
    Get DataFrames from rows where the query value is one of the popular items
    in 2001, and append them to the empty list.
"""
for i in Popular:
    rows_Popular.append(trends.loc[trends['query'] == i])

"""
 Alter the variables in the list so the DataFrames only contain 
 'Global' location.
"""  
for i in range(0,len(rows_Popular)):
    rows_Popular[i] = rows_Popular[i].loc[rows_Popular[i]['location'] == 'Global']

"""
    Make a plot for each popular query that plots the years in which it
    was popular other than just 2001 against the score for that year.
    These plots will track the popularity of the most popular items
    in 2001 over the years, and show if they stayed relevant.
"""    
for i in range(0, len(rows_Popular)):
    plt.bar(rows_Popular[i]['year'],rows_Popular[i]['rank'])
    plt.title(Popular[i] + ": Years in which was relevant + rank")
    plt.xlabel('Year/s')
    plt.ylabel('Rank/s')
    plt.xticks(rows_Popular[i]['year'])
    plt.show()


