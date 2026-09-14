from accounts import Account, SavingAccount, CheckingAccount

class Bank:
    def __init__(self, accounts, current_account):
        self.accounts = accounts
        self.current_account = current_account
    def create_account(self, name):
        if name in self.accounts:
            print ("Account already exists.")
        else :
            print("Choose account type:")
            print("1. Regular Account")
            print("2. Savings Account")
            print("3. Checking Account")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid menu option.")
                return
            if choice == 1:
                new_account = Account(name, 0.0)
                self.accounts[name] = new_account
                self.current_account = new_account
                print("Account created successfully.")
            elif choice == 2:
                try:
                    interest_rate = float(input("Enter your interest rate: "))
                    new_account = SavingAccount(name, 0.0, interest_rate)
                    self.accounts[name] = new_account
                    self.current_account = new_account
                    print("Account created successfully.")
                except ValueError:
                    print("Invalid interest rate!")
            elif choice == 3 :
                try:
                    transaction_fee = float(input("Enter your transaction fee: "))
                    new_account = CheckingAccount(name, 0.0, transaction_fee)
                    self.accounts[name] = new_account
                    self.current_account = new_account
                    print("Account created successfully.")
                except ValueError:
                    print("Invalid transaction fee!")
            else:
                print("Invalid account type.")
    def login(self, name):
        if name in self.accounts:
            print (f"Welcome, {name}!")
            self.current_account = self.accounts[name]
        else:
            print ("Account not found.")
            self.current_account = None
    def logout(self):
        self.current_account = None
