import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.scatter(x = 'Year', y = 'CSIRO Adjusted Sea Level', data = df)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'] )
    
    years = df['Year'].append(pd.Series(range(2014, 2050)))
    plt.plot(years, intercept + slope*years, 'r', label='fitted line')


    # Create second line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x = df.loc[df['Year']>=2000, 'Year'], y = df.loc[df['Year']>=2000,'CSIRO Adjusted Sea Level'])
    years = years.loc[years >= 2000]
    
    plt.plot(years, intercept + slope*years, 'g', label='fitted line2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()