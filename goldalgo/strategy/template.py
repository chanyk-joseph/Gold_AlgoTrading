import numpy as np
import datetime as dt
class Strategy(object):
    """
    Representation of a trading strategy in the trading system. A strategy will
    delegate to its own market analyzer to generate a market view for decision.
    Upon a signal is generated, it will create the corresponding current or
    future strategy orders.
    """

    def __init__(self):
        """
        Implementations should initiate their own states, e.g. a map for their
        pending strategy orders.
        """
        pass

    def get_name(self):
        """
        Returns the name of an implementation. For debug or logging.
        """
        return self._name

    def generate_orders(self, config, timestamp):
        """
        This is the entrance to your strategy. Given the timestamp of the
        project's main loop, you should do whatever possible to check if you
        can generate some signal and the corresponding current or future
        strategy orders at this point time.

        config: you may access to the market data provider by this object.
        timestamp: the time point you assume where the back-test state is.

        returns:  to be processed immediately or just
                 an empty array.
        """
        raise NotImplementedError