from tkinter import *

root = Tk()
root.title("Checkbutton Example")
root.geometry("300x200")

v1 = IntVar()
v2 = IntVar()

c1 = Checkbutton(root, text="Male", variable=v1)
c2 = Checkbutton(root, text="Female", variable=v2)

c1.pack()
c2.pack()

root.mainloop()