import sqlite3

# create connection to the db

conn = sqlite3.connect("mydb")  # for server side programming we have change the connection
# line and we have to mention the varchar(size)
mycursor = conn.cursor()


# function to create the table
def createTable():
    print("*" * 40)
    sql = '''create table if not exists student(name varchar, email varchar primary key, 
            mobile varchar , password varchar )'''

    try:
        mycursor.execute(sql)
        print("Table Created")
    except:
        print("Something went wrong")


# function to insert data
def insertData():
    print("*" * 40)
    name = input("Enter name - ")
    email = input("Enter email - ")
    mobile = input("Enter mobile - ")
    password = input("Enter password - ")

    sql = "insert into student values('" + name + "', '" + email + "', '" + mobile + "', '" + password + "')"

    try:
        mycursor.execute(sql)
        print("Data inserted")
    except:
        print("something went wrong")


# function to update data
def updateData():
    print("*" * 40)
    email = input("Enter email - ")
    newmobile = input("Enter New mobile - ")
    sql = "update student set mobile ='" + newmobile + "' where email='" + email + "'"
    try:
        mycursor.execute(sql)
        print("Mobile updated succesfully")
    except:
        print("Something went wrong")


# function to show the data
def showData():
    sql = "select * from student"
    mycursor.execute(sql)

    for row in mycursor.fetchall():
        print(row[0], row[1], row[2], row[3])


# function to delete the data
def deleteData():
    print("*" * 40)
    email = input("Enter email - ")
    sql = "delete from student where email='" + email + "'"
    try:
        mycursor.execute(sql)
        print("Data deleted")
    except:
        print("Data deleted succesfully")


# function to login
def login():
    print("*" * 40)
    email = input("Enter email - ")
    password = input("Enter password - ")
    sql = "select * from student where email='" + email + "' and password='" + password + "'"
    mycursor.execute(sql)
    if len(mycursor.fetchall()) == 0:
        print("Could not login")
    else:
        print("Login Succesful")
        sql = "select * from student where email='" + email + "'"
        mycursor.execute(sql)
        for row in mycursor.fetchall():
            print(row[0], row[1], row[2], row[3])


while True:
    print("1. Create Table\n2. Insert Data\n3. Update Data\n4. Delete Data\n5. Show Data\n6. Login\n7. Exit")

    ch = eval(input("Enter Your Choice"))

    if ch == 1:
        createTable()
    elif ch == 2:
        insertData()
    elif ch == 3:
        updateData()
    elif ch == 4:
        deleteData()
    elif ch == 5:
        showData()
    elif ch == 6:
        login()
    elif ch == 7:
        conn.close()
        exit()
    else:
        print("Wrong choice")

    conn.commit()
