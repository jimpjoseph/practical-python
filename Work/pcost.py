# pcost.py
#
# Exercise 1.27

total_count = 0.0

f = open('Data/portfolio.csv')
headers = next(f)
for line in f:
	line.strip()
	row = line.split(',')
	total_count = total_count + int(row[1]) * float(row[2])

f.close()
print('Total cost ',f'{total_count:10.2f}')
