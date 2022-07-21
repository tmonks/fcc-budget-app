import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        text = self.name.center(30, "*") + "\n"

        for item in self.ledger:
            text += self.__format_ledger_item(item)

        text += f"Total: {self.get_balance()}"

        return text

    def __format_ledger_item(self, item):
        """ formats a ledger item for printing with a total width of 30 characters """

        description = item['description'][0:23].ljust(23)
        amount = f"{item['amount']:.2f}".rjust(7)
        return description + amount + "\n"

    def deposit(self, amount, description=""):
        """ creates a positive ledger item with amount and description """
        deposit = {'amount': amount, 'description': description}
        self.ledger.append(deposit)

    def check_funds(self, amount):
        """ Returns True if the current funds are enough to cover the `amount`, otherwise False """
        return self.get_balance() >= amount

    def get_balance(self):
        """ returns the current balance of the Category """
        return sum([x['amount'] for x in self.ledger])

    def withdraw(self, amount, description=""):
        """ 
        creates a positive ledger item with amount and description 
        returns False if there is not enough funds
        """

        if not self.check_funds(amount):
            return False
        withdrawal = {'amount': amount * -1, 'description': description}
        self.ledger.append(withdrawal)
        return True

    def transfer(self, amount, to_category):
        """
        transfers `amount` from the current Category to the `to_category`
        creates a withdrawal in the current Category and a corresponding deposit in the `to_category`
        """

        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {to_category.name}")
        to_category.deposit(amount, f"Transfer from {self.name}")
        return True

    def get_spend(self):
        """ gets the total of all the withdrawals """
        return sum(li['amount'] for li in self.ledger if li['amount'] < 0) * -1


def bar_chart_row(row_percent, percentages):
    """
    returns a bar chart row for the given `row_percent` (0 - 100) and list of percentages
    will print a `o` for each of the `percentages` that is at least `row_percent`
     """

    row = str(row_percent).rjust(3) + "| "
    for p in percentages:
        if (p * 100) > row_percent:
            row += "o  "
        else:
            row += "   "
    return row


def get_spend_percentages(categories):
    """ 
    takes a list of categories and returns a list of relative percentages 
    representing the proportion spent on each category 
    """

    amounts_spent = [c.get_spend() for c in categories]
    total_amount_spent = sum(amounts_spent)

    return [amt / total_amount_spent for amt in amounts_spent]


def create_bar_chart_rows(categories):
    """ returns a list of the bar chart rows for the specified categories from 100 to 0 """
    percentages = get_spend_percentages(categories)
    return [bar_chart_row(i, percentages) for i in range(100, -10, -10)]


def key_row(place, names):
    """ formats a row of the key for the given place in the category names """
    row = "     "
    for name in names:
        row += name[place] + "  "
    return row


def create_key_rows(categories):
    """ 
    returns a list of rows forming a key for the bar chart with the names
    of the specified categories printed vertically from top to bottom
    """

    names = [c.name for c in categories]
    max_length = max([len(name) for name in names])
    names = [name.ljust(max_length) for name in names]

    return [key_row(place, names) for place in range(0, max_length)]


def create_spend_chart(categories):
    """
    creates an ASCII bar chart representing the relative percentages spent 
    in each of the specified categories 
    """

    rows = ["Percentage spent by category"]
    rows += create_bar_chart_rows(categories)
    rows.append("    -" + "-" * (3 * len(categories)))
    rows += create_key_rows(categories)

    return "\n".join(rows)
