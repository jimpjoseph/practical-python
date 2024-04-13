#!/usr/bin/env python3
# pcost.py
#
# Exercise 6.2
import sys
from report_3_16 import read_portfolio

def main(argv):
	if len(argv) != 2:
		raise SystemExit(f'Usage: {sys.argv[0]}' ' portfile')
	print('Total cost ',f'{portfolio_cost(sys.argv[1])}')

def portfolio_cost(filename):
	cost = 0.0
	portfolio = read_portfolio(filename)
	return portfolio.total_cost




if __name__ == '__main__':
	import sys
	main(sys.argv)