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
    print(f"Milan loves you because {reason}")

def on_button_click():
    password = simpledialog.askstring("Password", "Enter your password:", show='*')
    formatted_password = password.replace(" ", "").lower()
    if formatted_password == "guardianangel".lower():
        messagebox.showinfo("Hello my love")
        choice_window = tk.Tk()
        choice_window.title("Choices")

        tell_why_milan_loves_you_button = tk.Button(choice_window, text="Tell me why Milan loves me", command=tell_why_milan_loves_you, bg="green")
        tell_why_milan_loves_you_button.pack(pady=10)

        choice_window.mainloop()
    else:
        print("Incorrect password")

root = tk.Tk()
root.title("Enter Password")
root.geometry("1000x1000")

text = "I love you, you little. I cannot expres my love for you with words. But Everytime it feels like i forgot about you, i made this reminder, hopefully you will never need it"
text_label = tk.Label(root, text="", wraplength=700) # added wraplength to limit the width of the text

def update_label(i):
    if i < len(text):
        text_label["text"] = text[:i+1]
        root.after(100, lambda: update_label(i+1))
    else:
        button = tk.Button(root, text="Click Me", command=on_button_click, bg="green")
        button.place(relx=0.5, rely=0.5, anchor='s', y=-100)
        text_label.pack(pady=20)

root.after(10000, lambda: update_label(0))
text_label.place(relx=0.5, rely=0.5, anchor='center')
root.mainloop()
