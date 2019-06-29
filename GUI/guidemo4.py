from tkinter import *
from tkinter import messagebox as mb


window = Tk()
window.geometry("300x400")

v = IntVar()
var = StringVar()
dish = ["PIZZA", "BURGER", "NOODLE", "AALOO"]
city = ['patna', 'raipur', 'bhilai', 'noida']


def show():
    x = v.get()
    mb.showinfo("YOUR CHOICE", dish[x-1])
    print(var.get())


for i in range(len(dish)):
    r1 = Radiobutton(window, text=dish[i], value=i+1, variable=v)
    r1.pack()

b = Button(window, text="Show Dish", command=show)
b.pack()

l = Label(window, text="Select city")
l.pack()
opt = OptionMenu(window, var, *city)
opt.pack()
window.mainloop()
