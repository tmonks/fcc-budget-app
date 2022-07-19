class Category:
	def __init__(self, name):
		self.name = name	
		self.ledger = []
		print(self.name, "constructed")

	def deposit(self, amount, description):
		deposit = {'amount': amount, 'description': description}
		self.ledger.append(deposit)

	def check_funds(self, amount):
		return self.get_balance() >= amount

	def get_balance(self):
		return sum([x['amount'] for x in self.ledger])

	def withdraw(self, amount, description=""):
		if not self.check_funds(amount):
			return False
		withdrawal = {'amount': amount * -1, 'description': description}
		self.ledger.append(withdrawal)
		return True

	def transfer(self, amount, to_category):
		if not self.check_funds(amount):
			return False
		self.withdraw(amount, f"Transfer to {to_category.name}")
		to_category.deposit(amount, f"Transfer from {self.name}")

# def create_spend_chart(categories):


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

# print(food)
# print(clothing)