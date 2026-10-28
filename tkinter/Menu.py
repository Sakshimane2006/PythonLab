from tkinter import *

root = Tk()
root.title("Menu Example")
root.geometry("300x200")

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Exit", command=root.quit)

root.mainloop()