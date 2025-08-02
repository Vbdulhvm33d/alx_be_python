# creating an account balance class with some functionalities

class BankAccount:

    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        #this line houses the code 
        if amount > 0:
            self.__account_balance += amount
            print(f"you've successfully deposited ${amount}")
        else:
            print("please enter a positive amount")

    def withdraw(self, amount):
        #this code houses the code
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"withdrawal of ${amount} successful.")
            return True
        
        elif amount > self.__account_balance:
            print(f"insufficient funds!")
            return False
             
    def display_balance(self):
        return self.__account_balance

#my_acct = BankAccount(0)
#my_acct.deposit(100)
#my_acct.withdraw(49)
#my_acct.display_balance()
