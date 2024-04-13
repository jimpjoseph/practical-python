class Stock():
	"""docstring for Stock"""
	__slots__ = ('name', '_shares', 'price')
	def __init__(self, name, shares, price):
		self.name = name
		self.shares = shares
		self.price = price


	@property
	def shares(self):
		return self._shares


	@shares.setter
	def shares(self, value):
		if not isinstance(value, int):
			raise TypeError('Expected int')
		self._shares = value

	def __repr__(self):
		return "Stock('" + self.name + "', " + str(self.shares) + ', ' + str(self.price) + ')'

	@property
	def cost(self):
		return self.shares * self.price

	def sell(self, amt):
		self.shares -= amt
