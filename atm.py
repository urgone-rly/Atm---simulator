# ATM Simulator Program

def check_balance(balance):
    print(f"\nYour current balance is ₹{balance}\n")
    return balance

def deposit_money(balance):
    try:
        amount = int(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("Amount must be positive.")
        else:
            balance += amount
            print(f"₹{amount} deposited successfully.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return balance

def withdraw_money(balance):
    try:
        amount = int(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return balance

# --- Main Program ---
correct_pin = "1234"
balance = 1000
attempts = 3

while attempts > 0:
    pin = input("Enter your 4-digit ATM PIN: ")
    if pin == correct_pin:
        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            try:
                choice = int(input("Enter your choice (1-4): "))
                if choice == 1:
                    balance = check_balance(balance)
                elif choice == 2:
                    balance = deposit_money(balance)
                elif choice == 3:
                    balance = withdraw_money(balance)
                elif choice == 4:
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please choose between 1-4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts left: {attempts}")
        if attempts == 0:
            print("You have entered the wrong PIN three times. Your account is temporarily locked.")
