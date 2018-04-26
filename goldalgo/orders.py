import time
import numpy as np

# global constant
ACTION_BUY = 11
ACTION_SELL = 12
ORDER_TYPE_MARKET = 21
ORDER_TYPE_LIMIT = 22

def next_soid():
    return str(int(time.time())) + str(np.random.randint(100)).zfill(2)

class StrategyOrder(object):
    """
    Value object for strategy orders. Strategy orders are the high level
    trading order generated from the process for strategy formation.

    soid: the unique identifier of a strategy order within a project
    timestamp: the time which this order is created.
    symbol: the instrument that we trade.
    action: buy or sell, use the global constant.
    qty: the number of contracts that we trade.
    endtime: specifies the time window for this order.
    must_be_filled: True / False, indicates the order must be 100% completed.
    ref_soid: the reference soid, for example the order that close a previous
              position would reference to the original entry order.
    """

    def __init__(self, soid, timestamp, symbol, action, qty, endtime, must_be_filled=False,
                 ref_soid=None):
        self._soid = soid
        self._timestamp = timestamp
        self._symbol = symbol
        self._action = action
        self._qty = qty
        self._endtime = endtime
        self._must_be_filled = must_be_filled
        self._ref_soid = ref_soid

    def get_soid(self):
        return self._soid

    def get_timestamp(self):
        return self._timestamp

    def get_symbol(self):
        return self._symbol

    def get_action(self):
        return self._action

    def get_qty(self):
        return self._qty

    def get_endtime(self):
        return self._endtime

    def get_must_be_filled(self):
        return self._must_be_filled

    def get_ref_soid(self):
        return self._ref_soid



class ChildOrder(object):
    """
    Value object for children orders. Child orders are those orders derived
    from strategy orders. In the trade execution process, order optimizers
    would slice the original strategy order into pieces into order to minimize
    market  impact. The child order would also be more substantial by
    specifying the type of order (market or limit order) to be executed in
    direct market access.

    soid: reference to the strategy order that this child order belongs to.
    coid: the sequence number of children orders under a strategy order.
    timestamp: the time which this child order is submitted to execute.
    symbol: the instrument that we trade.
    action: buy or sell, use the global constant.
    qty: the number of contracts that we trade.
    ordertype: limit order or market order, use the global constant.
    limitprice: the limit price for limit order.
    """

    def __init__(self, soid, coid, timestamp, symbol, action, qty, endtime, ordertype,
                 limitprice=None):
        self._soid = soid
        self._coid = coid
        self._timestamp = timestamp
        self._symbol = symbol
        self._action = action
        self._qty = qty
        self._ordertype = ordertype
        self._limitprice = limitprice
        self._endtime = endtime

    def get_soid(self):
        return self._soid

    def get_coid(self):
        return self._coid

    def get_timestamp(self):
        return self._timestamp

    def get_symbol(self):
        return self._symbol

    def get_action(self):
        return self._action

    def get_qty(self):
        return self._qty

    def get_ordertype(self):
        return self._ordertype

    def get_limitprice(self):
        return self._limitprice

    def get_endtime(self):
        return self._endtime


class FilledOrder(object):
    """
    Value object for order fulfillment. Order fulfillment is the information
    passed from the live or paper-traded direct market access module. For a
    child order submitted to DMA, it may be executed partially at different
    times. That's why the executed quantity and price can be different from
    the child order that an order fulfillment referred to.

    soid: reference to the strategy order that this child order belongs to.
    coid: reference to the child order that this order fulfillment belongs to.
    foid: the sequence number of this order fulfillment under a child order.
    timestamp: the time which the partial child order is executed.
    symbol: the instrument that we trade.
    action: buy or sell, use the global constant.
    qty: the partial number of contracts that is executed.
    price: the price that the partial child order is executed.
    market_impact: the estimated market impact that is associated with this
                   execution.
    """
    def __init__(self, soid, coid, foid, timestamp, symbol, action, qty, price, market_impact):
        self._soid = soid
        self._coid = coid
        self._foid = foid
        self._timestamp = timestamp
        self._symbol = symbol
        self._action = action
        self._qty = qty
        self._price = price
        self._market_impact = market_impact

    def get_soid(self):
        return self._soid

    def get_coid(self):
        return self._coid

    def get_foid(self):
        return self._foid

    def get_timestamp(self):
        return self._timestamp

    def get_symbol(self):
        return self._symbol

    def get_action(self):
        return self._action

    def get_qty(self):
        return self._qty

    def get_price(self):
        return self._price

    def get_market_impact(self):
        return self._market_impact
