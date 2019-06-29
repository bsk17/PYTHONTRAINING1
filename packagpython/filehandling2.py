# function to view the products
def viewprod():
    fp = open("Products.txt", "r")
    data = fp.read()
    print(data)
    fp.close()


# function to add the products
def addprod():
    fp = open("Products.txt", "a")
    name = input("Enter product Name - ")
    price = input("Enter product Price - ")
    quantity = input("Enter product Quantity")
    data = name+":"+price+":"+quantity+"\n"
    fp.write(data)
    fp.close()


# function to remove the products
def remprod():
    pname = input("Enter the name of product to remove - ")
    fp = open("Products.txt", "r")
    lines = fp.readlines()
    fp.close()

    fb = open("Products.txt", "w+")  # second we write the data which does not contain the mentioned email
    for i in range(len(lines)):
        if pname in lines[i]:
            pass
        else:
            fb.write(lines[i])
    fb.close()


# function to update the price
def updprice():
    pname = input("Enter the name of product - ")
    newprice = input("Enter the price - ")

    fb = open("Products.txt", "r+")  # first we read the file and store a list of data
    lines = fb.readlines()
    fb.close()

    for i in range(len(lines)):
        if pname in lines[i]:
            arr = lines[i].split(":")
            arr[1] = newprice
            newdata = arr[0]+":"+arr[1]+":"+arr[2]
            print(newdata)
            lines[i] = newdata
        else:
            pass

    fp = open("Products.txt", "w+")
    for i in range(len(lines)):
        fp.write(lines[i])
    fp.close()


# function to update the quantity
def updquantity():
    pname = input("Enter the name of product - ")
    newquantity = input("Enter the price - ")

    fb = open("Products.txt", "r+")  # first we read the file and store a list of data
    lines = fb.readlines()
    fb.close()

    for i in range(len(lines)):
        if pname in lines[i]:
            arr = lines[i].split(":")
            arr[2] = newquantity
            newdata = arr[0]+":"+arr[1]+":"+arr[2]
            print(newdata)
            lines[i] = newdata
        else:
            pass

    fp = open("Products.txt", "w+")
    for i in range(len(lines)):
        fp.write(lines[i])
    fp.close()


def addcart():
    pname = input("Enter the name of product you want to purchase")
    quantity = eval(input("Enter the quantity of products"))
    tamount = 0

    fb = open("Products.txt", "r")
    lines = fb.readlines()
    fb.close()

    for i in range(len(lines)):
        if pname in lines[i]:
            arr = lines[i].split(":")
            tamount = int(arr[1]) * quantity

    fp = open("Cart.txt", "a")
    data = pname + ":" + str(quantity) + ":"+str(tamount)+"\n"
    fp.write(data)
    fp.close()


def updcart():
    name = input("Enter name of the product you want to delete from cart - ")
    fb = open("Cart.txt", "r")
    lines = fb.readlines()
    fb.close()

    fp = open("Cart.txt", "w+")  # second we write the data which does not contain the mentioned email
    for i in range(len(lines)):
        if name in lines[i]:
            pass
        else:
            fp.write(lines[i])
    fp.close()


def viewcart():
    fp = open("Cart.txt", "r")
    data = fp.read()
    print(data)
    fp.close()


def purchase():
    amttopay = 0

    fp = open("Cart.txt", "r+")  # to read the cart
    lines = fp.readlines()
    fp.close()

    for i in range(len(lines)):
        arr = lines[i].split(":")
        print("You have "+arr[1]+" "+arr[0]+" for Rs "+arr[2])
        amttopay = amttopay + int(arr[2])  # total price to pay

    print("Total amount to pay - "+str(amttopay))

    fp1 = open("Products.txt", "r+")
    lines2 = fp1.readlines()
    fp1.close()

    # to calculate the reduced quantity of products
    for i in range(len(lines)):
        for j in range(len(lines2)):
            arr1 = lines[i].split(":")
            arr2 = lines2[j].split(":")
            if arr1[0] == arr2[0]:
                arr2[2] = str(int(arr2[2])-int(arr1[1]))
                newdata = arr2[0]+":"+arr2[1]+":"+arr2[2]+"\n"
                lines2[j] = newdata

    fb1 = open("Products.txt", "w+")  # to write updated data in products
    for k in range(len(lines2)):
        fb1.write(lines2[k])
    fb1.close()

    fb = open("Cart.txt", "w+")  # to empty cart
    fb.write("")
    fb.close()


# function to register
def register(file):
    name = input("Enter the name - ")
    email = input("Enter the email - ")
    password = input("Enter the password - ")
    mobile = input("Enter the mobile number - ")
    fb = open(file + ".txt", "a")
    data = name + ":" + email + ":" + password + ":" + mobile + "\n"
    fb.write(data)
    fb.close()


# function to login
def login(file):
    email = input("Enter the email - ")
    fb = open(file + ".txt", "r")
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

                if file == "Admin":
                    print("1. View All Products\n2.Add Product\n3.Remove Product\n4.Update Price"
                          "\n5.Update Quantity\n6.Exit")

                    choice = eval(input("Choice"))

                    if choice == 1:
                        viewprod()
                    elif choice == 2:
                        addprod()
                    elif choice == 3:
                        remprod()
                    elif choice == 4:
                        updprice()
                    elif choice == 5:
                        updquantity()
                    elif choice == 6:
                        exit()
                    else:
                        print("Wrong Choice")

                if file == "Customer":
                    print("1.View All Product\n2.Add to Cart\n3.Update Cart\n"
                          "4.View Cart\n5.Purchase\n6.Exit")

                    choice = eval(input("Choice"))

                    if choice == 1:
                        viewprod()
                    elif choice == 2:
                        addcart()
                    elif choice == 3:
                        updcart()
                    elif choice == 4:
                        viewcart()
                    elif choice == 5:
                        purchase()
                    elif choice == 6:
                        exit()
                    else:
                        print("Wrong choice")


# function which will be called when user selects admin
def admin():
    print("******************************************************"
          "Welcome Admin******************************************************")
    while True:
        print("1. Register\n2.Login\n3.Exit")
        file = "Admin"
        adminchoice = eval(input("Choice"))

        if adminchoice == 1:
            register(file)
        elif adminchoice == 2:
            login(file)
        elif adminchoice == 3:
            exit(0)
        else:
            print("Wrong choice")


# function which will be called when user selects customer
def customer():
    print("******************************************************"
          "Welcome Customer******************************************************")
    print("1. Register \n 2.Login")
    file = "Customer"
    adminchoice = eval(input("Choice"))

    if adminchoice == 1:
        register(file)
    elif adminchoice == 2:
        login(file)
    else:
        print("Wrong choice")
    pass


print("1.Admin \n2.Customer")
choice = eval(input("Choice"))
if choice == 1:
    admin()
elif choice == 2:
    customer()
else:
    print("Wrong choice")
