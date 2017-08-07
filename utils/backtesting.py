import pandas as pd
import numpy as np
import os
from utils.util import get_data, plot_data, get_bollinger_bands, get_portfolio_stats
import matplotlib.pyplot as plt
from itertools import izip
get_ipython().magic(u'matplotlib inline')

def simulate_strategy(date_start, date_end, folder_strategy, file_strategy):

    dates = pd.date_range(date_start, date_end)
    file_name = os.path.join(folder_strategy, '{}.csv'.format(file_strategy))

    # Load orders
    orders = pd.read_csv(file_name, index_col=0, parse_dates=True)
    stock = orders.ix[0]['Symbol'] 

    # Load stock data and join orders in the same DataFrame 
    prices_all = get_data([stock], dates)
    df = prices_all[[stock]]
    df = df.join(orders[['Order', 'Shares']])

    # Back-Testing Algorithm
    df['daily_val'] = 0.0
    hold = False

    # Compute portfolio daily value
    for i, row in df.iterrows():
    
        if row['Order'] == 'BUY':
            hold = True
            n_stocks = row['Shares']
    
        if hold == True:
            df.loc[i, 'Shares'] = n_stocks # replicate shares when stock is hold
            df.loc[i, 'daily_val'] = n_stocks * row[stock]

        if row['Order'] == 'SELL':
            hold = False

    # Compute daily returns
    df['daily_return'] = df['daily_val'].diff()        
    # Reset to 0 NaN and not valid daily_returns  
    df.ix[0, 'daily_return'] = 0
    for (index1, row1),(index2, row2) in izip(df.iterrows(), df[1:].iterrows()):
        if np.isnan(row1['Shares']) or np.isnan(row2['Shares']):
            df.loc[index2, 'daily_return'] = 0.0
    df['cum_return'] = df['daily_return'].cumsum()

    # Compute cumulative portfolio value
    T0 = df[df['Order']=='BUY'].index[0] # Timestamp @ first investment 
    Val0 = df.ix[T0]['daily_val'] # Initial portfolio value
    df['port_val'] = df['cum_return'] + Val0

    # Plot Section
    df_temp = pd.concat([df[stock]/df.ix[0][stock], df['port_val']/df.ix[T0]['port_val']], keys=[stock, 'Portfolio'], axis=1)
    ax = df_temp.plot(figsize=(15, 10))
    # Plot events
    for day, key in orders.iterrows():
        if key['Order'] == 'BUY':
            ax.axvline(x=day, color='green')
        elif key['Order'] == 'SELL':
            ax.axvline(x=day, color='red')
    plt.show()   

    # Compute stats sections
    sharpe_ratio, cum_ret, avg_daily_ret, std_daily_ret = get_portfolio_stats(df['port_val'])
    sharpe_ratio_stock, cum_ret_stock, avg_daily_ret_stock, std_daily_ret_stock = get_portfolio_stats(df[stock])

    # Compare portfolio against stock
    print "Sharpe Ratio of Fund: {}".format(sharpe_ratio)
    print "Sharpe Ratio of {}: {}".format(stock, sharpe_ratio_stock)
    print
    print "Cumulative Return of Fund: {}".format(cum_ret)
    print "Cumulative Return of {}: {}".format(stock, cum_ret_stock)
    print
    print "Standard Deviation of Fund: {}".format(std_daily_ret)
    print "Standard Deviation of {}: {}".format(stock, std_daily_ret_stock)
    print
    print "Average Daily Return of Fund: {}".format(avg_daily_ret)
    print "Average Daily Return of {}: {}".format(stock, avg_daily_ret_stock)
    print
    print "Initial Portfolio Value: {}".format(df['port_val'][0])
    print "Final Portfolio Value: {}".format(df['port_val'][-1])
    print "Final Portfolio Return: {}".format(df['cum_return'][-1])
    print "Final {} Return: {}".format(stock, (df[stock][-1]-df[stock][0])*n_stocks)
    