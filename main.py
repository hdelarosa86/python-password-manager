from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# CONSTANTS
FONT = ('Arial', 14, 'normal')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    generated_password = ''.join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == '' or username == '' or password == '':
        messagebox.showwarning(title=website, message='Please do not leave any fields empty.')

    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {username}'
                                                              f'\nPassword: {password}')
        if is_ok:
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)

            with open('data.txt', mode='a') as file:
                file.write(f'{website}  |  {username}  |  {password}\n')


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=0)

# Canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:', font=FONT)
website_label.grid(column=0, row=1)

username_label = Label(text='Email/Username:', font=FONT)
username_label.grid(column=0, row=2)

password_label = Label(text='Password:', font=FONT)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=38)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=3)

window.mainloop()
