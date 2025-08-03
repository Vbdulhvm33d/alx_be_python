# creating an account balance class with some functionalities

class BankAccount:

    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        #this line houses the code 
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited ${amount}")
        else:
            print("please enter a positive amount")

    def withdraw(self, amount):
        #this code houses the code
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew ${amount}")
            return True
        
        elif amount > self.account_balance:
            print(f"Insufficient funds.")
            return False
             
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

my_acct = BankAccount(0)
#my_acct.deposit(100)
my_acct.withdraw(49)
my_acct.display_balance()
