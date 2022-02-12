from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- SEARCH ------------------------------- #

def search_pass():
    website_text=website_entry.get()
    try:
        with open("data.json", mode="r") as file:
            data=json.load(file)
            if website_text in data:

                emaila=data[website_text]["email"]
                passworda=data[website_text]["password"]
                messagebox.showwarning(title="Result", message=f"username: {emaila} \n password: {passworda}")
                pyperclip.copy(password)
            else:
                messagebox.showwarning(title="Error", message=f"Website not found in data.json")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="File data.json not found")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

characters="ABCDEFGHILMNOPQRSTUVZWYXKJabcdefghilmnopqrstuvzyxwkj1234567890!£$%&/*_-°()=@"
def generate():
    password=""
    password=password.join([random.choice(characters) for _ in range (0,10) ])
    print(password)
    password_entry.delete(0,END)
    password_entry.insert(0,string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():

        mail_text=email_entry.get()
        website_text=website_entry.get()
        pass_text=password_entry.get()

        new_data={website_text: {"email":mail_text, "password": pass_text}}
        if website_text=="" or pass_text=="":
            messagebox.showwarning(title="Are you sure ?", message="Do you really want to leave those fields empty?")
        else:
            is_ok=messagebox.askokcancel(title=website_text, message=f"These are the details entered : \n {website_text} \n {mail_text} \n Password{pass_text}\n Is it ok to save?")
            if is_ok:

                try:
                    with open("data.json", mode="r") as file:
                        #file.write(f"\n{mail_text} | {website_text} | {pass_text}")

                        #Reading old data
                        data=json.load(file)
                        #Updateing old data

                except FileNotFoundError:
                     with open("data.json","w") as file:
                            json.dump(new_data,file,indent=4)
                else:
                    data.update(new_data)

                    with open("data.json", mode="w") as file:

                        json.dump(data, file, indent=4)
                finally:
                    print(mail_text,website_text,pass_text)
                    website_text=website_entry.delete(0,31)
                    pass_text=password_entry.delete(0,31)


# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Password Manager")
window.config( padx=50, pady=50, bg="white")



canvas=Canvas(width=200, height=200, bg="white",highlightthickness=0)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1,row=0)



#Labels
labelWeb=Label(window, text="Website:",  bg="white")
labelEmail=Label(window, text="Email/Username:",  bg="white")
labelPass=Label(window, text="Password:",  bg="white")
labelWeb.grid(column=0,row=2)
labelEmail.grid(column=0,row=3)
labelPass.grid(column=0,row=4)



#Entries
website_entry=Entry(width=40)
email_entry=Entry(width=40)
password_entry=Entry(width=40)
website_entry.grid(column=1,row=2,columnspan=2)
email_entry.grid(column=1,row=3,columnspan=2)
password_entry.grid(column=1,row=4)
email_entry.insert(0,"fausto.renda@gmail.com")
website_entry.focus()


#Buttons
generate_password_button=Button(text="Generate Password", command=generate)
generate_password_button.grid(row=4,column=3)

button1=Button(text="Add", width=35, command=add_pass)
button1.grid(column=1,row=5, columnspan=1)

button2=Button(text="Search", width=15, command=search_pass)
button2.grid(column=3,row=2, columnspan=1)



window.mainloop()

