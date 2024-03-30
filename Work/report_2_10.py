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
		for row in rows:
			try:
				holding = {
					'name' : row[0],
					'shares': int(row[1]),
					'price': float(row[2])
				}
				portfolio.append(holding)
			except ValueError:
				print("Couldn't parse", row)
	return portfolio


def make_report(portfolio, prices):
	report = []
	for p in portfolio:
		r = (p['name'], p['shares'],prices[p['name']], prices[p['name']] - p['price'] )
		report.append(r)
	return report

def compute_profit(portfolio, prices):
	profit = 0.0
	for p in portfolio:
		profit += p['shares']*(prices[p['name']] - p['price'])
	return profit

#if len(sys.argv) == 2:
#	filename = sys.argv[1]
#else:
#	filename = 'Data/portfolio.csv'
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

print('Profile(Loss) ', compute_profit(portfolio,prices))
report = make_report(portfolio, prices)
for name, shares, price, change in report:
	print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
