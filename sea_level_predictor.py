import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    new_x = pd.Series([i for i in range(1880,2051)])
    new_y = linr.intercept + linr.slope*new_x

    plt.plot(new_x, new_y, 'r')

    # Create second line of best fit
    df_cut = df[df['Year'] >= 2000]
    
    linr2 = linregress(df_cut['Year'], df_cut['CSIRO Adjusted Sea Level'])
    
    new_x2 = pd.Series([i for i in range(2000,2051)])
    new_y2 = linr2.intercept + linr2.slope*new_x2
    
    plt.plot(new_x2, new_y2, 'g')



    # Add labels and title
    plt.ylabel("Sea Level (inches)")
    plt.xlabel("Year")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
