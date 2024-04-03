#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.33
import sys
from report_3_16 import read_portfolio

def main(argv):
	if len(argv) != 3:
		raise SystemExit(f'Usage: {sys.argv[0]}' 'portfile pricefile')

	cost = 0.0
	portfolio = read_portfolio(filename)
	for p in portfolio:
		cost += p['shares'] * p['price'] 

	print('Total cost ',f'{cost:10.2f}')


if __name__ == '__main__':
	import sys
	main(sys.argv)