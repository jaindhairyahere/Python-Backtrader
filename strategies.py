import backtrader as bt
import backtrader.indicators as btind
import backtrader.feeds as btfeeds
import datetime
import logging
from typing import *
import pandas as pd
# from inspect import 

# print(function(bytearray))

Store = NewType('Store', bt.Store)
Order = NewType('Order',bt.Order)
logging.basicConfig(level=logging.INFO,
        filename="MarketLogs.log",
        format="%(message)s")
class TestStrategy(bt.Strategy):
    params = dict(period1=20,period2=25,period3=10)
    def log(self, txt, dt=None):
        ''' Logging function for this strategy Created by US'''
        dt = dt or self.datas[0].datetime.date(0)
        logging.info('%s, %s' % (dt.isoformat(), txt))
    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.order = None
        # f = open("abcd.txt","w")
        # for i in dir(self):
        #     print(i+"\t : \t",getattr(self,i))
        # f.flush()
        # f.close()
    def notify_order(self, order):
        # print("notify_ORDER\t",)
        if order.status in [order.Submitted, order.Accepted]:
            return 
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))
            elif order.issell():
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))
            self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None

    # def notify_store(self, msg, *args, **kwargs):
    #     print("notify_store\t",)
    #     print("Notification 0")

    # class Cerebro:
    #     def notify_store(self, msg, *args, **kwargs):
    #         print("\tTestStrategy < Cerebro < notify_order")
    #         print("Notification 1")

    def notify_trade(self, trade: bt.Trade):
        # print("notify_trade\t",)
        print(trade.price)
        print(trade)
        print()
        if not trade.isclosed:
            return
        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))


    def next(self):
        # print()
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' %self.dataclose[0])
        if self.order:
            # If there is a pending order then do not itereate to next row in data
            return 
        if not self.position:
            # print("self.position is None/False : ",self.position)
            
            # Position (asset size, asset price) -> NONE if both size and price are none
            # Position is none initially as we have nothing in hand
            if self.dataclose[0] < self.dataclose[-1]:
                if self.dataclose[0] < self.dataclose[-2]:
                    self.log('BUY CREATE, %0.2f' % self.dataclose[0])
                    self.order = self.buy(size=9)
        else:
            # print("self.position is True : ",self.position)
            
            if len(self) >= (self.bar_executed + 5):
                self.log('SELL CREATED {}'.format(self.dataclose[0]))
                self.order = self.sell(size=3)
    
    def buy(self, *args, **kwargs):
        print("BOUGHT")
        return super(TestStrategy, self).buy(*args, **kwargs)
    def sell(self, *args, **kwargs):
        print("SOLD")
        return super(TestStrategy, self).sell(*args, **kwargs)
