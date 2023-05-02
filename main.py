import tkinter
from tkinter import ttk
from tkinter import messagebox


def enter_data():
    accepted = accept_var
    if accepted == "Accepted":
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            numCourses = courses_spinbox.get()
            numPeriods = gradingperiods_spinbox.get()
            registrationStatus = registered_check_var.get()
            print("Title: ", title, "First Name: ", firstname, "Last Name: ", lastname, "Age: ", age, "Nationality: ", nationality, "Number of Courses: ", numCourses, "Number of Grading Periods: ", numPeriods, "Registration Status: ", registrationStatus)
        

        else: 
            tkinter.messagebox.showwarning(title = "Error", message = "You have not entered your first and last name.")
    else: tkinter.messagebox.showwarning(title = "Error",  message = "You have not accepted the terms." )



window = tkinter.Tk()
window.title("Date Entry Form")

frame = tkinter.Frame(window)
frame.pack()

#saving user info 
user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row = 0, column = 0, padx = 20, pady = 10)

# Name labels 
first_name_label = tkinter.Label(user_info_frame, text = "First Name")
first_name_label.grid(row = 0, column = 0)
last_name_label = tkinter.Label(user_info_frame, text = "Last Name")
last_name_label.grid(row = 0, column = 1)

#name entry 
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row = 1, column = 0)
last_name_entry.grid(row = 1, column = 1)

#Title 
title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values = ["", "Mr.", "Mrs.", "Dr.", "Ms."])
title_label.grid(row = 0, column = 2)
title_combobox.grid(row = 1, column = 2)

#Age
age_label = tkinter.Label(user_info_frame, text = "Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row = 2, column = 0)
age_spinbox.grid(row = 3, column = 0)

#Nationality 
nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["African", "Antarctican", "Asian", "European", "North American", "Oceanian", "South American"])
nationality_label.grid(row = 2, column = 1)
nationality_combobox.grid(row = 3, column = 1)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

#Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)

#Registration Status 
registered_label = tkinter.Label(courses_frame, text = "Registration Status")
registered_check = tkinter.Checkbutton(courses_frame, text = "Currently Registered")
registered_label.grid(row = 0, column = 0)
registered_check.grid(row = 1, column = 0)

# num of courses
courses_label = tkinter.Label(courses_frame, text = "# Completed Courses")
courses_spinbox = tkinter.Spinbox(courses_frame, from_ =0, to =50)
courses_label.grid(row = 0, column = 1)
courses_spinbox.grid(row = 1, column = 1)

#Semesters/Periods
gradingperiod_label = tkinter.Label(courses_frame, text="# Grading Periods")
gradingperiod_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=30)
gradingperiod_label.grid(row = 0, column = 2)
gradingperiod_spinbox.grid(row = 1, column = 2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady = 5)
#T&C
terms_frame = tkinter.LabelFrame(frame, text = "Terms & Conditions")
terms_frame.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 10)
accept_var = tkinter.Stringvar(value = "Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text = "I accept the terms and conditions.")
terms_check.grid(row = 0, column = 0)

#Button
button = tkinter.Button(frame, text = "Enter data", command = enter_data)
button.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10)

window.mainloop() 