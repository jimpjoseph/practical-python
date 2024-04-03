# report_3.py
#
# Exercise 3
from fileparse import parse_csv
import sys


def read_prices(filename: str) -> dict:
	'''
	Read prices from a CSV file of name, string data
	'''
	pricelist = parse_csv(filename,types=[str,float], has_headers=False)
	prices = dict(pricelist)
	return prices


def read_portfolio(filename: str) -> list:
	'''
	Read portfolio information name, shares, from from a CSV file of 
	name, shares and pricedata
	'''
	portfolio = parse_csv(filename,select=['name','shares','price'], types=[str,int,float])
	return portfolio


def make_report(portfolio: dict, prices: list) -> list:
	'''
	Makes a report based on portfolio and price data
	'''
	report = []
	for p in portfolio:
		r = (p['name'], p['shares'],prices[p['name']], prices[p['name']] - p['price'] )
		report.append(r)
	return report

def compute_profit(portfolio: dict, prices: list) -> float:
	'''
	Computes profit or loss based on portfolio and current prices
	'''
	profit = 0.0
	for p in portfolio:
		profit += p['shares']*(prices[p['name']] - p['price'])
	return profit

def print_report(report: list):
 	'''
 	Prints report based on the report.
 	'''
 	headers = ('Name', 'Shares', 'Price', 'Change')
 	print('%10s %10s %10s %10s'  % headers)
 	print(('-' * 10 + ' ') * len(headers))
 	for name, shares, price, change in report:
 		pr = "${:.2f}".format(price)
 		print(f'{name:>10s} {shares:>10d} {pr:>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename: str, prices_filename: str):
	'''
	Master function to generate the portolio.
	'''
	portfolio = read_portfolio(filename)
	prices = read_prices('Data/prices.csv')
	report = make_report(portfolio, prices)
	print_report(report)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
	else:
		filename = 'Data/portfolio.csv'

	portfolio_report(filename, 'Data/prices.csv')



