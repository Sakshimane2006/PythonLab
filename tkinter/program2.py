from tkinter import *

root = Tk()
root.title("Button Example")
root.geometry("300x200")

button = Button(root, text="Click Me")
button.pack()

root.mainloop()