
# coding: utf-8

# In[98]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, show
get_ipython().magic('matplotlib inline')
import seaborn as sns
import datetime
from plotly import __version__
import plotly
import plotly.offline as py
import plotly.graph_objs as go
import cufflinks as cf
from plotly.offline import download_plotlyjs , init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()
Sales_data = pd.read_excel('Main.xlsx')
Sales_data.info()
print (Sales_data.head(6))
print(type(Sales_data['Date']))
Sales_data['Date'] = pd.to_datetime(Sales_data['Date'])
Sales_data['Year'] = Sales_data['Date'].dt.year
Sales_data['month'] = Sales_data['Date'].dt.month
#print (Sales_data.head(6))
#Sales_by_month = Sales_data.groupby('month').sum()
Sales_data['Profit'] = (Sales_data['Sales'] - Sales_data['Total Cost']) 
Sales_data['Gross Margin%'] = ( 1 - Sales_data['Total Cost']/(Sales_data['Sales'])) * 100
print (Sales_data['Gross Margin%'])

# Sales by region
Sales_by_region = Sales_data.Sales.groupby(Sales_data.Province).sum()  #Returing a series which contains Province as index and sales as values
#print(Sales_by_region.values)
labels=Sales_by_region.index
values= Sales_by_region.values
fig = {
    'data': [{'labels': Sales_by_region.index,
           'values': Sales_by_region.values,
              "hole": .4,
              'type': 'pie'}],
    'layout': {'title': 'Sales by province'}
     }

py.iplot(fig)

# Sales by Each store

Sales_by_store = Sales_data.groupby('Store').sum() # Group the sales by stores 
Sales_by_store.sort_values(['Sales'], ascending=True, inplace=True)  # Dataframe is sorted using the sales column
Sales_by_store.iplot(kind = 'bar', y= 'Sales')
#print(Sales_data_2016['Profit'])


# Comparsion of profit for 2015 and 2016
Sales_data_2016 = Sales_data[Sales_data.Year == 2016]
Sales_data_2015 = Sales_data[Sales_data.Year == 2015]
Profit_by_month_in_2015 = Sales_data_2015.groupby('month').sum()
Profit_by_month_in_2016 = Sales_data_2016.groupby('month').sum()
#print(Profit_by_month_in_2015['Profit'])
trace1 = go.Bar(
    x= ["January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"],
    y=Profit_by_month_in_2015['Profit'],
    name='Profit in 2015',
    marker=dict(
        color='rgb(210,105,30)' 
    )
)
trace2 = go.Bar(
    x=["January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"],
    y=Profit_by_month_in_2016['Profit'],
    name='Profit in 2016',
    marker=dict(
        color='rgb(244,164,96)' 
    )
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)

fig2 = go.Figure(data=data, layout=layout)
py.iplot(fig2, filename='grouped-bar')



#Avg. Gross margin by month in year

Gross_Margin_by_month_in_2015 = Sales_data_2015.groupby('month').mean()
Gross_Margin_by_month_in_2016 = Sales_data_2016.groupby('month').mean()
#print(Gross_Margin_by_month_in_2015)
Months = ["January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]
gold = [10, 8, 4, 4, 4, 0]
silver = [8, 3, 2, 1, 0, 1]

trace1 = Scatter(
    x=Months, y=Gross_Margin_by_month_in_2015['Gross Margin%'],
    line=Line(
        color='#FFD700',
        width=3
    ),
    name='Gross Margin in 2015'
)

trace2 = Scatter(
    x=Months, y=Gross_Margin_by_month_in_2016['Gross Margin%'],
    line=Line(
        color='#C0C0C0',
        width=3
    ),
    name='Gross Margin in 2016'
)


data = Data([trace1, trace2])
layout = Layout(
    title='Gross Margin by Month',
    updatemenus=list([
        dict(
            x=-0.05,
            y=1,
            yanchor='top',
            buttons=list([
                dict(
                    args=['visible', [True, True]],
                    label='All',
                    method='restyle'
                ),
                dict(
                    args=['visible', [True, False]],
                    label='2015',
                    method='restyle'
                ),
                dict(
                    args=['visible', [False, True]],
                    label='2016',
                    method='restyle'
                )
            ]),
        )
    ]),
)
fig3 = Figure(data=data, layout=layout)
py.iplot(fig3)

# Sales per square feet by each store
Sales_per_Square__by_store_in_2015 = Sales_data_2015.groupby('Store').mean()
Sales_per_Square__by_store_in_2016 = Sales_data_2016.groupby('Store').mean()
Sales_per_Square__by_store_in_2015['Sales_per_square'] = Sales_per_Square__by_store_in_2015['Sales']/Sales_per_Square__by_store_in_2015['Store Size']
Sales_per_Square__by_store_in_2016['Sales_per_square'] = Sales_per_Square__by_store_in_2016['Sales']/Sales_per_Square__by_store_in_2016['Store Size']
print(Sales_per_Square__by_store_in_2015['Sales_per_square'])
print(Sales_per_Square__by_store_in_2016['Sales_per_square'])

trace1 = go.Bar(
    x= Sales_per_Square__by_store_in_2015.index,
    y=Sales_per_Square__by_store_in_2015['Sales_per_square'],
    name='Sales per Sqaure feet by store in 2015',
    marker=dict(
        color='rgb(50,205,50)'
    )
)
trace2 = go.Bar(
    x= Sales_per_Square__by_store_in_2016.index,
    y=Sales_per_Square__by_store_in_2016['Sales_per_square'],
    name='Sales per Sqaure feet by store in 2016',
    marker=dict(
        color='rgb(238,221,130)'
    )
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)

fig4 = go.Figure(data=data, layout=layout)
py.iplot(fig4, filename='grouped-bar')

#Sales_by_month.iplot(kind = 'bar', y= 'Sales')
#Sales_by_region.iplot(kind= 'bar', labels= Sales_by_region.index, values = Sales_by_region.values)


# In[ ]:




# In[ ]:



