from datetime import datetime
class Transactions:
    def __init__(self,narration,amount,transaction_type):
        self.amount=amount
        self.narration=narration
        self.transaction_type=transaction_type
        self.date_time=datetime.now()
    def __repr__(self):
        return f"{self.date_time}-{self.transaction_type}:{self.narration} of ${self.amount:.2f}"
class Account:
    def __init__(self,name,account_number):
        self.name=name
        self.account_number=account_number
        self._balance= 0
        self.transaction=[]
        self.minimum_balance=0
    def deposit(self,amount):
        if amount<=0:
            return "Deposit amount must be positive"
        self._balance +=amount
        self.transaction.append(Transactions("Deposit",amount,"Credit"))
        return f"confirmed,you have deposited ${amount}.new balance is ${self.get_balance():.2f}"
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self._balance - self.minimum_balance:
                return "Insufficient funds for this withdrawal."
        self._balance -= amount
        self.transaction.append(Transactions("Withdrawal", amount, "Debit"))
        return f"Confirmed: You have withdrawn ${amount}. New balance is ${self.get_balance():.2f}"
    def  get_balance(self):
        return self._balance
    def view_transaction(self):
        return "\n".join(str(transaction) for transaction in self.transaction )
    def change_account_owner(self,new_name):
        self.name=new_name
        return  f"Account owner changed to  ${self.name}"
    def  set_minimum_balance(self, amount):
        if amount <0:
            return "minimum balance must be positive"
        self.minimum_balance = amount
        return f"minimum balance set to  ${self.minimum_balance:.2f}"
    def close_account(self):
        self.balance=0
        self.transaction.clear()
        return "Account closed .All balances and transactions have been reset."
