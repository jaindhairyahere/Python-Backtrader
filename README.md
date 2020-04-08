Cerebro - Serves as the simulator of market
We create a Cerebro Object (cerebro = bt.Cerebro()) first i.e. setup the market, brokers, and us

Consider a broker which helps us invest i.e. maybe reduces our efforts and takes care of ur portfolio. We hand him some capital by cerebro.broker.set_cash(amount) method.
We may also set some commissioin for him by cerebro.broker.setcommission(commission = c) method. This sets commission as a fraction of Each Action Cost.

DataFeed - Data Feed Objects represent the data. We make a datafeed object by specifying datasource, fromdate, todate, and boolean 'reverse' parameter. 

Strategy Objects - We store a strategy as a class. All strategies are generally stored in some file. 
['IndType', 'ObsType', 'PriceClose', 'PriceDateTime', 'PriceHigh', 'PriceLow', 'PriceOpen', 'PriceOpenInteres', 'PriceVolume', 'StratType', '_OwnerCls', '__abs__', '__add__', '__bool__', '__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__div__', '__doc__', '__eq__', '__floordiv__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__pow__', '__radd__', '__rdiv__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__weakref__', '_addanalyzer', '_addanalyzer_slave', '_addindicator', '_addnotification', '_addobserver', '_addsizer', '_addwriter', '_alnames', '_clk_update', '_clock', '_getanalyzer_slave', '_getline', '_getminperstatus', '_id', '_lineiterators', '_ltype', '_makeoperation', '_makeoperationown', '_mindatas', '_minperiod', '_next', '_next_analyzers', '_next_observers', '_next_open', '_nextforce', '_notify', '_oldsync', '_once', '_oncepost', '_oncepost_open', '_operation', '_operation_stage1', '_operation_stage2', '_operationown', '_operationown_stage1', '_operationown_stage2', '_opstage', '_orders', '_orderspending', '_owner', '_periodrecalc', '_periodset', '_plotinit', '_plotlabel', '_roperation', '_settz', '_sizer', '_slave_analyzers', '_stage1', '_stage2', '_start', '_stop', '_tradehistoryon', '_trades', '_tradespending', 'add_timer', 'addindicator', 'addminperiod', 'advance', 'alias', 'aliased', 'analyzers', 'array', 'backwards', 'bind2line', 'bind2lines', 'bindlines', 'broker', 'buy', 'buy_bracket', 'cancel', 'cerebro', 'clear', 'close', 'csv', 'data', 'data0', 'data0_0', 'data0_1', 'data0_2', 'data0_3', 'data0_4', 'data0_5', 'data0_6', 'data0_7', 'data0_adjclose', 'data0_close', 'data0_datetime', 'data0_high', 'data0_low', 'data0_open', 'data0_openinterest', 'data0_volume', 'data_0', 'data_1', 'data_2', 'data_3', 'data_4', 'data_5', 'data_6', 'data_7', 'data_adjclose', 'data_close', 'data_datetime', 'data_high', 'data_low', 'data_open', 'data_openinterest', 'data_volume', 'dataclose', 'datas', 'ddatas', 'dnames', 'env', 'extend', 'forward', 'frompackages', 'getdatabyname', 'getdatanames', 'getindicators', 'getindicators_lines', 'getobservers', 'getposition', 'getpositionbyname', 'getpositions', 'getpositionsbyname', 'getsizer', 'getsizing', 'getwriterheaders', 'getwriterinfo', 'getwritervalues', 'home', 'incminperiod', 'l', 'line', 'line0', 'line_0', 'linealias', 'lines', 'log', 'minbuffer', 'next', 'next_open', 'nextstart', 'nextstart_open', 'notify_cashvalue', 'notify_data', 'notify_fund', 'notify_order', 'notify_store', 'notify_timer', 'notify_trade', 'observers', 'once', 'oncestart', 'order', 'order_target_percent', 'order_target_size', 'order_target_value', 'p', 'packages', 'params', 'plotinfo', 'plotlabel', 'plotlines', 'position', 'positionbyname', 'positions', 'positionsbyname', 'prenext', 'prenext_open', 'preonce', 'qbuffer', 'reset', 'rewind', , 'sell_bracket', 'set_tradehistory', 'setminperiod', 'setsizer', 'sizer', , 'stats', , 'updateminperiod', 'writers']

'start'
'stop'
'sell'



CEREBRO MAINTAINS ==>> (Data Feeds), actors (Stratgegies), spectators (Observers), critics (Analyzers) and documenters (Writers)
    1. Create a cerebro
        bt.Cerebro(**kwargs)
    2. Add Data Feeds
        cerebro.adddata( data: data_feed_object)
    3. Add Strategy
        cerebro.addstrategy( MyStrategy: strategy_object, **optimization_parameters)
    4. Other Elements
        cerebro.addwriter, addanalyzer, addobserver, addobservermulti 
    5. Changing the broker
        broker = MyBroker() ... a broker class that inherits from bt.broker
        cerebro.broker = broker ... @property
    6. Receive Notifications
        a. 




STRATEGIES ==>> Cerebro takes directly the Strategy class and the arguments to pass to it. The rationale behind: in an optimization scenario the class will be instantiated several times and passed different arguments

self.position is false when our basket size i.e. size of portfolio with us is 0 else it is true
len(self) returns number of data rows accessed till then