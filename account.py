from datetime import datetime
class Transaction:
    def __init__(self, narration, amount, transaction_type):
        self.date_time = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type  
class Account:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__transactions = []
    def deposit(self, amount):
        if amount > 0:
            self.__transactions.append(Transaction("Deposit", amount, "credit"))
    def withdraw(self, amount):
        if amount > 0 and self.get_balance() >= amount:
            self.__transactions.append(Transaction("Withdrawal", amount, "debit"))
    def get_balance(self):
        balance = 0
        for t in self.__transactions:
            if t.transaction_type == "credit":
                balance += t.amount
            elif t.transaction_type == "debit":
                balance -= t.amount
        return balance
    def print_statement(self):
        print("Transaction History:")
        for t in self.__transactions:
            print(t.date_time, t.narration, t.transaction_type, t.amount)
        print("Current Balance:", self.get_balance())
