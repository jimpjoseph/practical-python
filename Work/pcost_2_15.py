# pcost.py
#
# Exercise 1.33
import csv
import sys

def portfolio_cost(filename):
	total_cost = 0.0

	with open(filename) as f:
		rows = csv.reader(f)
		headers = next(rows)
		for rowno, row in enumerate(rows):
			try:
				total_cost = total_cost + int(row[1]) * float(row[2])
			except ValueError:
				print(f'Row {rowno}: Bad row: {row}')
	return total_cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost ',f'{cost:10.2f}')
