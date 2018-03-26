class Optimizer(object):
    """
    Representation of an optimizer in the trade execution process. The
    implementation should chops the strategy orders generated by a strategy
    into pieces, given the processing time limit. And it should decision the
    order type, and size for each child order. For simplicity, we are assumed
    that all quantity requested by the strategy order will be executed in the
    end within the time limit.
    """

    def __init__(self):
        """
        Implementations should initiate their own states, e.g. a map for their
        children orders execution schedule.
        """
        pass

    def get_name(self):
        """
        Returns the name of an implementation. For debug or logging.
        """
        return self._name

    def execute_strategy_orders(self, config, timestamp, orders):
        """
        This method will be triggered by the project main loop, after a list
        of strategy orders are retrieved from the strategy generator.
        Implementations should do whatever possible to chop the order into
        children orders and store the execution plan in their own state.

        config: you may access to the market data provider by this object.
        timestamp: the time point you assume where the back-test state is.
        orders: a list of strategy orders to be processed
        """
        raise NotImplementedError

    def pop_child_orders(self, timestamp):
        """
        Pop means retrieve elements and remove them from the stack. Given a
        time a point in back-test or live mode, pop the children orders to be
        executed by direct market access (DMA) immediately from execution plan.

        timestamp: the time point you assume where the back-test state is.

        returns: a list of children orders to be executed immediately or an
                 empty list.
        """
        raise NotImplementedError
