balance = 1000
correct_pin = "1234"

pin = input("Enter your 4-digit PIN: ")

# Check whether the PIN is correct.
if pin == correct_pin:
    amount = float(input("Enter the amount to withdraw: "))

    # Check whether the requested amount is within the available balance.
    if amount <= balance:
        balance = balance - amount
        print(f"Withdrawal successful. New balance: {balance}")
    else:
        print("Insufficient funds")

# Stop here if the PIN is incorrect.
else:
    print("Incorrect PIN")
