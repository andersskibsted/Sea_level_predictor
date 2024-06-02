import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linreg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = linreg.slope
    intercept = linreg.intercept
    extended_year = range(1880, 2051)
    line_of_best_fit = [slope * xi + intercept for xi in extended_year]
    plt.plot(extended_year,
             line_of_best_fit,
             color='red',
             label='Rise in Sea Level')
    plt.title('Rise in Sea Level')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    linreg_2000 = linregress(df_2000['Year'],
                             df_2000['CSIRO Adjusted Sea Level'])
    slope_2000 = linreg_2000.slope
    intercept_2000 = linreg_2000.intercept
    line_of_best_fit_2000 = [
        slope_2000 * xi + intercept_2000 for xi in range(2000, 2051)
    ]
    plt.plot(range(2000, 2051),
             line_of_best_fit_2000,
             color='green',
             label='Rise in Sea Level')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
