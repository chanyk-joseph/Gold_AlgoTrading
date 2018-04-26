CALL = 11
PUT = 12


class DataProvider(object):
    """
    Superclass for market data provider. The implementation will be responsible for
    1. querying contracts' specification;
    2. retrieving historical bar data for different symbol types, like index, future, option, etc.
    """

    def __init__(self, config):
        """
        Initiate the cache if necessary.

        config: the global configuration object, may help you to retrieve other modules or tell
        you the details of the project.
        """

    def list_contract_maturities(self, asset_code, timestamp):
        """
        List the available maturities for future and option of an asset, given a time point.

        asset_code: the code for a commodity, forex, equity, or index. E.g. GC for COMEX gold.
        timestamp: the time point at which to query the available contract's maturity

        return: a list of date object representing the settlement date of the contracts or an
                empty list
        """
        pass

    def list_option_strikes(self, asset_code, maturity, type):
        """
        List the available strike prices for call or put option of an asset, given the contract
        maturity.

        asset_code: the code for a commodity, forex, equity, or index. E.g. GC for COMEX gold.
        maturity: a date object representing the contract's maturity
        type: call or put option

        return: a list of strike prices or an empty list
        """
        pass

    def get_index(self, config, asset_code):
        """
        Retrieve the symbol object for an index, equity, commodity spot, or currency etc.

        config: the global configuration object, may help you to retrieve other modules or tell
                you the details of the project.
        asset_code: the code for a commodity, forex, equity, or index. E.g. GC for COMEX gold.

        return: the Symbol object, you may further access to detail specification and historical
                market data from that.
        """
        pass

    def get_future(self, config, asset_code, maturity):
        """
        Retrieve the symbol object for a future contract of an asset.

        config: the global configuration object, may help you to retrieve other modules or tell
                you the details of the project.
        asset_code: the code for a commodity, forex, equity, or index. E.g. GC for COMEX gold.
        maturity: the date object enquired from list_contract_maturities function

        return: the Symbol object, you may further access to detail specification and historical
                market data from that.
        """
        pass

    def get_option(self, config, asset_code, maturity, strike, type):
        """
        Retrieve the symbol object for an call or put option of an asset.

        config: the global configuration object, may help you to retrieve other modules or tell
                you the details of the project.
        asset_code: the code for a commodity, forex, equity, or index. E.g. GC for COMEX gold.
        maturity: the date object enquired from list_contract_maturities function
        strike: the strike price enquired from list_option_strikes function
        type: call or put option

        return: the Symbol object, you may further access to detail specification and historical
                market data from that.
        """
        pass

    def get_symbol(self, config, sybmbol_code):
        pass

    def get_risk_free_interest(self, date, maturity):
        """
        Retrieve the risk free interest rate for financial modelling.

        date: the date object for which the rate quoted on.
        maturity: the maturity on the yield curve.

        return: the annual risk free interest rate for the term. e.g. 1.2% pa is 0.012
        """
        pass


