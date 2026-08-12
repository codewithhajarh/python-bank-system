import json

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

class Bank:
    def __init__(self, accounts, current_account):
        self.accounts = accounts
        self.current_account = current_account
    def create_account(self, name):
        if name in self.accounts:
            print ("Account already exists.")
        else :
            response = input("Do you have an interest rate? (Yes/No) ")
            if response == "Yes":
                try:
                    interest_rate = float(input("Enter your interest rate: "))
                    new_account = SavingAccount(name, 0.0, interest_rate)
                    self.accounts[name] = new_account
                    self.current_account = new_account
                except ValueError:
                    print("Invalid interest rate!")
            else :
                response = input("Do you have a transaction fee? (Yes/No) ")
                if response == "Yes":
                    try:
                        transaction_fee = float(input("Enter your transaction fee: "))
                        new_account = CheckingAccount(name, 0.0, transaction_fee)
                        self.accounts[name] = new_account
                        self.current_account = new_account
                    except ValueError:
                         print("Invalid transaction fee!")
                else: 
                    new_account = Account(name, 0.0)
                    self.accounts[name] = new_account
                    self.current_account = new_account
            print("Account created successfully.")
    def login(self, name):
        if name in self.accounts:
            print (f"Welcome, {name}!")
            self.current_account = self.accounts[name]
        else:
            print ("Account not found.")
            self.current_account = None
    def logout(self):
        self.current_account = None

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

def load_accounts():
    accounts = {}
    try:
        with open("accounts.json", "r") as file:
            data = json.load(file)
        for name, account_data in data.items():
            balance = account_data["balance"]
            transactions = account_data["transactions"]
            if "interest_rate" in account_data:
                interest_rate = account_data["interest_rate"]
                account = SavingAccount(name, balance, interest_rate)
            elif "transaction_fee" in account_data:
                transaction_fee = account_data["transaction_fee"]
                account = CheckingAccount(name, balance, transaction_fee)
            else:
                account = Account(name, balance)
            account.transactions = transactions
            accounts[name] = account
    except FileNotFoundError:
        with open("accounts.json", "w") as file:
            pass

    return accounts

def save_accounts(accounts):
    data = {}
    for name, account in accounts.items():
        data[name] = {
            "balance": account.balance, 
            "transactions": account.transactions
            }
        if isinstance(account, SavingAccount):
            data[name]["interest_rate"] = account.interest_rate
        elif isinstance(account, CheckingAccount):
            data[name]["transaction_fee"] = account.transaction_fee
    with open("accounts.json", "w") as file:
        json.dump(data, file, indent = 4)

def menu_logout():
    print("========== PYTHON BANK ==========")
    print("")
    print("1. Create account")
    print("2. Login")
    print("3. Exit")
    print("")
    print("=================================")
def menu_login(current_account):
    print("========== PYTHON BANK ==========")
    print("")
    print(f"Current user: {current_account.owner}")
    print("")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Check balance")
    print("5. Transactions")
    print("6. Add interst rate")
    print("7. Logout")
    print("8. Exit")
    print("")
    print("=================================")

def main():
    accounts = load_accounts()
    current_account = None
    bank = Bank(accounts, current_account)

    while True :
        if bank.current_account is None :
            menu_logout()
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid menu option.")
                continue
            if choice == 1:
                name = input("Enter account holder name: ")
                bank.create_account(name)
                current_account = bank.current_account
                save_accounts(accounts)
            elif choice == 2:
                name = input("Enter account holder name: ")
                bank.login(name)
                current_account = bank.current_account
            elif choice == 3:
                print(f"Thank you for using Python Bank.")
                break
            else :
                print("Invalid menu option.")
        else :
            menu_login(bank.current_account)
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid menu option.")
                continue
            if choice == 1:
                try:
                    amount = float(input("Enter deposit amount: "))
                except ValueError:
                    print("Invalid amount.")
                    continue
                bank.current_account.deposit(amount)
                print(f"The new balance is: {bank.current_account.balance}")
                save_accounts(accounts)
            elif choice == 2:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                except ValueError:
                    print("Invalid amount.")
                    continue
                bank.current_account.withdraw(amount)
                print(f"The new balance is: {bank.current_account.balance}")
                save_accounts(accounts)
            elif choice == 3:
                name = input("Enter the owner of account you want to transfer to: ")
                try:
                    amount = float(input("Enter the amount you want to transfer: "))
                except ValueError:
                    print("Invalid amount.")
                    continue
                if name in bank.accounts:
                    other_account = bank.accounts[name]
                    bank.current_account.transfer(other_account, amount)
                    save_accounts(accounts)
                else: 
                    print("Invalid account!")
            elif choice == 4:
                bank.current_account.check_balance()
            elif choice == 5:
                bank.current_account.show_transactions()
            elif choice == 6:
                if isinstance(bank.current_account, SavingAccount):
                    bank.current_account.add_interest()
                    print(f"Interest added! New balance: {bank.current_account.balance}")
                    save_accounts(accounts)
                else:
                    print("This account don't own an interest!")
            elif choice == 7:
                bank.logout()
            elif choice == 8:
                print(f"Thank you for using Python Bank.")
                break
            else:
                print("Invalid menu option.")
 
main()

