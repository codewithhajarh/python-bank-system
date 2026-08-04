choice = 1
balance = 0.0
while choice != 4:
    print("========== PYTHON BANK ==========")
    print("")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("")
    print("=================================")
    choice = int(input("enter your number "))
    if choice == 4:
        print(f"Thank you for using Python Bank.")
        exit
    elif choice == 1:
        deposit = float(input("Enter deposit amount: "))
        if deposit < 0:
            print("Invalid amount.")
        else:
            balance = balance + deposit
            print(f"The new balance is: {balance}")
    elif choice == 2:
        withdraw = float(input("Enter withdrawal amount: "))
        if withdraw < 0 or withdraw > balance:
            print(f"Insufficient funds.")
        else:
            balance = balance - withdraw
            print(f"The new balance is: {balance}")
    elif choice == 3:
        print(f"Current balance: {balance}")
