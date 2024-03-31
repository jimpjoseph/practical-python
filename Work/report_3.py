# report_3.py
#
# Exercise 3
import csv
import sys


def read_prices(filename: str) -> dict:
	'''
	Read prices from a CSV file of name, string data
	'''
	prices = {}

	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		for row in rows:
			if row == []:
				continue
			try:
				prices[row[0]] = float(row[1])
			except ValueError:
				print("Couldn't parse", row)
	return prices


def read_portfolio(filename: str) -> list:
	'''
	Read portfolio information name, shares, from from a CSV file of 
	name, shares and pricedata
	'''
	portfolio = []

	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for rowno, row in enumerate(rows, start = 1):
			record = dict(zip(headers, row))
			try:
				holding = {
					'name' : record['name'],
					'shares': int(record['shares']),
					'price': float(record['price'])
				}
				portfolio.append(holding)
			except ValueError:
				print(f'Row {rowno}: Bad row: {row}')
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


if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

portfolio = read_portfolio(filename)
prices = read_prices('Data/prices.csv')

print('Profile(Loss) ', compute_profit(portfolio,prices))
report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
#print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
#print(f'{'':->10s} {'':->10s} {'':->10s} {'':->10s}')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
        pr = "${:.2f}".format(price)
        print(f'{name:>10s} {shares:>10d} {pr:>10s} {change:>10.2f}')


