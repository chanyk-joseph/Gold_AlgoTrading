ONE_SECOND = 10
ONE_MINUTE = 11
FIVE_MINUTE = 12
ONE_HOUR = 13
ONE_DAY = 14
ONE_WEEK = 15
ONE_MONTH = 16

OPEN_BID = 'Open_Bid'
OPEN_ASK = 'Open_Ask'
LAST_BID = 'Last_Bid'
LAST_ASK = 'Last_Ask'
OPEN_PRICE = 'Open_Price'
HIGH_PRICE = 'High_Price'
LOW_PRICE = 'Low_Price'
CLOSE_PRICE = 'Close_Price'
VOLUME = 'Volume'

class Symbol(object):
    """
    Representation an index, contracts, currency, interest rate, asset spot in the trading
    system, for which time series data like prices, bid, ask, volume are attached to.
    """

    def __init__(self, config, symbol_code):
        """
        Initiate the cache if necessary.

        config: the global configuration object, may help you to retrieve other modules or tell
                you the details of the project.
        symbol_code: a code representing the symbol
        """
        pass

    def get_hist_data(self, start_datetime, end_datetime, bar_size, fields):
        """
        Retrieve the historical bar data for the symbol.

        start_datetime: the start datetime of the historical bar data
        end_datetime: the end datetime of the historical bar data
        bar_size: the size of each bar, e.g. 1 minute, 5 minutes, 1 hour
        fields: a list fields to return, select values from the global variables.

        return: a pandas Dataframe object with the columns specified in fields. each row is a bar.
            1. symbol_code
            2. timestamp
            3. fields[1]
            ...
        """
        pass

    def get_symbol_code(self):
        pass
