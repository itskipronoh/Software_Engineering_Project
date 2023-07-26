

import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import mysql.connector






def authenticate():
    username = username_entry.get()
    password = password_entry.get()

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dispensary"
    )

    cursor = db.cursor()

    query = "SELECT * FROM login WHERE username=%s AND password=%s"
    values = (username, password)

    cursor.execute(query, values)
    user = cursor.fetchone()

    if user:
        login_window.withdraw()
        window.deiconify()
    else:
        messagebox.showerror("Authentication Failed", "Invalid username or password")

    cursor.close()
    db.close()

def sign_up():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dispensary"
    )

    cursor = db.cursor()

    query = "INSERT INTO login (username, password) VALUES (%s, %s)"
    values = (new_username, new_password)

    cursor.execute(query, values)
    db.commit()

    messagebox.showinfo("Success", "User created successfully!")

    new_username_entry.delete(0, tk.END)
    new_password_entry.delete(0, tk.END)

    cursor.close()
    db.close()

def show_signup_window():
    global signup_window
    signup_window = tk.Toplevel(window)
    signup_window.title("Sign Up")

    new_username_label = ttk.Label(signup_window, text="Enter New Username:")
    new_username_label.pack()
    global new_username_entry
    new_username_entry = ttk.Entry(signup_window)
    new_username_entry.pack(pady=5)

    new_password_label = ttk.Label(signup_window, text="Enter New Password:")
    new_password_label.pack()
    global new_password_entry
    new_password_entry = ttk.Entry(signup_window, show="*")
    new_password_entry.pack(pady=5)

    signup_button = ttk.Button(signup_window, text="Sign Up", command=sign_up)
    signup_button.pack(pady=10)
    
    
def submit_data():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    gender = gender_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()
    NHIF_label = NHIF_label_combobox.get()

    print("First Name:", firstname, "Last Name:", lastname, "Gender:", gender)
    print("Age:", age, "Nationality:", nationality, "NHIF:", NHIF_label)

# Create the login window
login_window = tk.Tk()
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

frame = tkinter.Frame(window)
frame.pack()


# Don't have an account label
dont_have_account_label = ttk.Label(login_window, text="Don't have an account?")
dont_have_account_label.pack(pady=5)

# Sign Up button
sign_up_button = ttk.Button(login_window, text="Sign Up", command=show_signup_window)
sign_up_button.pack(pady=10)




#saving student information

student_information_frame = tkinter.LabelFrame(frame, text="student information")
student_information_frame.grid(row= 0, column= 0, padx=20, pady=10 )


first_name_label = tkinter.Label(student_information_frame,text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = tkinter.Label (student_information_frame, text="Last Name")
last_name_label.grid(row= 0, column =1)


first_name_entry =tkinter.Entry(student_information_frame)
last_name_entry =tkinter.Entry(student_information_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

gender_label = tkinter.Label(student_information_frame ,text="gender")
gender_combobox = ttk.Combobox(student_information_frame, values = ["male","female",])
gender_label.grid(row= 0, column= 2)
gender_combobox.grid(row=1, column = 2)


age_label =tkinter.Label(student_information_frame, text="age")
age_spinbox = tkinter.Spinbox(student_information_frame, from_= 17,to= 60)
age_label.grid(row=3,column=0)
age_spinbox.grid(row=4, column=0)

nationality_label = tkinter.Label(student_information_frame, text="Nationality")
nationality_combobox = ttk.Combobox(student_information_frame, values=["African","Asian","European"])
nationality_label.grid(row=3, column=1)
nationality_combobox.grid(row=4, column=1)

NHIF_label = tkinter.Label(student_information_frame, text="nhif card")
NHIF_label_combobox = ttk.Combobox(student_information_frame, values=["YES","NO"])
NHIF_label.grid(row=3,column=2)
NHIF_label_combobox.grid(row=4,column=2)

for widget in student_information_frame.winfo_children():
    widget.grid(padx=10, pady=5)


#courses registration information
course_frame = tkinter.LabelFrame(frame)
course_frame.grid(row=1,column=0, sticky="news",padx=20,pady=10)


registered_label= tkinter.Label(course_frame,text="Reistration Status")
registered_check = tkinter.Checkbutton(course_frame,text="Currently Registerd")
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

semesters_label = tkinter.Label(course_frame , text="# Semester")
semesters_spinbox = tkinter.Spinbox(course_frame,from_=0, to="infinity")
semesters_label.grid(row=0,column=1)
semesters_spinbox.grid(row=1, column=1)


student_number_label = tkinter.Label(course_frame ,text="Student Number")
student_number_Entry = tkinter.Entry(course_frame,text="Student Number")
student_number_label.grid(row=0, column=2)
student_number_Entry.grid(row=1, column=2)



for widget in course_frame.winfo_children():
    widget.grid(padx=10, pady=5)



# Accept terms

terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="new", padx=20, pady=20)

# Enter data

button = tkinter.Button(frame, text="Submit Data", command=submit_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# Start the main event loop
window.mainloop()