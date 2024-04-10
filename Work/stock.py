class Stock():
	"""docstring for Stock"""
	def __init__(self, name, shares, price):
		self.name = name
		self.shares = shares
		self.price = price

	def __repr__(self):
		return "Stock('" + self.name + "', " + str(self.shares) + ', ' + str(self.price) + ')'

	def cost(self):
		return self.shares * self.price

	def sell(self, amt):
		self.shares -= amt
