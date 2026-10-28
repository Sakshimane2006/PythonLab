from tkinter import *

root = Tk()
root.title("Radiobutton Example")
root.geometry("300x200")

v = IntVar()

r1 = Radiobutton(root, text="Male", variable=v, value=1)
r2 = Radiobutton(root, text="Female", variable=v, value=2)

r1.pack()
r2.pack()

root.mainloop()