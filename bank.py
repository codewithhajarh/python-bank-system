def show_menu():
    print("========== PYTHON BANK ==========")
    print("")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("")
    print("=================================")

def deposit(balance):
    amount = float(input("Enter deposit amount: "))
    if deposit <= 0:
        print("Invalid amount.")
    else:
        balance += amount
    return balance

def withdraw(balance):
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
    return balance

def check_balance(balance):
    print(f"Current balance: {balance}")

def main():
    balance = 0.0

    while True:
        show_menu()
        choice = int(input("enter your choice: "))
        if choice == 1:
            balance = deposit(balance)
            print(f"The new balance is: {balance}")
        elif choice == 2:
            balance = withdraw(balance)
            print(f"The new balance is: {balance}")
        elif choice == 3:
            check_balance(balance)
        elif choice == 4:
            print(f"Thank you for using Python Bank.")
            break
        else:
            print("Invalid menu option.")

main()