# pcost.py
#
# Exercise 1.30

def portfolio_cost(filename):
	total_cost = 0.0

	f = open(filename)
	headers = next(f)
	for line in f:
		line.strip()
		row = line.split(',')
		total_cost = total_cost + int(row[1]) * float(row[2])
	f.close()
	return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost ',f'{cost:10.2f}')
