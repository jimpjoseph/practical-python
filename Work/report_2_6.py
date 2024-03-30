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


if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'
portfolio = read_portfolio(filename)
print('Portfolio ', portfolio)
