age = int(input("Enter your age: "))

# Adults who are 18 or older can join without parental consent.
if age >= 18:
    print("Welcome to the club!")

# Members aged 13 to 17 need parental consent to join.
elif age >= 13 and not (age >= 18):
    consent = input("Do you have parental consent? (yes/no): ").lower()

    # Teenagers with parental consent are eligible.
    if consent == "yes":
        print("Welcome to the club!")
    else:
        print("Sorry, you are not eligible yet.")

# Anyone under 13 is not eligible yet.
else:
    print("Sorry, you are not eligible yet.")