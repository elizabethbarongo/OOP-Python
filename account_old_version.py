class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []
        self.loan = 0
        self.frozen = False
        self.min_balance = 0
        self.withdrawals=[]
        self.closed=False

    def deposit(self, amount):
          if amount > 0:
             self.balance += amount
             self.transactions.append(f"Deposited {amount}")
             return f"Deposited {amount}. New balance is {self.balance}"


    def withdraw(self, amount):
        if self.frozen:
            return f"Withdrawal failed: Account '{self.name}' is frozen."

        if amount <= 0:
            return f"Withdrawal failed: Invalid amount {amount}."

        if self.balance - amount < self.min_balance:
            return (f"Withdrawal failed: Minimum balance of {self.min_balance} must be maintained. "
                    f"Current balance: {self.balance}")

        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")
        return f"Withdrew {amount}. New balance: {self.balance}"

    


    def transfer_funds(self, other_account, amount):
        result = self.withdraw(amount)

        if self.withdraw(amount).startswith("Withdrew"):
             other_account.deposit(amount)
             self.transactions.append(f"Transferred {amount} to {other_account.name}")
             return f"Transferred {amount} to {other_account.name}"
        else:
            return f"Transfer failed: {result}"


    def show_balance(self):
        return f"{self.name} balance: {self.balance}"

    def show_transactions(self):
        return f"{self.name} transactions: "+",".join(self.transactions)

    def request_loan(self, amount):
          self.balance += amount
          self.transactions.append(f"Loan received: {amount}")
          return f"Loan of{amount} granted. New balance: {self.balance}"

    def repay_loan(self,amount):
        if amount <0:
            return f"Repayment failed: Invalid amount{amount}"
        if amount > self.balance:
            return f"Repayment failed: Not enough money to repay{amount}"
        self.balance-= amount
        self.transactions.append(f"Loan repaid:{amount}")
        return f"Loan of {amount} repaid. New balance: {self.balance}" 

    def view_account_details(self):
         return f"Name: {self.name}, Balance: {self.balance}" 

    def change_account_owner(self, new_name):
         self.name = new_name
         return f"Account owner changed to {self.name}"

    def account_statement(self):
        return f"{self.name} Balance: {self.balance}, Transactions:{self.transactions}" 

    def calculate_interest(self,rate,time):
        interest = (self.balance * rate * time) /100
        return f"Interest on {self.balance} at {rate}% for {time} yaers is {interest}"

    def freeze_account(self):
        self.frozen = True
        return f"Account for {self.name} has been frozen"

    def set_minimum_balance(self,amount):
        self.minimum_balance = amount
        return f"Minimum balance set to {self.minimum_balance}"

    def close_account(self):
        self.balance = 0
        self.closed = True
        print  (f"Account closed for {self.name}")

    


   
        
                





        
       

        
    

