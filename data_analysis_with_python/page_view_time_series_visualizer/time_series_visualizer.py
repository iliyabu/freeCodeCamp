import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])
df = df.set_index('date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 8))

    df.plot(ax=ax, title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views',
            legend=False, color='r')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['Years'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar['Months'] = pd.DatetimeIndex(df_bar['date']).month
    df_bar.drop('date', axis=1, inplace=True)
    df_bar = df_bar.groupby(['Years', 'Months']).mean()
    df_bar = df_bar.unstack()
    df_bar = df_bar.droplevel(1, axis=1)
    df_bar.columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']
    df_bar.columns.name = 'Months'

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 8))
    df_bar.plot.bar(ax=ax, ylabel='Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month'] = pd.Categorical(df_box['month'],
                                     categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
                                                 'Nov', 'Dec'],
                                     ordered=True)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))

    sns.boxplot(ax=axes[0], data=df_box, x='year', y='value').set(xlabel='Year', ylabel='Page Views',
                                                                  title='Year-wise Box Plot (Trend)')
    sns.boxplot(ax=axes[1], data=df_box, x='month', y='value').set(xlabel='Month', ylabel='Page Views',
                                                                   title='Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
