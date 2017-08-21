# trading-strategy

## Overview 

This repository shows a practical application of two basic trading strategies that make use of some highly popular technical indicators, like Bollinger bands and momentum, to determine when to buy, sell or short shares of a given stock.

## Contents

This repository consists of three notebooks:

1. Bollinger Strategy 1    
When stock price crosses the bollinger bands it may be interpreted as a signal to buy or to sell, since this denotes important changes in market volatility. 
The first strategy presented here detects a buy signal when price crosses the lower-band from below and triggers an exit signal (for the long position) when price hits the middle band (moving average).
A short sell signal is instead detected when price crosses the upper-band from above, and the exit of the short position is triggered when price hits the middle band.
The result of such a simple strategy over the stock IBM for the time period of Dec 31, 2007 to Dec 31, 2009 can be seen in the plot below. 

![Bollinger Strategy graph](https://github.com/Carmine977/trading-strategy/blob/master/data/images/IBM_Strategy_1.png)

Vertical lines on the chart denote trades events: green lines indicate buying long, red lines indicate selling short, and black lines indicate exits of either short or long position. All of the trades were for 100 stocks each.  
The plot below shows the value of this portfolio over time compared to the value of the stock itself over the same time period. As you can see the use of this simple strategy would generate a +34% profit against +25,6% of the stock.

![Bollinger Strategy value](https://github.com/Carmine977/trading-strategy/blob/master/data/images/IBM_Strategy_1_BackTesting.png)

2. Bollinger Strategy 2

3. Back-Testing Simulator



## Usage

Run these codes using [jupyter notebook](http://jupyter.readthedocs.io/en/latest/install.html). Just type `jupyter notebook` in the main directory and the code will pop up in a browser window. 





