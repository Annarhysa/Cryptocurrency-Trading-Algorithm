import yfinance as yf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter

def date_input():
    s_date = input("Enter the start date in (yyyy-mm-dd) format: ")
    e_date = input("Enter the end date in (yyyy-mm-dd) format: ")
    BTC_USD = yf.download("BTC-USD", start= s_date, end= e_date, interval='1d')



    trade_signals = pd.DataFrame(index=BTC_USD.index)

    # Define the intervals for the Fast and Slow Simple Moving Averages (in days)
    short_interval = 10
    long_interval = 40

    # Compute the Simple Moving Averages and add it to the dateframe as new columns
    trade_signals['Short'] = BTC_USD['Close'].rolling(window=short_interval, min_periods=1).mean()
    trade_signals['Long'] = BTC_USD['Close'].rolling(window=long_interval, min_periods=1).mean()

    trade_signals['Signal'] = 0.0
    trade_signals['Signal'] = np.where(trade_signals['Short'] > trade_signals['Long'], 1.0, 0.0)

    trade_signals['Position'] = trade_signals['Signal'].diff()





    #plotting the values
    fig, ax = plt.subplots(dpi=500)

    # Formatting the date axis
    date_format = DateFormatter("%h-%d-%y")
    ax.xaxis.set_major_formatter(date_format)
    ax.tick_params(axis='x', labelsize=8)
    fig.autofmt_xdate()


    # Plotting the Bitcoin closing price against the date (1 day interval)
    ax.plot(BTC_USD['Close'], lw=0.75, label='Closing Price')

    # Plot the shorter-term moving average
    ax.plot(trade_signals['Short'], lw=0.75, alpha=0.75, color='orange', label='Short-term SMA')

    # Plot the longer-term moving average
    ax.plot(trade_signals['Long'], lw=0.75, alpha=0.75, color='purple', label='Long-term SMA')


    # Adding green arrows to indicate buy orders
    ax.plot(trade_signals.loc[trade_signals['Position']==1.0].index, trade_signals.Short[trade_signals['Position'] == 1.0],
     marker=6, ms=4, linestyle='none', color='green')

     # Adding red arrows to indicate sell orders
    ax.plot(trade_signals.loc[trade_signals['Position'] == -1.0].index, trade_signals.Short[trade_signals['Position'] == -1.0],
     marker=7, ms=4, linestyle='none', color='red')


    # Adding labels and title to the plot
    ax.set_ylabel('Price of Bitcoin (USD)')
    ax.set_title('Bitcoin to USD Exchange Rate')
    ax.grid() # adding a grid
    ax.legend() # adding a legend

    # Displaying the price chart
    plt.show()


    initial_balance = int(input("Enter how much money you will start with (in USD): "))
    backtest = pd.DataFrame(index=trade_signals.index)
                          
    backtest['BTC_Return'] = BTC_USD['Close'] / BTC_USD['Close'].shift(1) # Current closing price / yesterday's closing price
    backtest['Alg_Return'] = np.where(trade_signals.Signal == 1, backtest.BTC_Return, 1.0)
    backtest['Balance'] = initial_balance * backtest.Alg_Return.cumprod() # cumulative product


    fig, ax = plt.subplots(dpi=500)

    # Formatting the date axis
    date_format = DateFormatter("%h-%d-%y")
    ax.xaxis.set_major_formatter(date_format)
    ax.tick_params(axis='x', labelsize=8)
    fig.autofmt_xdate()

    # Plotting the value of Buy and Hold Strategy
    ax.plot(initial_balance*backtest.BTC_Return.cumprod(), lw=0.75, alpha=0.75, label='Buy and Hold')

    # Plotting total value of Crossing Averages Strategy
    ax.plot(backtest['Balance'], lw=0.75, alpha=0.75, label='Crossing Averages')

    # Adding labels and title to the plot
    ax.set_ylabel('USD')
    ax.set_title('Value of Portfolio')
    ax.grid() # adding a grid
    ax.legend() # adding a legend

    # Displaying the price chart
    plt.show()




if __name__ == '__main__':
    date_input()
                          
    
