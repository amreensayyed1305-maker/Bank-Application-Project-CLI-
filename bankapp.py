# Simple Banking App

balance = 0

# Function to add money
def credit(amount):
    global balance
    balance = balance + amount
    print("Money added:", amount)
    print("Balance:", balance)


# Function to remove money
def debit(amount):
    global balance
    balance = balance - amount
    print("Money removed:", amount)
    print("Balance:", balance)


# Function to show balance
def show_balance():
    print("Current Balance:", balance)


# Menu
print("Bank App")

while True:
    print("\n1. Add Money")
    print("2. Remove Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose (1/2/3/4): ")

    if choice == "1":
        amount = int(input("Enter amount: "))
        credit(amount)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        debit(amount)

    elif choice == "3":
        show_balance()

    elif choice == "4":
        print("Thank you!")
        break
