# fmpclient
A FinancialModellingPrep API wrapper.
FMPClient supports the `Company Valuation`, `Stock Time Series`, `Stock Market`, `Cryptocurrencies` and `Forex` APIs.

## Requirements
Python 3 is supported for this binding.

This package relies on the third-party depency - requests.

## Installation
To install the latest stable release with pip
```sh
$ pip install fmpclient
```

## Running the Tests
TODO

## Importing the Module
To import the module:
```python
import fmpclient
```

Alternatively you can just import the class:
```python
from fmpclient import FMPClient
```

## Quick Start
To query the FinancialModellingPrep (FMP) API you can construct the API client and make calls like so:
```python
from fmpclient import FMPClient
api = FMPClient()

tickers=['GOOG']
api.company_valuation.income_statement(tickers)
```

A API call would return JSON like so:
```python
>>> api.company_valuation.income_statement(tickers)
{'AAPL': {'Revenue': {'2014-09': '182795', '2015-09': '233715', '2016-09': '215639', '2017-09': '229234', '2018-09': '265595', 'TTM': '261612'}, 'Cost of revenue': {'2014-09': '112258', '2015-09': '140089', '2016-09': '131376', '2017-09': '141048', '2018-09': '163756', 'TTM': '161654'}, 'Gross profit': {'2014-09': '70537', '2015-09': '93626', '2016-09': '84263', '2017-09': '88186', '2018-09': '101839', 'TTM': '99958'}, 'Research and development': {'2014-09': '6041', '2015-09': '8067', '2016-09': '10045', '2017-09': '11581', '2018-09': '14236', 'TTM': '14731'}, 'Sales, General and administrative': {'2014-09': '11993', '2015-09': '14329', '2016-09': '14194', '2017-09': '15261', '2018-09': '16705', 'TTM': '17257'}, 'Total operating expenses': {'2014-09': '18034', '2015-09': '22396', '2016-09': '24239', '2017-09': '26842', '2018-09': '30941', 'TTM': '31988'}, 'Operating income': {'2014-09': '52503', '2015-09': '71230', '2016-09': '60024', '2017-09': '61344', '2018-09': '70898', 'TTM': '67970'}, 'Interest Expense': {'2014-09': '384', '2015-09': '733', '2016-09': '1456', '2017-09': '2323', '2018-09': '3240', 'TTM': '3396'}, 'Other income (expense)': {'2014-09': '1364', '2015-09': '2018', '2016-09': '2804', '2017-09': '5068', '2018-09': '5245', 'TTM': '5205'}, 'Income before taxes': {'2014-09': '53483', '2015-09': '72515', '2016-09': '61372', '2017-09': '64089', '2018-09': '72903', 'TTM': '69779'}, 'Provision for income taxes': {'2014-09': '13973', '2015-09': '19121', '2016-09': '15685', '2017-09': '15738', '2018-09': '13372', 'TTM': '10348'}, 'Net income from continuing operations': {'2014-09': '39510', '2015-09': '53394', '2016-09': '45687', '2017-09': '48351', '2018-09': '59531', 'TTM': '59431'}, 'Net income': {'2014-09': '39510', '2015-09': '53394', '2016-09': '45687', '2017-09': '48351', '2018-09': '59531', 'TTM': '59431'}, 'Net income available to common shareholders': {'2014-09': '39510', '2015-09': '53394', '2016-09': '45687', '2017-09': '48351', '2018-09': '59531', 'TTM': '59431'}, 'Basic': {'2014-09': '6086', '2015-09': '5753', '2016-09': '5471', '2017-09': '5217', '2018-09': '4955', 'TTM': '4861'}, 'Diluted': {'2014-09': '6123', '2015-09': '5793', '2016-09': '5500', '2017-09': '5252', '2018-09': '5000', 'TTM': '4904'}, 'EBITDA': {'2014-09': '61813', '2015-09': '84505', '2016-09': '73333', '2017-09': '76569', '2018-09': '87046', 'TTM': '84728'}}}
```