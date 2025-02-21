from register import *
from bank import *

print("WELCOME TO BANKING PROJECT")

while True:
    try:
        register = int(input("1:SIGN-UP\n2:SIGN-IN: "))
        if register == 1:
            SignUp()
        elif register == 2:
            user = SignIn()
            break
        else:
            print("Please enter a valid option.")
    except ValueError:
        print("Invalid input. Try again.")

account_number = data_query(f"SELECT account_number FROM customers WHERE username = '{user}';")[0][0]

while True:
    print(f"Welcome {user.capitalize()}, choose a banking service:\n") 
    try:
        facility = int(input("1:Balance-Enquiry\n2:Cash-Deposit\n3:Cash-Withdraw\n4:Fund-transfer\n"))
        bobj = Bank(user, account_number)

        if facility == 1:
            bobj.balance_enquiry()
        elif facility == 2:
            amount = int(input("Enter amount to deposit: "))
            bobj.deposit(amount)
            mydb.commit()
        elif facility == 3:
            amount = int(input("Enter amount to withdraw: "))
            bobj.withdraw(amount)
            mydb.commit()
        elif facility == 4:
            receiver = int(input("Enter receiver's account number: "))
            amount = int(input("Enter amount to transfer: "))
            bobj.fund_transfer(receiver, amount)
            mydb.commit()
        else:
            print("Invalid choice. Try again.")
    except ValueError:
        print("Enter a valid number.")
