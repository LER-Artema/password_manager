import json
from random import randint, shuffle, choice
from tkinter import *
from tkinter import messagebox

import pyperclip


# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_l = [choice(letters) for _ in range(randint(8, 10))]
    password_s = [choice(symbols) for _ in range(randint(2, 4))]
    password_n = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_l + password_s + password_n

    shuffle(password_list)

    passwor = "".join(password_list)

    password_entry.insert(0, passwor)
    pyperclip.copy(passwor)


def search_website():
    try:
        with open("Passwords_Data.json") as website_data:
            web_data = json.load(website_data)
            w = website_entry.get()
            w = w.capitalize()
    except FileNotFoundError:
        messagebox.showwarning("Oops! No file found")
    else:
        try:
            web = web_data[w]
        except KeyError:
            messagebox.showwarning("Oops!")
        else:
            messagebox.showinfo(f"{w}", f'Email:{web["Email"]} \n '
                                        f'Password: {web["Password"]}')


def save_data():
    empty_fields = website_entry.get() == "" or email_entry.get() == ""

    w = website_entry.get()
    p = password_entry.get()
    e = email_entry.get()
    w = w.capitalize()
    new_data = {w: {"Password": p, "Email": e}}
    if empty_fields:
        messagebox.showwarning("Oops", "Don't leave any fields empty!")
    else:
        try:
            with open("Passwords_Data.json", mode="r") as passwords_data:
                data = json.load(passwords_data)
        except FileNotFoundError:
            with open("Passwords_Data.json", mode="w") as passwords_data:
                json.dump(new_data, passwords_data, indent=4)
        else:
            data.update(new_data)
            with open("Passwords_Data.json", mode="w") as passwords_data:
                json.dump(data, passwords_data, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# --------------------UI-----------------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
email = Label(text="Email/Username:")
password = Label(text="Password:")

website.grid(column=0, row=1)
email.grid(column=0, row=2)
password.grid(column=0, row=3)

website_entry = Entry()
email_entry = Entry(width=35)
password_entry = Entry()

website_entry.grid(column=1, row=1, sticky="EW")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "david2002rivs@gmail.com")
password_entry.grid(column=1, row=3, sticky="EW")

generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3, sticky="EW")
search = Button(text="Search", command=search_website)
search.grid(column=2, row=1, sticky="EW")
add = Button(text="Add", width=37, command=save_data)
add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
