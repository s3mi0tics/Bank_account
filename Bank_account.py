class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance<0:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate*self.balance
        else:
            print("no yield due to negitive account balance")
        return self

a54321 = BankAccount()
a98765 = BankAccount()

a54321.deposit(500).display_account_info().yield_interest().display_account_info()

#a54321.deposit(500).deposit(700).deposit(900).withdraw(850).display_account_info().yield_interest().display_account_info()

a54321.withdraw(1000).display_account_info().yield_interest().display_account_info()

