from tkinter import *
from tkinter import messagebox as mb

window = Tk()
window.geometry("300x400")

v = IntVar()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()

def show():
    sel = []
    unsel = []

    if v.get() == 1:
        sel.append("Swimming")
    else:
        unsel.append("Swimming")

    if v1.get() == 1:
        sel.append("Playing")
    else:
        unsel.append("Playing")

    if v2.get() == 1:
        sel.append("Sleeping")
    else:
        unsel.append("Sleeping")

    if v3.get() == 1:
        sel.append("Studying")
    else:
        unsel.append("Studying")

    data = "Selected : "+str(sel)+"\nUnselected"+str(unsel)
    mb.showinfo("HOBBIES", data)

l1 = Label(window, text="Select your hobbies")
l1.place(x=10, y=0)

check1 = Checkbutton(window, text='Swimming', onvalue=1, offvalue=0, variable=v)
check2 = Checkbutton(window, text='Playing', onvalue=1, offvalue=0, variable=v1)
check3 = Checkbutton(window, text='Sleeping', onvalue=1, offvalue=0, variable=v2)
check4 = Checkbutton(window, text='Studying', onvalue=1, offvalue=0, variable=v3)

check1.place(x=150, y=0)
check2.place(x=150, y=30)
check3.place(x=150, y=60)
check4.place(x=150, y=90)

b1 = Button(window, text="show", command=show)
b1.place(x=0, y=120)
window.mainloop()
