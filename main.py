from tkinter import *
FONT_SIZE = 14
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    website_entry.delete(0, len(website))
    username_entry.delete(0, len(username))
    password_entry.delete(0, len(password))
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

#Labels
website_label = Label(text='Website:', font=('Arial', FONT_SIZE, 'normal'))
website_label.grid(column=0, row=1)

username_label = Label(text='Email/Username:', font=('Arial', FONT_SIZE, 'normal'))
username_label.grid(column=0, row=2)

password_label = Label(text='Password:', font=('Arial', FONT_SIZE, 'normal'))
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
generate_password_button = Button(text='Generate Password')
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=3)


window.mainloop()
