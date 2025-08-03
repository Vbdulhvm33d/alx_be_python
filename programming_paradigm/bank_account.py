# creating an account balance class with some functionalities

class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.1f}")
        else:
            print("please enter a positive amount")
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True
        else:
            print(f"Insufficient funds.")
            return False       
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.1f}")