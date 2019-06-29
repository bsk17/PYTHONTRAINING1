# function to login
def login():
    email = input("Enter the email - ")
    fb = open("Data2.txt", "r")
    lines = fb.readlines()
    for singleline in lines:
        arr = singleline.split(":")
        if arr[1] == email:  # to check for presence of email
            pstatus = 1
            if pstatus != 1:
                print("Email does not exists")
            password = input("Enter the password - ")
            if arr[2] == password:  # to check for respective password for email
                lstatus = 1
                print("Logged in succesfully ")

                if pstatus == 1 and lstatus != 1:
                    print("Password is incorrect")

                fb.close()

                print("1. To change password\n2. To delete account")
                ch = eval(input("Enter Choice - "))
                if ch == 1:
                    changepass(password)
                elif ch == 2:
                    delete(email)
                else:
                    print("Wrong choice")
                    break


# function to register
def register():
    name = input("Enter the name - ")
    email = input("Enter the email - ")
    password = input("Enter the password - ")
    mobile = input("Enter the mobile number - ")
    fb = open("Data2.txt", "a")
    data = name + ":" + email + ":" + password + ":" + mobile + "\n"
    fb.write(data)
    fb.close()


# function to change the password
def changepass(passw):
    newpassword = input("Enter the new password - ")

    # first read the data
    fb = open("Data2.txt", "r+")  # first we read the file and store a list of data
    lines = fb.readlines()
    fb.close()

    # locate the data which contains password and change the password
    for i in range(len(lines)):
        if passw in lines[i]:
            arr = lines[i].split(":")
            olddata = arr[0]+":"+arr[1]+":"+arr[2]+":"+arr[3]
            arr[2] = newpassword
            newdata = arr[0]+":"+arr[1]+":"+arr[2]+":"+arr[3]
            print(newdata)
            lines[i] = newdata
        else:
            pass

    # write the data back to file
    fp = open("Data2.txt", "w+")
    for i in range(len(lines)):
        fp.write(lines[i])
    fp.close()


# function to delete the account
def delete(email):
    fb = open("Data2.txt", "r+")  # first we read the file and store a list of data
    lines = fb.readlines()
    fb.close()
    print(lines)

    fp = open("Data2.txt", "w+")  # second we write the data which does not contain the mentioned email
    for i in range(len(lines)):
        if email in lines[i]:
            pass
        else:
            fp.write(lines[i])
            print(lines)
    fp.close()


print("**************WELCOME**************")
choice = eval(input("Enter 1 to Register\nEnter 2 to login"))


if choice == 1:  # main choice to the user
    register()
elif choice == 2:
    login()
else:
    print("Invalid choice")
