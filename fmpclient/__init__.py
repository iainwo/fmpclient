"""
fmpclient
---------

An API wrapper for FinancialModellingPrep.

:copyright: (c) 2019 by Iain Wong.
:license: MIT< see LICENSE for details.
"""

__title__ = 'fmpclient'
__version__ = '0.1.3'
__author__ = 'Iain Wong'
__license__ = 'MIT'
__copyright__ = 'Copyright 2019 Iain Wong'

from urllib.parse import urljoin
import inspect
import requests
from datetime import date

class FMPClient(object):
    """ A FinancialModellingPrep API wrapper. """
    
    def __init__(self):
        self.requester = self.Requester()
        self._attach_endpoints()
        
    def _attach_endpoints(self):
        """ Generate and attach endpoints """
        for name, endpoint in inspect.getmembers(self):
            if (inspect.isclass(endpoint) 
                and issubclass(endpoint, self._Endpoint) 
                and endpoint is not self._Endpoint):
                endpoint_instance = endpoint(self.requester)
                setattr(self, endpoint.name, endpoint_instance)
    
    class Requester(object):
        """ An object for making API requests """
        
        def GET(self, url, params={}):
            """ Make a GET request 
            
            :param url: String. FMP endpoint.
            : param params: Dictionary. Query params to include in GET.
            """           
            params.setdefault('datatype', 'json')
            #print (f'GET: {url} with params: {params}')
            response = requests.get(url, params=params)
            if 200 != response.status_code:
                error = 'HTTPError: {}'.format(response.status_code)
                return {'success': False, 'error': error}
            try:
                return response.json()
            except ValueError as err:
                return {'success': False, 'error': err}
        
    class _Endpoint(object):
        """ Base class of an endpoint """
        url = 'https://financialmodelingprep.com/api/v3/'
        
        def __init__(self, requester):
            self.requester = requester            
        
        def _build_path(self, path, tickers):
            return path + '/' + ','.join(map(str, tickers))
        
        def _GET(self, path, tickers, params={}):
            """ Make a GET request to this endpoint
            
            :param path: String. Path to append to the endpoint url.
            :param params: Dictionary. These are query params.
            """
            path = self._build_path(path, tickers)
            request_url = urljoin(self.url, path)
            print(f'url: {self.url}, request_url: {request_url}, path: {path}')
            return self.requester.GET(request_url, params)
    
    class CompanyValuation(_Endpoint):
        """ FMP Company Profile API endpoints. """
        name = 'company_valuation'
        
        def profile(self, tickers, params={}):
            """ 
            Companies profile (Price, Beta, Volume Average, Market Capitalisation, 
            Last Dividend, 52 week range, stock price change, stock price change 
            in percentage, Company Name, Exchange, Description, Industry, Sector, 
            CEO, Website and image). 
            
            Hourly, JSON
            """
            params['datatype'] = 'json'
            return self._GET('company/profile', tickers, params)
        
        def income_statement(self, tickers, period=None, datatype='json', params={}):
            """
            Get the tickers' income statments 
            :param tickers: List. The tickers to query.
            :param period: String. The period of the income statement.
                Options: 'quarter'
            """
            if 'quarter' == period:
                params['period'] = 'quarter'
            if datatype in ['json', 'csv']:
                params['datatype'] = datatype
            return self._GET('financials/income-statement', tickers, params)
        
        def balance_sheet_statement(self, tickers, period=None, datatype='json', params={}):
            """
            Get the tickers' balance sheets
            :param tickers: List. The tickers to query.
            :param period: String. The period of the income statement.
                Options: 'quarter'
            """
            if 'quarter' == period:
                params['period'] = 'quarter'
            if datatype in ['json', 'csv']:
                params['datatype'] = datatype
            return self._GET('financials/balance-sheet-statement', tickers, params)
        
        def cash_flow_statement(self, tickers, period=None, datatype='json', params={}):
            """
            Get the tickers' cash flow statements
            :param tickers: List. The tickers to query.
            :param period: String. The period of the income statement.
                Options: 'quarter'
            """
            if 'quarter' == period:
                params['period'] = 'quarter'
            if datatype in ['json', 'csv']:
                params['datatype'] = datatype
            return self._GET('financials/cash-flow-statement', tickers, params)
        
        def financial_ratios(self, tickers, params={}):
            """
            Get the tickers' cash flow statements
            :param tickers: List. The tickers to query.
            """
            return self._GET('financial-ratios', tickers, params)
        
        def enterprise_value(self, tickers, period=None, params={}):
            """
            Get the tickers' company enterprise value
            :param tickers: List. The tickers to query.
            :param period: String. The period of the income statement.
                Options: 'quarter'
            """
            if 'quarter' == period:
                params['period'] = 'quarter'
            return self._GET('enterprise-value', tickers, params)
        
        def key_metrics(self, tickers, period=None, params={}):
            """
            Get the tickers' company key metrics
            :param tickers: List. The tickers to query.
            :param period: String. The period of the income statement.
                Options: 'quarter'
            """
            if 'quarter' == period:
                params['period'] = 'quarter'
            return self._GET('company-key-metrics', tickers, params)

        def financial_growth(self, tickers, period=None, params={}):
            """
            Get the tickers' financial growth metrics
            :param tickers: List. The tickers to query.
            :param period: String. The period of the income statement.
                Options: 'quarter'
            """
            if 'quarter' == period:
                params['period'] = 'quarter'
            return self._GET('financial-growth', tickers, params)
        
        def company_rating(self, tickers, params={}):
            """
            Get the tickers' ratings. Calculated daily.
            :param tickers: List. The tickers to query.
            """
            return self._GET('company/rating', tickers, params)
        
        def discounted_cash_flow_value(self, tickers, params={}):
            """
            Get the tickers' discounted cash flow.
            Calculated in realtime.
            :param tickers: List. The tickers to query.
            """
            return self._GET('company/discounted-cash-flow', tickers, params)
        
        def historical_discounted_cash_flow_value(self, tickers, period=None, params={}):
            """
            Get the tickers' financial growth metrics
            :param tickers: List. The tickers to query.
            :param period: String. The period of the income statement.
                Options: 'quarter'
            """
            if 'quarter' == period:
                params['period'] = 'quarter'
            return self._GET('company/historical-discounted-cash-flow', tickers, params)
    
    class StockTimeSeries(_Endpoint):
        """ FMP Stock Time Series API endpoints. """
        name = 'stock_time_series'

        def stock_realtime_price(self, tickers=[], params={}):
            """
            Get the tickers' realtime stock prices
            :param tickers: List. The tickers to query. This is optional.
                If tickers are not provided, the API request will return the realtime
                stock prices for all tickers. Can specify multiple tickers for a 
                batch request.
            """
            return self._GET('stock/real-time-price', tickers, params)

        def stock_historical_price(self, tickers, serietype=None, from_date=None, to_date=None, timeseries=0, params={}):
            """
            Get the tickers' historical stock prices.
            :param tickers: List. The tickers to query. This query accepts multiple tickers at once.
            :param serietype: String. Can be set to 'line' which will only return the historical price.
                When un-set the request will return the historical change and volume of change.
            :param from_date: Date (from datetime). Query historical data on an interval beginning on this date.
            :param to_date: Date (from datetime). Query historical data on the interval ending with this date.
            :param timeseries: int. Query historical data on an interval beginning this many days back ending now.
            """
            if 'line' == serietype:
                params['serietype'] = 'line'
            if isinstance(from_date, date) and isinstance(to_date, date):
                params['from'] = str(from_date)
                params['to'] = str(to_date)
            if 0 < timeseries:
                params['timeseries'] = timeseries
            return self._GET('historical-price-full', tickers, params)

        def symbols_list(self, params={}):
            
            """
            Get all the available tickers on FMP.
            """
            return self._GET('company/stock/list', [], params)

    class StockMarket(_Endpoint):
        """ FMP Stock Market API endpoints. """
        name = 'stock_market'

        def stock_market_index(self, indexes=[], params={}):
            """
            Get the indexes price and change.
            :param indexes: List. The tickers of the indexes to query.
                Can be empty - in which case, the request will query all indexes.
            """
            return self._GET('majors-indexes', indexes, params)

        def stock_market_actives(self, params={}):
            """
            Get the most active stocks.
            """
            return self._GET('stock/actives', [], params)

        def stock_market_gainers(self, params={}):
            """
            Get the most stocks which have gained the most.
            """
            return self._GET('stock/gainers', [], params)

        def stock_market_losers(self, params={}):
            """
            Get the most stocks which have lost the most.
            """
            return self._GET('stock/losers', [], params)

        def nyse_trading_hours(self, params={}):
            """
            Get the NYSE holiday and trading hours.
            """
            return self._GET('is-the-market-open', [], params)

        def sectors_performance(self, params={}):
            """
            Get the performance of each market sector.
            """
            return self._GET('sectors-performance', [], params)
    
    class Cryptocurrencies(_Endpoint):
        """ FMP Cryptocurrencies API endpoints. """
        name = 'cryptocurrencies'

        def cryptocurrencies(self, cryptocurrencies=[], params={}):
            """
            Get the indexes price and change.
            :param cryptocurrencies: List. The tickers of the cryptocurrencies to query.
                Can be empty - in which case, the request will query all currencies.
            """
            return self._GET('cryptocurrencies', cryptocurrencies, params)

    class Forex(_Endpoint):
        """ FMP Forex API endpoints. """
        name = 'forex'

        def foreign_exchange_rate(self, currencies=[], params={}):
            """
            Get the foreign currency exchange rates (FX).
            :param currenies: List. The tickers of the currencies to query.
                Can be empty - in which case, the request will query all currencies.
            """
            return self._GET('forex', currencies, params)