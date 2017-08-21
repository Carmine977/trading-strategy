# trading-strategy

## Overview 

This repository shows a practical application of two basic trading strategies that make use of some highly popular technical indicators, like Bollinger bands and momentum, to determine when to buy, sell or short shares of a given stock.
When stock price crosses the bollinger bands it may be interpreted as a signal to buy or to sell, since this denotes important changes in market volatility. The momentum instead, expresses the energy prices have to move in a certain direction. 

## Contents

This repository consists of three notebooks:

1. Bollinger Strategy 1    
The first strategy presented here detects a buy signal when price crosses the lower-band from below and triggers an exit signal when price hits the middle band (moving average). Instead, a short selling signal is detected when price crosses the upper-band from above, while the exit of the short position is triggered when price hits the middle band.  
The result of such a simple strategy over the stock IBM for the time period of Dec 31, 2007 to Dec 31, 2009 can be seen in the plot below. 

![Bollinger Strategy 1 graph](https://github.com/Carmine977/trading-strategy/blob/master/data/images/IBM_Strategy_1.png)

Vertical lines on the chart denote trades events: green lines indicate buying long, red lines indicate selling short, and black lines indicate exits of either short or long position. All of the trades were for 100 stocks each.  
The plot below shows the value of this portfolio compared to the value of the stock itself over the same time period. As you can see, the use of this simple strategy would generate a +34% profit against +25,6% of the stock.

![Bollinger Strategy 1 value](https://github.com/Carmine977/trading-strategy/blob/master/data/images/IBM_Strategy_1_BackTesting.png)

2. Bollinger Strategy 2  
First strategy requires the opening of a high number of positions, many of which close with losses. In the second strategy, I try to get an higher profit and lower risk by opening only long positions (no shorting sell) and applying a slightly different strategy, which combines bollinger bands with momentum.   
In particular, the buy signal is given when price crosses the middle-band from below with a positive momentum, while the exit signal is triggered when price reaches the upper band. The use of momentum in this strategy can significantly reduce the number of false positive signals.   
Results are shown in the picture below, where it can be seen that over the period considered the overall return is 56,5%.

![Bollinger Strategy 2 value](https://github.com/Carmine977/trading-strategy/blob/master/data/images/IBM_Strategy_2_BackTesting.png)

3. Back-Testing Simulator    
The above plots were obtained using the backtesting method of this third notebook. The backtesting simulation is a process by which all of the trades recommended by the strategy are fed into an order book, and a simulation is run from the beginning of the time period till the end to see how the strategy wuold perform.


## Usage

Run these codes using [jupyter notebook](http://jupyter.readthedocs.io/en/latest/install.html). Just type `jupyter notebook` in the main directory and the code will pop up in a browser window. 





