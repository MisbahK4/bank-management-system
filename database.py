import mysql.connector as sql

mydb = sql.connect(
            host="127.0.0.1",
            user="root",
            password="misbahpt6",
            database="BANK"
)
cursor=mydb.cursor()
# if mydb.is_connected():
#         print("Connected to the database successfully!")
# else:
#         print("Not connected")        
# print(cursor)
def createcustomertable():
    cursor.execute('''
              CREATE TABLE IF NOT EXISTS customers
              (username VARCHAR(20),
               password VARCHAR(20),
               name VARCHAR(20),
               age INTEGER,
               city VARCHAR(20),
               balance INTEGER,
               account_number INTEGER,
               status BOOLEAN
              
              ) 
                ''')
def data_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result    
mydb.commit()                
if __name__ =="__main__":
    createcustomertable()
