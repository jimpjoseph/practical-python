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


