balance = 10000 
def check_balance():
    print("Current Balance =", balance)
def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        balance = balance + amount
        print("Amount Deposited Successfully")
        print("Updated Balance =", balance)
    else:
        print("Invalid Amount")
def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance = balance - amount
        print("Please collect your cash")
        print("Remaining Balance =", balance)
    else:
        print("Insufficient Balance")
while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Thank You for Using ATM")
        break
    else:
        print("Invalid Choice")

