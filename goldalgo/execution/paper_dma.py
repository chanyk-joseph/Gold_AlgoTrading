from goldalgo.orders import *
from goldalgo.common.symbol import *
from goldalgo.execution.dma import *
from goldalgo.execution.scheduler import *
from goldalgo.execution.order_queue import *

class PaperDMA(DMA):

    _name = 'Paper_DMA'

    def __init__(self):
        self._filled = TradeScheduler()
        self._limit_orders = {}

    def _get_bar(self, config, symbol_code, timestamp):
        fields = []
        data_provider = config.get_data_provider()
        symbol = data_provider.get_symbol(symbol_code)
        #bar = symbol.get_hist_data(start_datetime, end_datetime, bar_size, fields)


    def _gen_filled_order(self, timestamp, order, price):
        soid = order.get_soid()
        coid = order.get_coid()
        foid = 1
        symbol_code = order.get_symbol()
        action = order.get_action()
        qty = order.get_qty()
        return FilledOrder(soid, coid, foid, timestamp, symbol_code, action, qty, price, 0)


    def _execute_limit_orders(self, config, timestamp):
        for symbol_code in self._limit_orders.keys():
            bar = self._get_bar(config, symbol_code, timestamp)

            orders = self._limit_orders[symbol_code]
            for i, order in enumerate(orders):
                action = order.get_action()
                limit_price = order.get_limitprice()
                if action == ACTION_BUY:
                    if limit_price < bar[LOW_PRICE].values[0]:
                        continue
                else:   # sell
                    if limit_price > bar[HIGH_PRICE].values[0]:
                        continue

                orders.pop(i)
                fo = self._gen_filled_order(timestamp, order, limit_price)
                self._scheduler.add(timestamp, fo)
            # end loop orders
        # end loop symbols


    def execute_child_orders(self, config, timestamp, orders):
        for order in orders:
            order_type = order.get_ordertype()
            if order_type == ORDER_TYPE_MARKET:
                symbol_code = order.get_symbol()
                action = order.get_action()
                bar = self._get_bar(config, symbol_code, timestamp)
                if action == ACTION_BUY:
                    price = bar[OPEN_ASK].values[0]
                else:  # sell
                    price = bar[OPEN_BID].values[0]
                fo = self._gen_filled_order(self, timestamp, order, price)
                self._scheduler.add(timestamp, fo)

            else: # limit order
                symbol_code = order.get_symbol()
                if not symbol_code in self._limit_orders.keys():
                    self._limit_orders[symbol_code] = []
                self._limit_orders[symbol_code].append(order)
        # end loop orders
        self._execute_limit_orders(self, config, timestamp)


    def pop_filled_order(self, timestamp):
        return self._filled.pop_orders(timestamp)
