import customtkinter as ctk
from tkinter import messagebox

from log_in import log_in
from sign_up import sign_up
import userObj 



# Set appearance mode and color theme
ctk.set_appearance_mode("dark")  # Modes: "light" or "dark"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

# Function to handle sign-in action
def on_log_in():
    try:
        user = username_entry.get()
        password = password_entry.get()
        if log_in(user, password):
            messagebox.showinfo("Succes!" , "You have successfully logged in!")
            exit()

        else:
            messagebox.showwarning("Warning!","Incorrect Password!")
            password_entry.delete(0,"end")
    except userObj.userException as e:
            messagebox.showerror("Error" , e.message)
            username_entry.delete(0,"end")
            password_entry.delete(0,"end")


    
    

def on_sign_up():
    try:
        user = username_entry.get()
        password = password_entry.get()
        sign_up(user, password)
        messagebox.showinfo("Succes!" , "The User has been sucussfully signed up!")
    except userObj.userException as e:
        messagebox.showerror("Error" , e.message)
        username_entry.delete(0 , "end")
        password_entry.delete(0,"end")

    finally:
        display_log_in()


def clear_window():
    for widget in app.winfo_children():
        widget.destroy()

def display_sign_up():

    global username_entry, password_entry

    # Title Label
    title_label = ctk.CTkLabel(app, text="Sign Up", font=("Arial", 20))
    title_label.pack(pady=20)

    # Username Field
    username_label = ctk.CTkLabel(app, text="Username:")
    username_label.pack(pady=5)

    username_entry = ctk.CTkEntry(app, width=200)
    username_entry.pack(pady=5)

    # Password Field
    password_label = ctk.CTkLabel(app, text="Password:")
    password_label.pack(pady=5)

    password_entry = ctk.CTkEntry(app, width=200, show="*")
    password_entry.pack(pady=5)

    sign_up_button = ctk.CTkButton(app, text="Sign up", command=on_sign_up)
    sign_up_button.pack(pady=20)

    go_back_button = ctk.CTkButton(app, text="Go back", command=display_log_in)
    go_back_button.pack(pady=20)

    

def display_log_in():

    global username_entry, password_entry

    clear_window()
    # Title Label
    title_label = ctk.CTkLabel(app, text="Sign In", font=("Arial", 20))
    title_label.pack(pady=20)

    # Username Field
    username_label = ctk.CTkLabel(app, text="Username:")
    username_label.pack(pady=5)

    username_entry = ctk.CTkEntry(app, width=200)
    username_entry.pack(pady=5)

    # Password Field
    password_label = ctk.CTkLabel(app, text="Password:")
    password_label.pack(pady=5)

    password_entry = ctk.CTkEntry(app, width=200, show="*")
    password_entry.pack(pady=5)

    # Sign-In Button
    log_in_button = ctk.CTkButton(app, text="Log In", command=on_log_in)
    log_in_button.pack(pady=20)

    # Sign-up Button
    sign_up_button = ctk.CTkButton(app, text="No Account? Sign Up", command=switch_to_sign_up)
    sign_up_button.pack(pady=50)

def switch_to_sign_up():
    clear_window()
    display_sign_up()

# Initialize the main application window
app = ctk.CTk()
app.title("CustomTkinter Sign In")
app.geometry("500x450")
app.resizable(0,0)
# Title Label
title_label = ctk.CTkLabel(app, text="Sign In", font=("Arial", 20))
title_label.pack(pady=20)

# Username Field
username_label = ctk.CTkLabel(app, text="Username:")
username_label.pack(pady=5)

username_entry = ctk.CTkEntry(app, width=200)
username_entry.pack(pady=5)

# Password Field
password_label = ctk.CTkLabel(app, text="Password:")
password_label.pack(pady=5)

password_entry = ctk.CTkEntry(app, width=200, show="*")
password_entry.pack(pady=5)

# Sign-In Button
log_in_button = ctk.CTkButton(app, text="Log In", command=on_log_in)
log_in_button.pack(pady=20)

# Sign-up Button
sign_up_button = ctk.CTkButton(app, text="No Account? Sign Up", command=switch_to_sign_up)
sign_up_button.pack(pady=50)


def centre_window():
    app.update_idletasks()
    w = app.winfo_width()
    h = app.winfo_height()

    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    app.geometry("%dx%d+%d+%d" % (w, h, x, y))

centre_window()

# Run the application
app.mainloop()
