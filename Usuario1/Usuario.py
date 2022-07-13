
class Usuario:
    def __init__(self, name):
        self.name = name
        self.balance_account = 0

    def make_deposit(self, amount):
        self.balance_account += amount
        return self

    def make_withdraw(self, amount):
        self.balance_account -= amount
        return self

    def show_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance_account}.")
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdraw(amount)
        other_user.make_deposit(amount)
        self.show_balance()
        other_user.show_balance()
        return self




