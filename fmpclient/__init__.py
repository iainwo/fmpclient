"""
fmpclient
---------

An API wrapper for FinancialModellingPrep.

:copyright: (c) 2019 by Iain Wong.
:license: MIT< see LICENSE for details.
"""

__title__ = 'fmpclient'
__version__ = '0.1.0'
__author__ = 'Iain Wong'
__license__ = 'MIT'
__copyright__ = 'Copyright 2019 Iain Wong'

from urllib.parse import urljoin
import inspect
import requests

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
        url = 'https://financialmodelingprep.com/api/v3'
        
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
            url = urljoin(self.url, path)
            return self.requester.GET(url, params)
    
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
        