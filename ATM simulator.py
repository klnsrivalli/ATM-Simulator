class ATM:
    #Initial Blanace
    def __init__(self):
        self.balance = 10000  
    #function to check balance
    def check_balance(self):
        return f"Your balance is Rs. {self.balance}"
    #function to withdraw amount
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f"Withdrawal successful. Remaining balance: Rs. {self.balance}"
        else:
            return "Insufficient balance"
    #function to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. \nBalance: Rs. {self.balance}"
        else:
            return "Invalid amount"

def main():
    atm = ATM()
    pin = input("Enter your PIN: ")
    #Sample PIN
    if pin == "1234":  
        while True:
            print("\nChoose from the below choices:")
            print("1.Check Balance")
            print("2.Withdraw Money")
            print("3.Deposit Money")
            print("4.Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                print(atm.check_balance())
            elif choice == '2':
                amount = float(input("Enter Amount: "))
                print(atm.withdraw(amount))
            elif choice == '3':
                amount = float(input("Enter Amount: "))
                print(atm.deposit(amount))
            elif choice == '4':
                print("Thank you!")
                print("HAVE A NICE DAY!!")
                break
            else:
                print("Invalid choice")
    else:
        print("Invalid PIN")

if __name__ == "__main__":
    print("***** Welcome To ATM Simulator *****")
    main()
