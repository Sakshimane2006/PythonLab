from tkinter import *

root = Tk()
root.title("My First GUI")
root.geometry("300x200")

label = Label(root, text="Welcome to Python")
label.pack()

root.mainloop()