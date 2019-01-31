from tkinter import *
import serverCode as sc


#Creating wrapper function to add student to database
def add_student():
    if name_value.get():
        sc.insert(name_value.get(), roll_value.get(), section_value.get(), grade_value.get())
        listbox.delete(0, END)
        listbox.insert(END, (name_value.get(), roll_value.get(), section_value.get(), grade_value.get()))



#Creating a wrapper function to view all the student
def view_all_student():
    all_student_data = sc.view()
    listbox.delete(0, END)
    for item in all_student_data:
        listbox.insert(END, item)
    input_1.delete(0, END)
    input_2.delete(0, END)
    input_3.delete(0, END)
    input_4.delete(0, END)


#Creating a wrapper function to search individual student
def search_student():
    if name_value.get():
        student_data = sc.search(name_value.get())
        listbox.delete(0, END)
        for data in student_data:
            listbox.insert(END, data)


#Creating a wrapper function to update a student record
def update_student():
    if name_value.get():
        updated_student_data = sc.update(name_value.get(), roll_value.get(), section_value.get(), grade_value.get())
        listbox.delete(0, END)
        for item in sc.search(name_value.get()):
            listbox.insert(END, item)


#Creating a wrapper function to delete a student record
def delete_student():
    if name_value.get():
        sc.delete(name_value.get())


#Function for catching the selected list and update the student record
def selected_student_record(event):
    global student_record_selected_from_list
    index=listbox.curselection()[0]
    student_record_selected_from_list = listbox.get(index)
    input_1.delete(0,END)
    input_1.insert(END,student_record_selected_from_list[0])
    input_2.delete(0,END)
    input_2.insert(END,student_record_selected_from_list[1])
    input_3.delete(0,END)
    input_3.insert(END,student_record_selected_from_list[2])
    input_4.delete(0,END)
    input_4.insert(END,student_record_selected_from_list[3])




# Initialize  the window
window = Tk()

window.wm_title('Class Room')



# Creating label with Label class
label_1 = Label(text='Name', width=17)
label_1.grid(row=0,column=0)

label_2 = Label(text='Section', width=17)
label_2.grid(row=1,column=0)

label_3 = Label(text='Roll', width=17)
label_3.grid(row=0,column=2)

label_4 = Label(text='Grade', width=17)
label_4.grid(row=1,column=2)


# Creating input field with Entry class
name_value=StringVar()
input_1 = Entry(window, textvariable=name_value)
input_1.grid(row=0,column=1)

roll_value=StringVar()
input_2 = Entry(window, textvariable=roll_value)
input_2.grid(row=0,column=3)

section_value=StringVar()
input_3 = Entry(window, textvariable=section_value)
input_3.grid(row=1,column=1)

grade_value=StringVar()
input_4 = Entry(window, textvariable=grade_value)
input_4.grid(row=1,column=3)




# Create button with Button class
button_1 = Button(window, text='View All Student', width=17, command=view_all_student)
button_1.grid(row=2,column=3)

button_2 = Button(window, text='Search Student' , width=17, command=search_student)
button_2.grid(row=3,column=3)

button_3 = Button(window, text='Add Student', width=17, command=add_student)
button_3.grid(row=4,column=3)

button_4 = Button(window, text='Update Selected', width=17, command=update_student)
button_4.grid(row=5,column=3)

button_5 = Button(window, text='Delete Selected', width=17, command=delete_student)
button_5.grid(row=6,column=3)

button_6 = Button(window, text='Exit', width=17, background='#FF0000', command=window.destroy)
button_6.grid(row=7,column=3)



# Creating a Listbox with Listbox class
listbox = Listbox(window, height=12, width=50)
listbox.grid(row=2, rowspan=6, column=0, columnspan=2)

#Creating a scrollbar
scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

#configure the scrollbar with listbox
listbox.configure(yscrollcommand=scroll.set)
scroll.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', selected_student_record)

# Running the window and widget as loop (???)
window.mainloop()
