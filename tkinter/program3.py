from tkinter import *

root = Tk()
root.title("Entry Example")
root.geometry("300x200")

label = Label(root, text="Enter Your Name")
label.pack()

entry = Entry(root)
entry.pack()

root.mainloop()