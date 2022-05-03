import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 8))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    first_line_years = pd.Series([x for x in range(1880, 2051)])
    first_line_of_best_fit = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(first_line_years, first_line_of_best_fit.intercept + first_line_of_best_fit.slope * first_line_years)

    # Create second line of best fit
    second_line_years = pd.Series([x for x in range(2000, 2051)])
    second_line_of_best_fit = linregress(df[df['Year'] >= 2000]['Year'],
                                         df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    plt.plot(second_line_years, second_line_of_best_fit.intercept + second_line_of_best_fit.slope * second_line_years)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
