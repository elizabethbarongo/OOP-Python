class Account:
    def __init__(self,name):
        self.name=name
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]


    def deposit(self,amount):
        self.deposits.append(amount)
        self.balance += amount
        return f"Hello {self.name}, you have received {amount}. Your new balance is {self.balance}"

    def withdraw(self,amount):
        if amount <= self.balance:
            self.withdrawals.append(amount)
            self.balance -= amount
            return f"Hello {self.name}, you have withdrawn {amount}. Your new balance is {self.balance}"
        else:
            return "Insufficient funds for withdrawal"    

    def get_balance(self):
        return self.balance


    def transfer(self,amount):
        self.balance = self.balance - amount
        return f"Hello {self.name}, you have sent {amount}. Your account balance is {self.balance}"


    
    def request_loan(self, amount,loan_balance):
        loan_balance = 0
        if amount > 0:
            
            loan_balance += amount
            
            print(f"Loan of ${amount} requested. Current loan balance: ${loan_balance}")
        else:
            print("Invalid loan amount") 


    def pay_loan(self, amount,loan_balance):
        loan_balance = 0
        if 0 < amount <= loan_balance:
          loan_balance -= amount
          self.balance -= amount
          print(f"Loan payment of ${amount} processed. Remaining loan balance: ${loan_balance}. New account balance: ${self.balance}")
        elif amount > loan_balance:
          print(f"Loan payment exceeds loan balance. Current loan balance: ${loan_balance}")
        else:
            print("Invalid loan payment amount.")


    def account_details(self):
        return f"Hello {self.name}. Your account balance is {self.balance}"

    
    def change_owner_name(self,new_owner_name):
        self.name == new_owner_name
        return new_owner_name


    def account_statement(self):
        return f"Hello {self.name} you deposited {sum(self.deposits)} on 28-03-2025 and withdrew {sum(self.withdrawals)} on 30-10-2026 and your account balance is {self.balance}"

    def get_interest(self,principal,time):
        rate = 0.05
        interest = principal* rate * time
        return interest



    def set_minimun_balance(self, amount):
        minimum_balance= 600
        if minimum_balance >= self.balance:
            return f"You can withdraw"
        else:
            "You cannot withdraw "    


    
            
        
    
        


   














    









            




