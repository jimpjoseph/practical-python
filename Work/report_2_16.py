# pcost.py
#
# Exercise 1.33
import csv
import sys


def read_prices(filename):
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


def read_portfolio(filename):
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


def make_report(portfolio, prices):
	report = []
	for p in portfolio:
		r = (p['name'], ['shares'],prices[p['name']], prices[p['name']] - p['price'] )
		report.append(r)
	return report

def compute_profit(portfolio, prices):
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
for r in report:
	print(r)
