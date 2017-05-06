# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



# Handle table-like data and matrices
import numpy as np
import pandas as pd

# Visualisation
import matplotlib 
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns
wholedf = pd.read_csv('Baby_Names_1880-2014.csv')
wholedf.head(5)
wholedf['Year'] = pd.to_datetime(wholedf['Year'])
wholedf['month'] = wholedf['Year'].dt.month
wholedf['day'] = wholedf['Year'].dt.day
wholedf['year'] = wholedf['Year'].dt.year
       
sns.lmplot(x='year', y='Count', data=wholedf)