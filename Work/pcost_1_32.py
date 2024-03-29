# pcost.py
#
# Exercise 1.30
import csv

def portfolio_cost(filename):
	total_cost = 0.0

	f = open(filename)
	rows = csv.reader(f)
	headers = next(rows)
	for row in rows:
		try:
			total_cost = total_cost + int(row[1]) * float(row[2])
		except ValueError:
			print("Couldn't parse", row)
	f.close()
	return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost ',f'{cost:10.2f}')
