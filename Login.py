import sqlite3

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('User.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = "SELECT * from users"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id: ", row[0])
            print("Username: ", row[1])
            print("Password: ", row[2])
      

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

#readSqliteTable()


# Login Application
def login(username, password):
    try:
        sqliteConnection = sqlite3.connect('User.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = "SELECT * from users where username='" + username + "'" + " AND password='" + password + "';" 
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        #print("Printing each row")
        if(len(records) != 0):
            print("You are login!")
        else:
            print("Your password is incorrect or username!")
        for row in records:
            #print("Id: ", row[0])
            print("Username: ", row[1]," ....You are login successfully!")
            #print("Password: ", row[2])
      

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            #print("The SQLite connection is closed")


#print(login("Ho Weng Yin","D210044A"))
print("____________________________________")
print("Testing.............................")
#" or ""="
# "SELECT * from users where username='''
print(login(" ' OR '1 "," ' OR '1 "))

#print("What is ur username: ")
#username = input("What is ur username? ")
#password = input("What is ur password? ")
#print(login("Hello World' ","'OR 1 = 1"))
