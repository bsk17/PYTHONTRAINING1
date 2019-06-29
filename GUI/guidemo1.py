from tkinter import *
from tkinter import messagebox as mb


# this function is passed as command argument for hello label
def show():

    # for creating a messagebox
    mb.showinfo("Warning", "you clicked Hello")

    # for creating another window
    window2 = Tk()
    window2.geometry("300x400")
    a = Label(window2, text="YOU CLICKED HELLO")
    a.pack()
    window2.mainloop()


window = Tk()
window.title("GUI DEMO")
# window.minsize(width=300, height=400)  # for minimum constraint
# window.maxsize(width=300, height=400)  # for maximum constraint
window.geometry("300x400")  # this is used widely
# window.iconbitmap("file.ico")  # to change the icon

x = Label(window, text="Welcome to Python Training",
          bg="red", fg="white", font=('Times New Roman', 10, 'bold'))  # to put any text
x.pack()  # this is compulsory

b1 = Button(window, text="Hello", width=10, bg="blue", fg="white", command=show)
b1.pack()

b2 = Button(window, text="Cancel", width=10, bg="red", command=window.quit)
b2.pack()

window.mainloop()
