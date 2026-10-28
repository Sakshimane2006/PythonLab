# import tkinter as tk

# # Create the main window
# root = tk.Tk()

# # Set window title
# root.title("My First GUI")

# # Set window size
# root.geometry("400x300")

# # Create a label
# label = tk.Label(root, text="Hello World!", font=("Arial", 16))

# # Display the label
# label.pack(pady=20)

# # Run the application
# root.mainloop()

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Registration")
root.geometry("500x600")
root.configure(bg="#101827")
root.resizable(False, False)

title = tk.Label(
    root,
    text="STUDENT REGISTRATION",
    font=("Arial", 22, "bold"),
    bg="#101827",
    fg="#60A5FA"
)
title.pack(pady=(30, 8))

subtitle = tk.Label(
    root,
    text="Create your student profile",
    font=("Arial", 11),
    bg="#101827",
    fg="#CBD5E1"
)
subtitle.pack(pady=(0, 25))

form = tk.Frame(root, bg="#1E293B", padx=30, pady=25)
form.pack(padx=30, fill="x")

def add_field(label_text):
    tk.Label(
        form,
        text=label_text,
        font=("Arial", 11, "bold"),
        bg="#1E293B",
        fg="#F8FAFC",
        anchor="w"
    ).pack(fill="x", pady=(8, 5))

    entry = tk.Entry(
        form,
        font=("Arial", 12),
        bg="#334155",
        fg="white",
        insertbackground="white",
        relief="flat",
        bd=0
    )
    entry.pack(fill="x", ipady=9, pady=(0, 10))
    return entry

name_entry = add_field("Full Name")
email_entry = add_field("Email Address")
age_entry = add_field("Age")
course_entry = add_field("Course")

def register():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    age = age_entry.get().strip()
    course = course_entry.get().strip()

    if not all([name, email, age, course]):
        messagebox.showwarning("Missing Details", "Please fill in all fields.")
        return

    if "@" not in email or "." not in email:
        messagebox.showwarning("Invalid Email", "Please enter a valid email.")
        return

    if not age.isdigit() or int(age) < 1 or int(age) > 120:
        messagebox.showwarning("Invalid Age", "Please enter a valid age.")
        return

    messagebox.showinfo(
        "Registration Successful",
        f"Welcome, {name}!\n\nEmail: {email}\nAge: {age}\nCourse: {course}"
    )

    for entry in [name_entry, email_entry, age_entry, course_entry]:
        entry.delete(0, tk.END)

tk.Button(
    root,
    text="REGISTER NOW",
    font=("Arial", 12, "bold"),
    bg="#3B82F6",
    fg="white",
    activebackground="#2563EB",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=register
).pack(fill="x", padx=60, pady=25, ipady=12)

tk.Label(
    root,
    text="LEARN  •  GROW  •  SUCCEED",
    font=("Arial", 9, "bold"),
    bg="#101827",
    fg="#94A3B8"
).pack(pady=5)

root.mainloop()
