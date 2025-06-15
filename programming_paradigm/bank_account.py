class BankAccount:
    """A simple bank account class with deposit, withdraw, and and display balance"""

    def __init__(self, initial_balance=0):
        """Initialize account balnce with an optional starting amount (default: 0)."""
        self.__account_balance = initial_balance # encapsulated balance

    def deposit(self, amount):
        """add a specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """deduct the specified amount if the funds are sufficient"""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """print the current balance in a user friendly format"""
        print(f"Current Balance: ${self.__account_balance}")