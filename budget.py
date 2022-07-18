class Category:

	ledger = []
	name = ""

	def __init__(self, name):
		self.name = name	
		print(self.name, "constructed")

	def deposit(self, amount, description):
		deposit = {'amount': amount, 'description': description}
		self.ledger.append(deposit)

	def get_balance(self):
		return self.ledger


# def create_spend_chart(categories):


food = Category("Food")
food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(food)
# print(clothing)