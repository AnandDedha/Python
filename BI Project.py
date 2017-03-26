
# coding: utf-8

# In[87]:

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
Sales_data.head(6)
Sales_data['Date'] = pd.to_datetime(Sales_data['Date'])
Sales_data['Year'] = Sales_data['Date'].dt.year
Sales_data['month'] = Sales_data['Date'].dt.month
print (Sales_data.head(6))
Sales_by_month = Sales_data.groupby('month').sum()
Sales_by_region = Sales_data.Sales.groupby(Sales_data.Province).sum()  #Returing a series which contains Province as index and sales as values
print(Sales_by_region.values)
labels=Sales_by_region.index
values= Sales_by_region.values
fig = {
    'data': [{'labels': Sales_by_region.index,
              'values': Sales_by_region.values,
              "hole": .4,
              'type': 'pie'}],
    'layout': {'title': 'Sales per Region'}
     }

py.iplot(fig)
Sales_by_month.iplot(kind = 'bar', y= 'Sales')
#Sales_by_region.iplot(kind= 'bar', labels= Sales_by_region.index, values = Sales_by_region.values)


# In[ ]:




# In[ ]:



