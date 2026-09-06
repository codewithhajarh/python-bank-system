class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
            return False
        elif amount > self.balance:
            print("Insufficient funds.")
            return False
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -{amount}")
            return True
    def transfer(self, other_account, amount):
        if other_account.owner == self.owner :
            print("Invalid account")
        elif amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            other_account.balance += amount
            self.transactions.append(f"Transfer to {other_account.owner}: -{amount}")
            other_account.transactions.append(f"Transfer from {self.owner}: +{amount}")
            print("Transfer is successful!")
    def check_balance(self):
        print(f"Current balance: {self.balance}")
    def show_transactions(self):
        print("========== TRANSACTIONS ==========")
        print("")
        if len(self.transactions) > 0:
            for i in range(len(self.transactions)):
                print(f"{self.transactions[i]}\n")
        else:
            print("No transations yet!")
        print("")
        print("==================================")

class SavingAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance = (1 + self.interest_rate) * self.balance
    def withdraw(self, amount):
        if amount > 500:
            print("Savings account withdrawal limit is 500.")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            super().withdraw(amount)

class CheckingAccount(Account):
    def __init__(self, owner, balance, transaction_fee):
        super().__init__(owner, balance)
        self.transaction_fee = transaction_fee
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount + self.transaction_fee > self.balance :
            print("Invalid amount!")
        else:
            if super().withdraw(amount):
                self.balance -= self.transaction_fee
                self.transactions.append(f"Withdrawal fee: -{self.transaction_fee}")

