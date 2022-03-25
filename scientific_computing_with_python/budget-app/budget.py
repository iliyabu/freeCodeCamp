from math import floor


class Category:
    def __str__(self):
        budget_object = ""
        budget_object += self.budget_category.center(30, '*') + "\n"
        for item in self.ledger:
            amount_string = f"{item['amount']:.2f}"
            budget_object += f"{item['description'][:23].ljust(23)}{amount_string[:7].rjust(7)}\n"
        budget_object += f"Total: {self.get_balance():.2f}"
        return budget_object

    def __init__(self, budget_category):
        self.budget_category = budget_category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(list(map(lambda x: x['amount'], self.ledger)))

    def get_withdraws(self):
        return -sum(list(map(lambda x: x['amount'] if x['amount'] < 0 else 0, self.ledger)))

    def transfer(self, amount, another_budget_category):
        if self.withdraw(amount, f"Transfer to {another_budget_category.budget_category}"):
            another_budget_category.deposit(amount, f"Transfer from {self.budget_category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return self.get_balance() >= amount


def create_spend_chart(categories):
    chart = ""
    categories_withdraws = list(map(lambda x: x.get_withdraws(), categories))
    categories_withdraws = list(map(lambda x: floor(10 * x / sum(categories_withdraws)), categories_withdraws))

    chart += "Percentage spent by category\n"

    for i in range(10, -1, -1):
        percent = f"{i}0| ".rjust(5) if i > 0 else f"{i}| ".rjust(5)
        bars = ""
        for category in categories_withdraws:
            if category >= i:
                bars += "o  "
            else:
                bars += "   "

        chart += f"{percent}{bars}\n"

    chart += f"    -" + "---" * len(categories) + "\n"

    max_category = max(list(map(lambda x: len(x.budget_category), categories)))
    for i in range(max_category):
        legend = ""
        for category in categories:
            if len(category.budget_category) > i:
                legend += f"{category.budget_category[i]}  "
            else:
                legend += "   "
        chart += f"     {legend}\n"
    chart = chart.rstrip()
    return chart + "  "
