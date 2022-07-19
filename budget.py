class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        print(self.name, "constructed")

    def __str__(self):
        text = self.name.center(30, "*") + "\n"

        for item in self.ledger:
            text += self.__format_ledger_item(item)

        text += f"Total: {self.get_balance()}"

        return text

    def __format_ledger_item(self, item):
        description = item['description'][0:23].ljust(23)
        amount = f"{item['amount']:.2f}".rjust(7)
        return description + amount + "\n"

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

def create_spend_chart(categories):
	return "coming soon!!"
