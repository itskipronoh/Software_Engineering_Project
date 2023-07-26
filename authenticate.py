import tkinter
from tkinter import ttk
from tkinter import messagebox

def authenticate():
    username = username_entry.get()
    password = password_entry.get()

    # Replace these with your actual authentication logic
    valid_username = "admin"
    valid_password = "1234"

    if username == valid_username and password == valid_password:
        # If authentication is successful, hide the login window and show the main window
        login_window.withdraw()
        window.deiconify()
    else:
        messagebox.showerror("Authentication Failed", "Invalid username or password")

def submit_data():
    # Your existing submit_data function code here...
    pass

# Create the login window
login_window = tkinter.Tk()
login_window.title("Login")

username_label = tkinter.Label(login_window, text="Username")
password_label = tkinter.Label(login_window, text="Password")
username_entry = tkinter.Entry(login_window)
password_entry = tkinter.Entry(login_window, show="*")
login_button = tkinter.Button(login_window, text="Login", command=authenticate)

username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()

# Hide the main window initially
window = tkinter.Tk()
window.title("University-Dispensary-Attendance")
window.withdraw()

# Rest of your main window code (same as before)...

window.mainloop()
