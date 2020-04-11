from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import re
import requests
import os

from automate_images_download import automate_images_download
from SEND_EMAIL import EMAIL

root=Tk()
root.geometry('800x500')
root.title("WELCOME TO DATASET AUTOMATION")
root.configure(bg='#f0af4f')

def download():
    if box1_string.get() == "" or box2_string.get() == "" or box3_string.get() == "":
        messagebox.showerror("showerror", "Please enter something in the entry fields !")
        return
    dir_path = os.getcwd() + r'\sourav_image'
    messagebox.showinfo("Info", f"Identified working directory : {dir_path}")
    messagebox.showinfo("Warning", "Please see cmd (terminal) for debug info !")
    m = automate_images_download()
    m.main_run(dir_path, box1_string.get(), box2_string.get(), box3_string.get())



label1 = Label(root, text="Query : ", font=('Arial', 20))
label1.grid(padx=10, pady=10, row=1, column=0, sticky='W')

label2 = Label(root, text="API KEY : ", font=('Arial', 20))
label2.grid(padx=10, pady=10, row=2, column=0, sticky='W')

label3 = Label(root, text="SEARCH_ENGINE ID : ", font=('Arial', 20))
label3.grid(padx=10, pady=10, row=3, column=0, sticky='W')

# label4 = Label(root, text="Sender Email : ", font=('Arial', 20))
# label4.grid(padx=10, pady=10, row=4, column=0, sticky='W')
#
# label5 = Label(root, text="Receiver Email : ", font=('Arial', 20))
# label5.grid(padx=10, pady=10, row=5, column=0, sticky='W')
#
# label6 = Label(root, text="Email Password : ", font=('Arial', 20))
# label6.grid(padx=10, pady=10, row=6, column=0, sticky='W')

box1_string =tk.StringVar(root)
box1 = Entry(root, textvariable = box1_string, font='Helvetica')
box1.grid(row=1, column=2)

box2_string =tk.StringVar(root)
box2 = Entry(root, textvariable = box2_string, show='*', font='Helvetica')
box2.grid(row=2, column=2)

box3_string =tk.StringVar(root)
box3 = Entry(root, textvariable = box3_string, show='*', font='Helvetica')
box3.grid(row=3, column=2)

# box4_string =tk.StringVar(root)
# box4 = Entry(root, textvariable = box4_string, font='Helvetica')
# box4.grid(row=4, column=2)
#
# box5_string =tk.StringVar(root)
# box5 = Entry(root, textvariable = box5_string, font='Helvetica')
# box5.grid(row=5, column=2)
#
# box6_string =tk.StringVar(root)
# box6 = Entry(root, textvariable = box6_string, show='*', font='Helvetica')
# box6.grid(row=6, column=2)

button1_font = font.Font(size=15)
button1 = Button(root, text="Download", command=download, width=15, height=3, activebackground='#87dce0')
button1['font'] = button1_font
button1.grid(padx=10, pady=20, row=10, column=1)


e = EMAIL()
button2_font = font.Font(size=15)
button2 = Button(root, text="SEND AS EMAIL", command=lambda : e.EMAIL_window(root))
button2['font'] = button2_font
button2.grid(padx=10, pady=20, row=12, column=1)

# button3 = Button(root, text="Signup", command=retrieve_input)
# button3.grid(padx=10, pady=20, row=7, column=1)



# button2 = Button(root, text="Upload Image", command=retrieve_input)
# button2.grid(padx=10, pady=20, row=9, column=3)

# textBox=Text(root, height=2, width=10)
# textBox.pack()
# buttonCommit=Button(root, height=1, width=10, text="Commit", command=retrieve_input)
# buttonCommit.pack()

mainloop()
