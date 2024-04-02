# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename: str, select = None, types = None, has_headers = True, delimiter = ',') -> list:
	'''
	Parse a CSV file into a list of records
	'''
	with open(filename) as f:
		rows = csv.reader(f, delimiter=delimiter)

		#Read the file headers
		if has_headers:
			headers = next(rows)

		if select and has_headers:
			indices = [headers.index(colname) for colname in select]
			headers = select
		else:
			indices = []

		records = []
		for row in rows:
			if not row: 	#Skip rows with no data
				continue
			if types:
				row = [func(val) for func, val in zip(types, row)]

			if indices:
				row = [ row[index] for index in indices]

			if has_headers:
				record = dict(zip(headers, row))
				records.append(record)
			else:
				records.append(tuple(row))

	return records

