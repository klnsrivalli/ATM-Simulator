# ATM-Simulator
# Description:
    It is a basic ATM-Simulator implemented in python.It allows users to check balance,deposit and withdraw money.
# Features:
- User authentication: Users must input their PIN to access their account.
- Withdrawal: Users can withdraw money from their account.
- Deposit: Users can deposit money into their account.
- Balance Inquiry: Users can check their account balance.
- User-friendly interface: The program provides clear prompts and messages to guide users through each operation.
# Class Definition:
  - class ATM represents an ATM Machine.
  - It includes 3 methods:
    - __init__(self):Initialises ATM with initial balance of Rs.10,000
    -  check_balance(self): Returns the current balance of the ATM.
    -   withdraw(self, amount): Withdraws a specified amount from the ATM balance, if the requested amount is valid,else,shows insufficient balance
    -  deposit(self, amount): Deposits a specified amount into the ATM balance, if the amount is valid.
 #  Main Function - main():
   - This function is the entry point of the program.
   - It creates an instance of the ATM class.
   - Prompts the user to enter a PIN.
   - If the entered PIN is correct (1234 #sample PIN), it shows below options:
     - Check balance
     - Withdraw money
     - Deposit money
     - Exit
   - Based on the user's choice, it calls the corresponding method of the ATM class.
   # Output:
   - The user is prompted to enter a PIN.
   - Upon entering a correct PIN & based on the user's choice, the corresponding operation is performed, and the result is displayed.
   - If a wrong PIN is entered, it displays "INVALID PIN".

   # CONCLUSION:
   Overall, the code provides a simple ATM simulation experience with basic functionalities.  
     

    





