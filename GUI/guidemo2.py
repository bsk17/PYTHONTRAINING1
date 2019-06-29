from tkinter import *
from tkinter import messagebox as mb


def register():
    name = e1.get()
    password = e2.get()
    print("NAME = ", name)
    print("PASSSWORD = ", password)
    mb.showinfo("DATA", "Welcome "+name+" Your Password is"+password)


window = Tk()
window.geometry("300x400")
window.title("First Page")

# creating our widgets
l1 = Label(window, text="Welcome to Python Project", bg="#FF512F")
l2 = Label(window, text="Enter Name = ", bg="#EA384D")
l3 = Label(window, text="Enter Pass = ", bg="#EA384D")
e1 = Entry(window)
e2 = Entry(window, show="*")  # to hide the password
b1 = Button(window, text="Register", bg="#DA22FF", command=register)
b2 = Button(window, text="Cancel", bg="#DA22FF")

# placing our widgets
l1.place(x=60, y=0)
l2.place(x=10, y=30)
e1.place(x=110, y=30)
l3.place(x=10, y=60)
e2.place(x=110, y=60)
b1.place(x=40, y= 90)
b2.place(x=200, y=90)

window.mainloop()
