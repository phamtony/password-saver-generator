from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- FIND PW ------------------------------- #
def find_password():
    website_read = website_entry.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError as warning_msg:
        messagebox.showinfo(title="Data File Missing", message=f"No data file found.")
    else:
        if website_read in data:
            email = data[website_read]["email"]
            password = data[website_read]["password"]
            messagebox.showinfo(title=f"{website_read}",
                                message=f"email: {email} \npassword: {password}")
        else:
            messagebox.showwarning(title="Error", message=f"No details for {website_read} exist.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    password_entry.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_inputs():
    website_read = website_entry.get()
    email_read = email_entry.get()
    password_read = password_entry.get()
    new_data = {
        website_read: {
            "email": email_read,
            "password": password_read
        }
    }

    if len(website_read) == 0 or len(password_read) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any blank fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Mypass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "insert_email@here.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

search_pw_button = Button(text="Search", width=11, command=find_password)
search_pw_button.grid(row=1, column=2)

generate_pw_button = Button(text="Generate Password", width=11, command=generate_pw)
generate_pw_button.grid(row=3, column=2)

add_mypass_button = Button(text="Add", width=34, command=get_inputs)
add_mypass_button.grid(row=4, column=1, columnspan=2)


window.mainloop()