from tkinter import *

window = Tk()
window.title("GUI DEMO")
# window.minsize(width=300, height=400)  # for minimum constraint
# window.maxsize(width=300, height=400)  # for maximum constraint
window.geometry("300x400")  # this is used widely
# window.iconbitmap("file.ico")  # to change the icon

x = Label(window, text="Welcome to Python Training", bg="red", fg="white")  # to put any text
x.pack()  # this is compulsory
window.mainloop()
