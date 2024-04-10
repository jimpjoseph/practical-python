# report_3.py
#
# Exercise 3
from fileparse import parse_csv
import stock
import tableformat

def read_prices(filename: str) -> dict:
	'''
	Read prices from a CSV file of name, string data
	'''
	with open(filename) as f:
		pricelist = parse_csv(f,types=[str,float], has_headers=False)
		prices = dict(pricelist)
		return prices


def read_portfolio(filename: str) -> list:
	'''
	Read portfolio information name, shares, from from a CSV file of 
	name, shares and pricedata
	'''
	with open(filename) as f:
		portdicts = parse_csv(f,select=['name','shares','price'], types=[str,int,float])
		portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
		return portfolio


def make_report(portfolio: dict, prices: list) -> list:
	'''
	Makes a report based on portfolio and price data
	'''
	report = []
	for p in portfolio:
		r = (p.name, p.shares,prices[p.name], prices[p.name] - p.price )
		report.append(r)
	return report

def compute_profit(portfolio: dict, prices: list) -> float:
	'''
	Computes profit or loss based on portfolio and current prices
	'''
	profit = 0.0
	for p in portfolio:
		profit += p.shares*(prices[p.name] - p['price'])
	return profit

def print_report(report: list, formatter):
 	'''
 	Prints report based on the report.
 	'''
 	formatter.headings(['Name', 'Shares', 'Price', 'Change'])
 	#print('%10s %10s %10s %10s'  % headers)
 	#print(('-' * 10 + ' ') * len(headers))
 	for name, shares, price, change in report:
 		pr = "${:.2f}".format(price)
 		rowData = [name, str(shares), pr, f'{change:0.2f}']
 		formatter.row(rowData)
 		#print(f'{name:>10s} {shares:>10d} {pr:>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename: str, prices_filename: str,fmt='txt'):
	'''
	Master function to generate the portolio.
	'''
	portfolio = read_portfolio(portfolio_filename)
	prices = read_prices(prices_filename)
	report = make_report(portfolio, prices)
	if fmt == 'txt':
		formatter = tableformat.TextTableFormatter()
	elif fmt == 'csv':
		formatter = tableformat.CSVTableFormatter()
	elif fmt == 'html':
		formatter = tableformat.HTMLTableFormatter()
	else:
		raise RuntimeError(f'Unknown format {fmt}')
	print_report(report, formatter)

def main(argv):
	if len(argv) != 4:
		raise SystemExit(f'Usage: {sys.argv[0]}' ' portfile pricefile fmt')

	portfile = argv[1]
	pricefile = argv[2]
	fmt = argv[3]
	#print(portfile, pricefile, fmt)
	portfolio_report(portfile, pricefile, fmt)

if __name__ == '__main__':
	import sys
	main(sys.argv)



