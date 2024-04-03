#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.33
import sys
from report_3_12 import read_portfolio

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = 0.0
portfolio = read_portfolio(filename)
for p in portfolio:
	cost += p['shares'] * p['price'] 

print('Total cost ',f'{cost:10.2f}')
