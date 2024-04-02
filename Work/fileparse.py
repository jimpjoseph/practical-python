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

		#Select requires headers
		if select and not has_headers:
			raise RuntimeError("select argument requires column headers")

		start_no = 0
		#Read the file headers
		if has_headers:
			headers = next(rows)
			start_no = 1

		if select:
			indices = [headers.index(colname) for colname in select]
			headers = select
		else:
			indices = []

		records = []

		for lineno, row in enumerate(rows, start = start_no):
			if not row: 	#Skip rows with no data
				continue
			try:
				if types:
					row = [func(val) for func, val in zip(types, row)]

				if indices:
					row = [ row[index] for index in indices]

				if has_headers:
					record = dict(zip(headers, row))
					records.append(record)
				else:
					records.append(tuple(row))
			
			except ValueError as e:
				print(f"Row {lineno}: Couldn't covert {row}")
				print(f"Row {lineno}: Reason {e}")


	return records

