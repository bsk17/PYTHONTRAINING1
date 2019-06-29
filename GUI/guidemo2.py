from tkinter import *

window = Tk()
window.geometry("300x400")
window.title("First Page")
l1 = Label(window, text="Welcome to Python Project")
l2 = Label(window, text="Enter Name = ")
l3 = Label(window, text="Enter Pass = ")
e1 = Entry(window)
e2 = Entry(window)
b1 = Button(window, text="Register")
b2 = Button(window, text="Cancel")

l1.pack()
l2.pack()
e1.pack()
l3.pack()
e2.pack()
b1.pack()
b2.pack()

window.mainloop()
