import sqlite3
from tkinter import *
from tkinter import messagebox


# Step 1: Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect('college_registration.db')
cursor = conn.cursor()

# Step 2: Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    course TEXT,
    email TEXT,
    contact TEXT
)
''')
conn.commit()

# Step 3: Function to submit data
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    course = entry_course.get()
    email = entry_email.get()
    contact = entry_contact.get()

    if not (name and age and gender and course and email and contact):
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    cursor.execute("INSERT INTO students (name, age, gender, course, email, contact) VALUES (?, ?, ?, ?, ?, ?)", 
                   (name, age, gender, course, email, contact))
    conn.commit()
    messagebox.showinfo("Success", "Registration Successful!")
    clear_fields()

def clear_fields():
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    gender_var.set(None)
    entry_course.delete(0, END)
    entry_email.delete(0, END)
    entry_contact.delete(0, END)

# Step 4: GUI using tkinter
root = Tk()
root.title("College Registration Form")
root.geometry("400x400")
root.config(bg="Lavender")


# Labels and Entries
Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky=W)
entry_name = Entry(root)
entry_name.grid(row=0, column=1)

Label(root, text="Age").grid(row=1, column=0, padx=10, pady=5, sticky=W)
entry_age = Entry(root)
entry_age.grid(row=1, column=1)

Label(root, text="Gender").grid(row=2, column=0, padx=10, pady=5, sticky=W)
gender_var = StringVar()
Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky=W)
Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=1, padx=60, sticky=W)

Label(root, text="Course").grid(row=3, column=0, padx=10, pady=5, sticky=W)
entry_course = Entry(root)
entry_course.grid(row=3, column=1)

Label(root, text="Email").grid(row=4, column=0, padx=10, pady=5, sticky=W)
entry_email = Entry(root)
entry_email.grid(row=4, column=1)

Label(root, text="Contact No.").grid(row=5, column=0, padx=10, pady=5, sticky=W)
entry_contact = Entry(root)
entry_contact.grid(row=5, column=1)

# Submit Button
Button(root, text="Submit",bg="green",fg="white" ,command=submit_form).grid(row=6, column=1, pady=20)

root.mainloop()

# Close DB connection when done
conn.close()
