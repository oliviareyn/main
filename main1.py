import tkinter
from tkinter import ttk 
from tkinter import messagebox
import os
import openpyxl1

def enter_data():
    accepted = terms_check_var.get()

    if accepted == "Accepted":
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            registration_status = reg_status_var.get()
            courses = courses_spinbox.get()
            semesters = semesters_spinbox.get()

            print("Title: ", title, "First name: ", firstname, "Last name: ", lastname, "Age: ", age, "Nationality: ", nationality, "Number of courses: ", courses, "Number of Semesters: ", Semesters, "Registration Status: ", registration_status)
            print("---------------------------------------------------------------------------")

            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = ["First Name", "Last Name", "Title", "Age", "Nationality", "# Courses", "# Semesters", "Registration Status"]
                sheet.append(heading)
                workbook.save(filepath)
                workbook = openpyxl.load_workbook(filepath)
                sheet = workbook.active
                sheet.append([firstname, lastname, title, age, nationality, courses, semesters, registration_status])
                workbook.save(filepath)
        else:   
            tkinter.messagebox.showwarning(title = "Error", message = "First name and last name are required.")
    else:
        tkinter. messagebox.showwarning(title = "Error", message = "You have not accepted the terms.")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Tk()
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid( row = 0, column = 0, padx = 20, pady = 20)

first_name_label = tkinter.Label(user_info_frame, text = "First Name")
first_name_label.grid( row = 0, column = 0, padx = 20, pady = 20)
last_name_label = tkinter.Label(user_info_frame, text = "Last name")
last_name_label.grid(row = 0, column = 1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row = 1, column = 0)
last_name_entry.grid(row = 1, column = 1)

title_label = tkinter.Label(user_info_frame, text = "Title")
title_combobox = ttk.Combobox(user_info_fra,e, value=["", "Mrs.", "Ms.", "Mr.", "Dr."])
title_label.grid(row = 0 , column = 2)
title_combobox.grid(row= 1, column = 2)

age_label = tkinter.Label(user_info_frame, text = "Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=100)
age_label.grid(row = 2, column = 0)
age_spinbox.grid(row =3, column = 0)

nationality_label = tkinter.Label(user_info_frame, text = "Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values = ["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_label.grid(row = 2, column = 1)
nationality_combobox.grid(row = 3, column = 1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)

registered_label = tkinter.Label(courses_frame, text = "Registration Status")
reg_status_var = tkinter.StringVar(value = "Not Registered")
registered_label.grid(row = 0, column = 0)
registered_check = tkinter.Checkbutton(courses_frame, text = "Currently Registered", variable = reg_status_var, onvalue = "Registered", offvalue = "Not registered")
registered_check.grid(row = 1, column = 0)

courses_label = tkinter.Label(courses_frame, text = "# Completed Courses")
courses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=50)
courses_label.grid(row = 0, column = 1)
courses_spinbox.grid(row = 1, column = 1)

semesters_label = tkinter.Label(courses_frame, text = "# Semesters")
semesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=10)
semesters_label.grid(row = 0, column = 2)
semesters_spinbox.grid(row = 1, column = 2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

terms_frame = tkinter.LabelFrame(frame, text = "terms & conditions")
terms_frame.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 20)

terms_check_var = tkinter.StringVar(value = "Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text = "I accept the terms and conditions.", variable = terms_check_var, onvalue = "Accepted", offvalue = "Not Accepted")
terms_check.grid(row = 0, column = 0, padx = 10, pady = 5)

button = tkinter.Button(frame, text = "Enter data", command = enter_data)
button.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10)

window.mainloop()

