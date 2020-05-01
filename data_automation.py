from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import re
import requests
import os

from automate_images_download import automate_images_download

root=Tk()
root.geometry('900x700')
root.title("WELCOME TO DATASET AUTOMATION")
root.configure(bg='#f0af4f')


download_button_clicked = False

def download():
    global download_button_clicked
    if box1_string.get() == "" or box2_string.get() == "" or box3_string.get() == "":
        messagebox.showerror("Error", "Please enter something in the entry fields !")
        return

    dir_path = os.getcwd() + '\\' + box4_string.get()
    messagebox.showinfo("Info", f"Identified working directory : {dir_path}")
    messagebox.showinfo("Warning", "Please see cmd (terminal) for debug info !")
    m = automate_images_download()
    m.main_run_download(dir_path, box1_string.get(), box2_string.get(), box3_string.get())
    download_button_clicked = True

    if download_button_clicked:
        box5.config(state=NORMAL, cursor="xterm")
        box6.config(state=NORMAL, cursor="xterm")
        box7.config(state=NORMAL, cursor="xterm", show="*")



def sent_mail():
    if download_button_clicked:
        if box5_string.get() == "" or box6_string.get() == "" or box7_string.get() == "":
            messagebox.showerror("LOGINError", "Please Enter the CREDENTIALS !")
            return
        print("sending mail..")
        m1 = automate_images_download()
        m1.main_run_mail(box1_string.get(), box4_string.get(), box5_string.get(), box6_string.get(), box7_string.get())
    else:
        messagebox.showerror("Error", "Please Download the images first !")




label1 = Label(root, text="Query : ", font=('Arial', 20))
label1.grid(padx=10, pady=10, row=1, column=0, sticky='W')

label2 = Label(root, text="API KEY : ", font=('Arial', 20))
label2.grid(padx=10, pady=10, row=2, column=0, sticky='W')

label3 = Label(root, text="SEARCH_ENGINE ID : ", font=('Arial', 20))
label3.grid(padx=10, pady=10, row=3, column=0, sticky='W')

label4 = Label(root, text="Download folder name : ", font=('Arial', 20))
label4.grid(padx=10, pady=10, row=4, column=0, sticky='W')

label5 = Label(root, text="sender Email : ", font=('Arial', 20))
label5.grid(padx=10, pady=10, row=5, column=0, sticky='W')

label6 = Label(root, text="Receiver Email : ", font=('Arial', 20))
label6.grid(padx=10, pady=10, row=6, column=0, sticky='W')

label7 = Label(root, text="Email Password : ", font=('Arial', 20))
label7.grid(padx=10, pady=10, row=7, column=0, sticky='W')


box1_string =tk.StringVar(root)
box1 = Entry(root, textvariable = box1_string, font='Helvetica')
box1.grid(row=1, column=2)

box2_string =tk.StringVar(root)
box2 = Entry(root, textvariable = box2_string, show='*', font='Helvetica')
box2.grid(row=2, column=2)

box3_string =tk.StringVar(root)
box3 = Entry(root, textvariable = box3_string, show='*', font='Helvetica')
box3.grid(row=3, column=2)

box4_string =tk.StringVar(root)
box4 = Entry(root, textvariable = box4_string, font='Helvetica')
box4.grid(row=4, column=2)


box5_string =tk.StringVar(root)
box5 = Entry(root, textvariable = box5_string, font='Helvetica')
box5.grid(row=5, column=2)
box5.config(state=DISABLED, cursor="circle")


box6_string =tk.StringVar(root)
box6 = Entry(root, textvariable = box6_string, font='Helvetica')
box6.grid(row=6, column=2)
box6.config(state=DISABLED, cursor="circle")


box7_string =tk.StringVar(root)
box7 = Entry(root, textvariable = box7_string, show='*', font='Helvetica')
box7.grid(row=7, column=2)
box7.config(state=DISABLED, cursor="circle")

button1_font = font.Font(size=15)
button1 = Button(root, text="Download", command=download, width=15, height=3, activebackground='#87dce0')
button1['font'] = button1_font
button1.grid(padx=10, pady=20, row=10, column=1)

button2_font = font.Font(size=15)
button2 = Button(root, text="MAIL", command=sent_mail, width=10, height=3, activebackground='#87dce0')
button2['font'] = button2_font
button2.grid(padx=10, pady=20, row=11, column=1)


mainloop()
