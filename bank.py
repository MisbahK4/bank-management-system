from database import *
import datetime

class Bank:
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number

    def create_transaction_table(self):
        data_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transactions ("
                   f"timedate VARCHAR(30), "
                   f"account_number INTEGER, "
                   f"remarks VARCHAR(50), "
                   f"amount INTEGER);")

    def balance_enquiry(self):
        temp = data_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if temp:
            print(f"{self.__username}, your current balance is: ₹{temp[0][0]}")
        else:
            print("Error: Unable to retrieve balance.")

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return

        temp = data_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if temp:
            new_balance = temp[0][0] + amount
            data_query(f"UPDATE customers SET balance = {new_balance} WHERE username = '{self.__username}';")
            self.balance_enquiry()
            data_query(f"INSERT INTO {self.__username}_transactions (timedate, account_number, remarks, amount) VALUES "
                       f"('{datetime.datetime.now()}', {self.__account_number}, 'DEPOSIT', {amount});")
            print(f"{self.__username}, ₹{amount} has been deposited.")
        else:
            print("Error: Unable to process deposit.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return

        temp = data_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if temp and temp[0][0] >= amount:
            new_balance = temp[0][0] - amount
            data_query(f"UPDATE customers SET balance = {new_balance} WHERE username = '{self.__username}';")
            self.balance_enquiry()
            data_query(f"INSERT INTO {self.__username}_transactions (timedate, account_number, remarks, amount) VALUES "
                       f"('{datetime.datetime.now()}', {self.__account_number}, 'WITHDRAWAL', {amount});")
            print(f"{self.__username}, ₹{amount} has been withdrawn.")
        else:
            print("Error: Insufficient funds.")

    def fund_transfer(self, receiver_account, amount):
        if amount <= 0:
            print("Error: Transfer amount must be greater than zero.")
            return

        sender_balance = data_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        receiver_balance = data_query(f"SELECT balance FROM customers WHERE account_number = {receiver_account};")

        if not receiver_balance:
            print("Error: Receiver account not found.")
            return

        if sender_balance and sender_balance[0][0] >= amount:
            new_sender_balance = sender_balance[0][0] - amount
            new_receiver_balance = receiver_balance[0][0] + amount
            data_query(f"UPDATE customers SET balance = {new_sender_balance} WHERE username = '{self.__username}';")
            data_query(f"UPDATE customers SET balance = {new_receiver_balance} WHERE account_number = {receiver_account};")
            self.balance_enquiry()
            data_query(f"INSERT INTO {self.__username}_transactions (timedate, account_number, remarks, amount) VALUES "
                       f"('{datetime.datetime.now()}', {self.__account_number}, 'TRANSFER TO {receiver_account}', {amount});")
            print(f"{self.__username}, ₹{amount} has been transferred to account {receiver_account}.")
        else:
            print("Error: Insufficient balance.")
