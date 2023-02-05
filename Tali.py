import tkinter as tk
import random
from tkinter import simpledialog, messagebox

def tell_why_milan_loves_you():
    reasons = [
        "you are kind, caring, and always bring a smile to his face.",
        "you make every day special and fill it with laughter.",
        "of the way you look at him and the way you understand him."
    ]
    reason = random.choice(reasons)
    messagebox.showinfo("Why Milan loves you", f"Milan loves you because {reason}")

def show_text(root):
    text = "I love you, you little. I cannot expres my love for you with words. But Everytime it feels like i forgot about you, i made this reminder, hopefully you will never need it"
    text_label = tk.Label(root, text="", wraplength=700, width=100, height=100)
    button = tk.Button(root, text="Why I love you", command=tell_why_milan_loves_you, bg="green")

    def update_label(i):
        if i < len(text):
            text_label["text"] = text[:i+1]
            root.after(100, lambda: update_label(i+1))
        else:
            button.place(relx=0.5, rely=0.5, anchor='s', y=-100)
            text_label.pack(pady=20)

    root.after(10000, lambda: update_label(0))
    text_label.place(relx=0.5, rely=0.5, anchor='center')

def check_password(password):
    formatted_password = password.replace(" ", "").lower()
    if formatted_password == "guardianangel".lower():
        root = tk.Tk()
        root.title("Text")
        root.geometry("1000x1000")
        show_text(root)
        root.mainloop()
    else:
        messagebox.showerror("Incorrect password", "Try again")
        root.quit()

root = tk.Tk()
root.withdraw()
password = simpledialog.askstring("Password", "Enter your password:", show='*')
check_password(password)
root.mainloop()
