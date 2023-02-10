# Cryptocurrency Trading Algorithm
The prominence of Cryptocurrencies as a means of transaction and investment vehicle has seen astronomical growth in recent years - but what is it and how is it different than the traditional currencies we're used to? The currencies you are familar with and likely use on a day-to-day basis, such as the US Dollar and the Euro, are known as *fiat currencies*. They are issued by the government and there exists a central authority, such as a central bank, to regulate and govern it's use. In stark contrast, a defining feature of a *Cryptocurrency* is that there is no central regulatory authority. Instead, transactions are held in a ledger or database which is secured cryptographically. Both types of currencies have their advantages and disadvantages.

While this is all interesting, the most important question you might be asking is "what's in it for me?" As an individual investor, you may find success in trading Cryptocurrencies to take home a profit - but unfortunately, that often involves a significant time investment, tracking charts and prices to determine what the next trade to make is. If that sounds appealing, then by all means, enjoy! It is certainly a viable option.

If, however, you prefer a little more of a hands-off approach, a trading algorithm may be here to save the day. Algorithmic trading is a way to automate making decisions on when to buy or sell an asset based on some pre-programmed instructions and criteria. You design and implement a trading strategy and let the computer do the work for you! If the strategy is effective and well-tested, then you can potentially earn money while you sleep without having to spend hours staring at charts.

## **Learnings**
*After completing this guided project you will be able to:*

*   Fetch Cryptocurrency market prices and data
*   Perform basic analysis of market behaviour
*   Implement a simple algorithmic trading strategy
*   Analyze the performance of the trading algorithm

## **Key Features**

*   Yahoo Finance is a popular website and service that provides up-to-date financial news and market quotes. Luckily, there is a Python library called `yfinance` that allows you to easily access and save this data
*   The yfinance library has a built-in method for retrieving historical market data. Let's use this to get the exchange rate of Bitcoin to US Dollars over the year of 2020. We use the `download()` method, passing in the ticker we're interested in ("BTC-USD"), the start and end dates, and the time interval between datapoints. Let's use a 1 day interval
*   Price charts are an essential tool for understanding and analyzing a given stock or currency. They are a time series showing an asset's price over time. This project uses the same ideology to present the outcomes
*   A Moving Average is a staple in the analysis of price charts. It's calculated by creating a series of averages of subsets of the data we have
*   Backtesting the algorithm with user input



## **Outcome**
1. One of the simplest trading strategies making use of Simple Moving Averages is the [***Moving Average Crossover***](https://en.wikipedia.org/wiki/Moving_average_crossover?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkQuickLabsanalyzecryptomarketswiththecoinbaseapi28469139-2022-01-01). The basic idea behind this strategy is to use two Simple Moving Averages - one with a relatively short sampling interval and the other with a longer interval. When the shorter moving average crosses over the longer interval moving average, it can signal a reversal in trend. For example, if the shorter term moving average is below the longer moving average but then crosses over to the top of it, this may signal the beginning of an upwards (bullish) trend. Using the *Moving Average Crossover* strategy, this would be a *buy* signal. Similarily, when the shorter moving average is above the longer interval one and it crosses under, this could signal a downward (bearish) trend, which would be a *sell* signal in this strategy.\`
2. Once you have a trading algorithm implemented, you will certainly want to test it to see if it can actually produce a profit and compare its performace with other strategies. Often, the first way to do this is to perform a [**backtest**](https://www.investopedia.com/terms/b/backtesting.asp?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkQuickLabsanalyzecryptomarketswiththecoinbaseapi28469139-2022-01-01). The core idea behind a backtest is to simulate running your trading algorithm on historical data and compute several metrics, such as the return. While this method certainly *does not* guarantee that the algorithmn will be consistently profitable, it's a quick way to test the viability of a strategy and reject clearly unfeasable strategies.

