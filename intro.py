import backtrader as bt
import backtrader.indicators as btind
import backtrader.feeds as btfeeds
import datetime
from strategies import TestStrategy
import os
import sys
import pandas as pd
# We use strategies as classes in this
# Pass Data Feed objects to Strategy

# class MyStrategy(bt.Strategy):
#     params = dict(period=20)
#     def __init__(self):
#         self.sma = btind.MovingAverageSimple(self.datas[0], period=self.params.period)


cerebro = bt.Cerebro()
cerebro.addstrategy(TestStrategy)

datapath = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),'oracle.csv')
data = btfeeds.YahooFinanceCSVData(dataname=datapath,
    fromdate=datetime.datetime(2014, 1, 1),
    todate = datetime.datetime(2014,12,31),
    reverse = False
    )
cerebro.adddata(data)

cerebro.broker.set_cash(1000000)
cerebro.broker.setcommission(commission=0.001)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())