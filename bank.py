def show_menu():
    print("========== PYTHON BANK ==========")
    print("")
    print("1. Create account")
    print("2. Login")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Exit")
    print("")
    print("=================================")

def create_account(accounts_dict):
    account = input("Enter account holder name: ")
    if account in accounts_dict:
        print ("Account already exists.")
    else: 
        accounts_dict[account] = 0.0
        print ("Account created successfully.")
    return (accounts_dict, account)

def login(accounts_dict):
    current_user = input("Enter account holder name: ")
    if current_user in accounts_dict:
        print (f"Welcome, {current_user}!")
        return current_user
    else:
        print ("Account not found.")
        return None

def deposit(accounts_dict, current_user):
    amount = float(input("Enter deposit amount: "))
    if amount <= 0:
        print("Invalid amount.")
    else:
        accounts_dict[current_user] += amount
    return accounts_dict[current_user]

def withdraw(accounts_dict, current_user):
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount.")
    elif amount > accounts_dict[current_user]:
        print("Insufficient funds.")
    else:
        accounts_dict[current_user] -= amount
    return accounts_dict[current_user]

def check_balance(accounts_dict, current_user):
    print(f"Current balance: {accounts_dict[current_user]}")

def load_accounts():
    accounts_dict = {}
    try :
        with open("accounts.txt", "r") as file:
            for line in file:
                parts = line.split(",")
                accounts_dict[parts[0]] = float(parts[1])
            return accounts_dict
    except FileNotFoundError:
        with open("accounts.txt", "w") as file:
            pass
            return accounts_dict

def save_accounts(accounts_dict):
    with open("accounts.txt", "w") as file:
        for key, value in accounts_dict.items():
            line = f"{key},{value}\n"
            file.write(line)

def main():
    accounts_dict = load_accounts()
    current_user = None

    while True:
        show_menu()
        choice = int(input("enter your choice: "))
        if choice == 1:
            accounts_dict, current_user = create_account(accounts_dict)
            save_accounts(accounts_dict)
        elif choice == 2:
            current_user = login(accounts_dict)
        elif choice == 3:
            if current_user is None:
                print("Please login first.")
            else:
                print(f"The new balance is: {deposit(accounts_dict, current_user)}")
                save_accounts(accounts_dict)
        elif choice == 4:
            if current_user is None:
                print("Please login first.")
            else:
                print(f"The new balance is: {withdraw(accounts_dict, current_user)}")
                save_accounts(accounts_dict)
        elif choice == 5:
            if current_user is None:
                print("Please login first.")
            else:
                check_balance(accounts_dict, current_user)
        elif choice == 6:
            print(f"Thank you for using Python Bank.")
            break
        else:
            print("Invalid menu option.")

main()