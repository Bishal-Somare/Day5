
#Description:Create a custom exception `InsufficientBalanceError` and implement a bank account system with deposit, withdrawal, and balance check functionality. The program handles errors gracefully and prevents overdraw.




class InsufficientBalanceError(Exception):
    def __init__(self, message="Insufficient balance for the transaction"):
        self.message = message
        super().__init__(self.message)

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientBalanceError()
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Account balance: {self.balance}")


account = BankAccount("John Doe", 500)
try:
    account.deposit(200)
    account.withdraw(800)
except InsufficientBalanceError as e:
    print(e)
except ValueError as e:
    print(e)
account.check_balance()

