from tkinter import *

root = Tk()
root.title("Listbox Example")
root.geometry("300x200")

listbox = Listbox(root)

listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")

listbox.pack()

root.mainloop()