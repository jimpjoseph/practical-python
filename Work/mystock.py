import stock

class MyStock(stock.Stock):
	def __init__(self, name, shares, price, factor):
		super().__init__(name,shares,price)
		self.factor = factor
	def panic(self):
		self.sell(self.shares)
	def cost(self):
		actual_cost = super().cost()
		return self.factor * actual_cost