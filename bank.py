class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"✅ Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrawn: {amount}")
        else:
            print("❌ Insufficient funds!")

    def check_balance(self):
        print(f"💰 Current Balance: {self.__balance}")
        return self.__balance


# ---------- ATM SYSTEM ----------
def atm_system():
    account = BankAccount(1000)  # initial balance
    while True:
        print("\n=== ATM Menu ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print("👋 Thank you for using the ATM!")
            break

        else:
            print("❌ Invalid choice, please try again.")


# Run ATM system
atm_system()
