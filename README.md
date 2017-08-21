# trading-strategy

## Overview 

This repository shows the practical application of two basic trading strategies that make use of highly popular technical indicators, like Bollinger bands and momentum, to determine when to buy, sell or short shares of a given stock.

## Contents

This repository consists of three notebooks:

1. Bollinger Strategy 1
When price crosses the bollinger bands, it may be interpreted as a signal to buy or to sell, since they denote important changes in market volatility. 
This first strategy detects a buy signal when price crosses the lower-band from below and triggers exit of the long position when price hits the middle band (moving average).
On the other hand, a short sell signal is detected when price crosses the upper-band from above, while it triggers exit of the short position when price hits the middle band from above.
The result of such a strategy over the stock IBM for the time period of Dec 31, 2007 to Dec 31, 2009 can be seen in the graph below. 

The vertical lines on the chart denote trades – red lines indicate a beginning to short sell a stock, green lines indicate buying a stock to hold long-term, and black lines indicate exits of either a short or long position. All of the trades were for 100 stocks each.  
And here's a graph of the value of this portfolio over time, compared to the value of the S&P 500 over the same time period and the same starting funds of $10,000


2. Bollinger Strategy 2

3. Back-Testing Simulator

## Usage

Run these codes using [jupyter notebook](http://jupyter.readthedocs.io/en/latest/install.html). Just type `jupyter notebook` in the main directory and the code will pop up in a browser window. 





