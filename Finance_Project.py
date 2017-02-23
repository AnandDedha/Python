

from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().magic('matplotlib inline')
import plotly
import cufflinks as cf
cf.go_offline()



# CitiGroup
C = data.DataReader("C", 'google', start='2006-01-01', end='2016-01-01')

# JPMorgan Chase
JPM = data.DataReader("JPM", 'google', start='2006-01-01', end='2016-01-01')

# Morgan Stanley
MS = data.DataReader("MS", 'google', start='2006-01-01', end='2016-01-01')


tickers = ['C', 'JPM', 'MS']

bank_stocks = pd.concat([C,JPM, MS],axis=1,keys=tickers)
bank_stocks.columns.names = ['Bank Ticker','Stock Info']
bank_stocks.head()
bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()

returns = pd.DataFrame()


for tick in tickers:
    returns[tick+' Return'] = bank_stocks[tick]['Close'].pct_change()
returns.head()

import seaborn as sns
sns.pairplot(returns[1:])

returns.idxmin()

returns.idxmax()

returns.std() # Citigroup riskiest

returns.ix['2015-01-01':'2015-12-31'].std() 

sns.distplot(returns.ix['2015-01-01':'2015-12-31']['MS Return'],color='green',bins=100)

sns.distplot(returns.ix['2008-01-01':'2008-12-31']['C Return'],color='red',bins=100)

for tick in tickers:
    bank_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()

bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()

bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()

plt.figure(figsize=(12,6))
C['Close'].ix['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
C['Close'].ix['2008-01-01':'2009-01-01'].plot(label='C CLOSE')
plt.legend()

sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)


sns.clustermap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)

close_corr = bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr()
close_corr.iplot(kind='heatmap',colorscale='rdylbu')

C[['Open', 'High', 'Low', 'Close']].ix['2015-01-01':'2016-01-01'].iplot(kind='candle')

MS['Close'].ix['2015-01-01':'2016-01-01'].ta_plot(study='sma',periods=[13,21,55],title='Simple Moving Averages')

C['Close'].ix['2015-01-01':'2016-01-01'].ta_plot(study='boll')
