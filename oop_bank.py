class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        else:
            self.balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
    def check_balance(self):
        print(f"Current balance: {self.balance}")

class Bank:
    def __init__(self, accounts, current_account):
        self.accounts = accounts
        self.current_account = current_account
    def create_account(self, name):
        if name in self.accounts:
            print ("Account already exists.")
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

def load_accounts():
    accounts = {}
    try :
        with open("oop_accounts.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                name = parts[0]
                balance = float(parts[1])
                accounts[name] = Account(name, balance)
            return accounts
    except FileNotFoundError:
        with open("oop_accounts.txt", "w") as file:
            pass
            return accounts
def save_accounts(accounts):
    with open("oop_accounts.txt", "w") as file:
        for name, account in accounts.items():
            line = f"{name},{account.balance}\n"
            file.write(line)

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
    print("3. Check balance")
    print("4. Logout")
    print("5. Exit")
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
            menu_login(current_account)
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid menu option.")
                continue
            if choice == 1:
                amount = float(input("Enter deposit amount: "))
                current_account.deposit(amount)
                print(f"The new balance is: {current_account.balance}")
                save_accounts(accounts)
            elif choice == 2:
                amount = float(input("Enter withdrawal amount: "))
                current_account.withdraw(amount)
                print(f"The new balance is: {current_account.balance}")
                save_accounts(accounts)
            elif choice == 3:
                current_account.check_balance()
            elif choice == 4:
                bank.logout()
            elif choice == 5:
                print(f"Thank you for using Python Bank.")
                break
            else:
                print("Invalid menu option.")
 
main()

