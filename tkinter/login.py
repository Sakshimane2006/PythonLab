
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My Login App")
root.geometry("400x500")
root.configure(bg="#EAF0F6")
root.resizable(False, False)

users = {}

def clear_page():
    for widget in root.winfo_children():
        widget.destroy()

def welcome_page(username):
    clear_page()

    frame = tk.Frame(root, bg="white", padx=30, pady=40)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Welcome!", font=("Arial", 25, "bold"),
             bg="white", fg="#2563EB").pack(pady=15)

    tk.Label(frame, text=f"Hello, {username}!",
             font=("Arial", 15), bg="white").pack(pady=10)

    tk.Button(frame, text="LOGOUT", width=22, bg="#DC2626",
              fg="white", relief="flat",
              command=login_page).pack(pady=20, ipady=8)

def signup_page():
    clear_page()

    frame = tk.Frame(root, bg="white", padx=30, pady=25)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Create Account", font=("Arial", 22, "bold"),
             bg="white", fg="#2563EB").pack(pady=15)

    tk.Label(frame, text="Username", bg="white").pack(anchor="w")
    username = tk.Entry(frame, font=("Arial", 12), width=25)
    username.pack(pady=8, ipady=5)

    tk.Label(frame, text="Password", bg="white").pack(anchor="w")
    password = tk.Entry(frame, font=("Arial", 12), width=25, show="*")
    password.pack(pady=8, ipady=5)

    def register():
        name = username.get().strip()
        pwd = password.get()

        if not name or not pwd:
            messagebox.showwarning("Error", "Please fill all fields")
        elif name in users:
            messagebox.showerror("Error", "Username already exists")
        else:
            users[name] = pwd
            messagebox.showinfo("Success", "Account created successfully")
            login_page()

    tk.Button(frame, text="SIGN UP", command=register, width=22,
              bg="#2563EB", fg="white", relief="flat").pack(
                  pady=15, ipady=8)

    tk.Button(frame, text="Back to Login", command=login_page,
              bg="white", fg="#2563EB", relief="flat").pack()

def login_page():
    clear_page()

    frame = tk.Frame(root, bg="white", padx=30, pady=30)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Welcome Back!", font=("Arial", 23, "bold"),
             bg="white", fg="#2563EB").pack(pady=15)

    tk.Label(frame, text="Username", bg="white").pack(anchor="w")
    username = tk.Entry(frame, font=("Arial", 12), width=25)
    username.pack(pady=8, ipady=5)

    tk.Label(frame, text="Password", bg="white").pack(anchor="w")
    password = tk.Entry(frame, font=("Arial", 12), width=25, show="*")
    password.pack(pady=8, ipady=5)

    def login():
        name = username.get().strip()
        pwd = password.get()

        if name in users and users[name] == pwd:
            welcome_page(name)
        else:
            messagebox.showerror("Login Failed", "Please check your username and password")

    tk.Button(frame, text="LOGIN", command=login, width=22,
              bg="#2563EB", fg="white", relief="flat",
              cursor="hand2").pack(pady=15, ipady=8)

    tk.Button(frame, text="Create New Account", command=signup_page,
              bg="white", fg="#2563EB", relief="flat",
              cursor="hand2").pack()

login_page()
root.mainloop()
