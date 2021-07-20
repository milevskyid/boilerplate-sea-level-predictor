#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'])
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')

    # Create first line of best fit
    plt.figure(figsize=(14,6))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    # Create first line of best fit
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    x_det = list(range(1880,2051))
    y_det = list()
    for year in x_det:
      y_det.append(year*res.slope + res.intercept)
    plt.plot(x_det, y_det, 'r')

    # Create second line of best fit
    y_from_2000 = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    x_from_2000 = df[df['Year'] >= 2000]['Year']

    res_2000 = linregress(x_from_2000, y_from_2000)

    x_2000 = list(range(2000, 2051))
    y_2000 = list()
    for each in x_2000:
      y_2000.append((each*res_2000.slope + res_2000.intercept))
    plt.plot(x_2000, y_2000, 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()


# In[ ]:




