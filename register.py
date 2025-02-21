from database import *
import random
from customer import Customer
from bank import Bank

def SignUp():
    username = input("CREATE USERNAME: ")
    temp = data_query(f"SELECT username FROM customers WHERE username = '{username}';")
    
    if temp:
        print("Username already exists.")
        return
    else:
        print("Username is available, please proceed.")
    
    password = input("Enter the Password: ")
    name = input("Enter the Name: ")
    age = input("Enter the Age: ")
    city = input("Enter the City: ")
    
    while True:
        account_number = random.randint(10000000, 99999999)
        temp = data_query(f"SELECT account_number FROM customers WHERE account_number = {account_number};")
        
        if not temp:
            print("YOUR ACCOUNT NUMBER:", account_number)
            break

    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()

def SignIn():
    username = input("ENTER USERNAME: ")
    temp = data_query(f"SELECT username FROM customers WHERE username = '{username}';")
    
    if temp:
        while True:
            password = input(f"WELCOME {username.capitalize()} ENTER THE PASSWORD: ")
            temp = data_query(f"SELECT password FROM customers WHERE username = '{username}';")

            if temp and temp[0][0] == password:
                print("SIGN-IN SUCCESSFUL")
                return username
            else:
                print("WRONG PASSWORD, TRY AGAIN.")
    else:
        print("Invalid username.")
        return SignIn()
     