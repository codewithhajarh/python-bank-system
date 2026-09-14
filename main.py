import json
from accounts import Account, SavingAccount, CheckingAccount, InsufficientFundError, InvalidAmountError
from bank import Bank

def load_accounts():
    accounts = {}
    try:
        with open("accounts.json", "r") as file:
            data = json.load(file)
        for name, account_data in data.items():
            transactions = account_data["transactions"]
            account_type = account_data["type"]
            if account_type == "saving":
                account = SavingAccount.from_dict(account_data)
            elif account_type == "checking":
                account = CheckingAccount.from_dict(account_data)
            else:
                account = Account.from_dict(account_data)
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
            "owner": account.owner,
            "balance": account.balance, 
            "transactions": account.transactions,
            "type": account.type
            }
        
        if account.type == "saving":
            data[name]["interest_rate"] = account.interest_rate
        elif account.type == "checking":
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
                try:
                    bank.current_account.withdraw(amount)
                    print(f"The new balance is: {bank.current_account.balance}")
                    save_accounts(accounts)
                except InsufficientFundError as error:
                    print(error)
                except InvalidAmountError as error:
                    print(error)
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