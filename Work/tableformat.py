# tableformat.py

class TableFormatter:
	def headings(self, headers):
		'''
		Emit the table headings.
		'''
		raise NotImplementedError()

	def row(self, rowdata):
		'''
		Emit a single row of table data.
		'''
		raise NotImplementedError()


class TextTableFormatter(TableFormatter):
	def headings(self, headers):
		'''
		Emit the table headings.
		'''
		for h in headers:
			print(f'{h:>10s}', end=' ')
		print()
		print(('-' * 10 + ' ') * len(headers))

	def row(self, rowdata):
		'''
		Emit a single row of table data.
		'''
		for d in rowdata:
			print(f'{d:>10s}', end=' ')
		print()

class CSVTableFormatter(TableFormatter):
	def headings(self, headers):
		'''
		Emit the table headings.
		'''
		print(','.join(headers))

	def row(self, rowdata):
		'''
		Emit a single row of table data.
		'''
		print(','.join(rowdata))



class HTMLTableFormatter(TableFormatter):
	def headings(self, headers):
		'''
		Emit the table headings.
		'''
		print('<tr>',end='')
		for h in headers:
			print('<th>'+h, end='</th>')
		print('</tr>')
		

	def row(self, rowdata):
		'''
		Emit a single row of table data.
		'''
		print('<tr>',end='')
		for d in rowdata:
			print('<td>'+d, end='</td>')
		print('</tr>')

def create_formatter(fmt):
	if fmt == 'txt':
		formatter = TextTableFormatter()
	elif fmt == 'csv':
		formatter = CSVTableFormatter()
	elif fmt == 'html':
		formatter = HTMLTableFormatter()
	else:
		raise RuntimeError(f'Unknown format {fmt}')
	return formatter

def print_table(rows, headers, formatter): 
	formatter.headings(headers)
	for row in rows:
 		rowData = []
 		for h in headers:
 			rowData.append(str(getattr(row,h)))
 		formatter.row(rowData)
