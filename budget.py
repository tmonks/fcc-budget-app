import math


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

    def get_spend(self):
        return sum(li['amount'] for li in self.ledger if li['amount'] < 0) * -1


def get_nearest_percent(number):
    return math.floor(number * 10) * 10


def bar_chart_row(row_percent, percentages):
    row = str(row_percent).rjust(3) + "| "
    for p in percentages:
        if (p * 100) > row_percent:
            row += "o  "
        else:
            row += "   "
    return row + "\n"


def create_spend_chart(categories):
    # create bars
    amounts_spent = [c.get_spend() for c in categories]
    total_amount_spent = sum(amounts_spent)
    percentages = [amt / total_amount_spent for amt in amounts_spent]

    bar_chart = "Percentage spent by category\n"

    for i in range(100, 0, -10):
        bar_chart += bar_chart_row(i, percentages)

    # create separator
    bar_chart += "    -" + "-" * (3 * len(categories))

    # create key
    names = [c.name for c in categories]
    max_length = max([len(name) for name in names])
    names = [name.ljust(max_length) for name in names]

    return bar_chart


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
print(f"spent on food: {food.get_spend()}")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

# print(food)
# print(clothing)

print(create_spend_chart([food, clothing, auto]))
