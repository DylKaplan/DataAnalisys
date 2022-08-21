import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', header=0, index_col='date', parse_dates=['date'])

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(15,5))
    plt.plot(df)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()





    # Save image and return fig 
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
     
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(['year','month'])['value'].mean()
    df_bar = df_bar.unstack()
    
    # Draw bar plot
    fig = df_bar.plot.bar(figsize=(10,7),xlabel='Years',ylabel='Average Page Views').figure
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])




    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots 
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(20,9))
   
    box1 = sns.boxplot(x=df_box['year'], y=df_box['value'], orient='v', ax=axes[0])
    box1.set_ylabel("Page Views", fontsize=12)
    box1.set_title("Year-wise Box Plot (Trend)", fontsize=14)
    
    box2= sns.boxplot(x=df_box['month'], y=df_box['value'], orient='v', ax=axes[1])
    box2.set_ylabel("Page Views", fontsize=12)
    box2.set_title("Month-wise Box Plot (Seasonality)", fontsize=14)
    plt.show()




    # Save image and return fig 
    fig.savefig('box_plot.png')
    return fig
