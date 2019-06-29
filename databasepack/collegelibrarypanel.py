import pymysql

conn = pymysql.connect(host="localhost", user="root", password="password", database="pythonbhilai")
mycursor = conn.cursor()


def signup(role):
    if role == "Employee":
        eid = input("Enter Employee ID - ")
        name = input("Enter Name - ")
        dept = input("Enter department - ")
        salary = input("Enter Salary - ")

        try:
            sql = "insert into empdetail values('" + eid + "','" + name + "','" + dept + "','" + salary + "')"
            mycursor.execute(sql)
            print("Employee Sign up successful")
            conn.commit()
        except TypeError:
            print("Type Error")
            signup("Employee")
        except:
            print("Something went wrong")
            signup("Employee")

    elif role == "Student":
        rollno = input("Enter Roll no of student - ")
        name = input("Enter Name - ")
        dept = input("Enter department - ")
        sem = input("Enter Semester - ")

        try:
            sql = "insert into studetail values('" + rollno + "', '" + name + "', '" + dept + "', '" + sem + "')"
            print(sql)
            mycursor.execute(sql)
            print("Student Sign up successful")
            conn.commit()
        except TypeError:
            print("Type Error")
            signup("Student")
        except:
            print("Something went wrong")
            signup("Student")

    else:
        print("Signup unsuccessful")


def signin(role):
    if role == "Employee":
        empid = input("Enter Employee ID - ")
        name = input("Enter Name - ")
        sql = "select * from empdetail where empid='" + empid + "' and name='" + name + "'"
        mycursor.execute(sql)

        if len(mycursor.fetchall()) == 0:
            print("Could not login")
        else:
            print("Login Succesful")
            sql = "select * from empdetail where empid='" + empid + "'"
            mycursor.execute(sql)
            for row in mycursor.fetchall():
                print(row[0], ":", row[1], ":", row[2], ":", row[3])

    elif role == "Student":
        rollno = input("Enter Roll No - ")
        name = input("Enter Name - ")
        sql = "select * from studetail where rollno='" + rollno + "' and name='" + name + "'"
        mycursor.execute(sql)

        if len(mycursor.fetchall()) == 0:
            print("Could not login")
        else:
            print("Login Succesful")
            sql = "select * from studetail where rollno='" + rollno + "'"
            mycursor.execute(sql)
            for row in mycursor.fetchall():
                print(row[0], ":", row[1], ":", row[2], ":", row[3])

    else:
        print("Sign In unsuccessful")


def addbook():
    print("*" * 30 + "ADD BOOK" + "*" * 30)
    bid = input("Enter Book Id - ")
    title = input("Enter Title - ")
    subject = input("Enter Subject - ")
    author = input("Enter Author - ")
    status = input("Enter Status - (avail/issued)")
    sql = "insert into books values('" + bid + "','" + title + "','" + subject + "','" + author + "','" + status + "')"
    mycursor.execute(sql)
    try:

        conn.commit()
        print("Book Added Succesfully")
    except:
        print("Something went wrong")


def deletebook():
    print("*" * 30 + "DELETE BOOK" + "*" * 30)
    bid = input("Enter the Book Id - ")
    try:
        sql = "delete from books where bid='" + bid + "'"
        mycursor.execute(sql)
        print("Book Deleted successfully")
        conn.commit()
    except:
        print("Something went wrong")


def viewallbooks():
    print("*" * 30 + "VIEW ALL BOOKS" + "*" * 30)
    sql = "select * from books"
    mycursor.execute(sql)
    for row in mycursor.fetchall():
        print(row[0], ":", row[1], ":", row[2], ":", row[3], ":", row[4])
    conn.commit()


def searchbook():
    print("*" * 30 + "SEARCH BOOK" + "*" * 30)
    bid = input("Enter the book id")
    try:
        sql = "select * from books where bid='" + bid + "'"
        mycursor.execute(sql)

        if len(mycursor.fetchall()) != 0:
            print("Book Found")
            sql = "select * from books where bid='" + bid + "'"
            mycursor.execute(sql)
            for i in mycursor.fetchall():
                print(i[0], ":", i[1], ":", i[2], ":", i[3], ":", i[4])
        else:
            print("Book not found")
        conn.commit()
    except:
        print("Something went wrong")


def issuebook():
    print("*" * 30 + "ISSUE BOOK" + "*" * 30)
    bid = input("Enter Book Id - ")
    issueto = input("Enter Student Roll No - ")
    issuedby = input("Enter Employee ID - ")

    try:
        sql = "update books set status='issued' where bid='" + bid + "' and status='avail'"
        mycursor.execute(sql)
        conn.commit()
    except:
        print("Book not available")

    sql2 = "select * from books where bid='" + bid + "' and status='issued'"
    mycursor.execute(sql2)
    conn.commit()
    if len(mycursor.fetchall()) != 0:
        print("Book issued successfully")
    else:
        print("Cannot issue book")
    sql3 = "insert into issuedetail values('" + bid + "', '" + issueto + "', '" + issuedby + "')"
    mycursor.execute(sql3)
    conn.commit()


# function which shows admin functions
def employeepanel():
    print("\n" + "*" * 30 + "Welcome Employee" + "*" * 30)
    role = "Employee"
    while True:
        print("\n" + "*" * 50)
        print("1. Sign Up\n2.Sign In\n3. Add Book Details\n4. Delete Books From Records"
              "\n5. View All Books\n6. Search For Book\n7. Issue Book to student\n8. Exit")
        admin_choice = eval(input("Enter Choice - "))
        if admin_choice == 1:
            signup(role)
        elif admin_choice == 2:
            signin(role)
        elif admin_choice == 3:
            addbook()
        elif admin_choice == 4:
            deletebook()
        elif admin_choice == 5:
            viewallbooks()
        elif admin_choice == 6:
            searchbook()
        elif admin_choice == 7:
            issuebook()
        elif admin_choice == 8:
            exit()
            conn.close()
        else:
            print("Wrong choice")


# function which shows student functions
def studentpanel():
    print("\n" + "*" * 30 + "Welcome Student" + "*" * 30)
    role = "Student"
    while True:
        print("\n" + "*" * 50)
        print("1. Sign Up\n2.Sign In"
              "\n3. View All Books\n4. Search For Book\n5. Exit")
        admin_choice = eval(input("Enter Choice - "))
        if admin_choice == 1:
            signup(role)
        elif admin_choice == 2:
            signin(role)
        elif admin_choice == 3:
            viewallbooks()
        elif admin_choice == 4:
            searchbook()
        elif admin_choice == 5:
            exit()
            conn.close()
        else:
            print("Wrong choice")


while True:
    print("\n" + "*" * 30 + "Welcome to college library Panel" + "*" * 30)
    print("1. Employee\n2. Student\n 3. Exit")
    panel_choice = eval(input("Enter your choice  - "))
    if panel_choice == 1:
        employeepanel()
    elif panel_choice == 2:
        studentpanel()
    elif panel_choice == 3:
        exit()
        conn.close()
    else:
        print("Wrong Choice")
