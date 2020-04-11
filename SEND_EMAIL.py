from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import re
import requests
import os
from automate_images_download import automate_images_download

class EMAIL:
    def send(self):
        dir_path = os.getcwd() + r'\sourav_image'
        zipped_path = dir_path+'/images.zip'
        subject = "An email with attachment from Python"
        body = f"This is an email with zipped attachment of 100 images downloaded for the given query."

        m1 = automate_images_download()
        m1.resize_images(dir_path)
        m1.convert_images(dir_path)
        m1.zip_images(dir_path)
        m1.sent_mail(zipped_path, subject, body, self.box4_string.get(), self.box5_string.get(), self.box6_string.get())



    def EMAIL_window(self, root):
        window = tk.Toplevel(root)
        window.geometry('600x300')
        window.title("ENTER EMAIL CREDENTIALS")
        window.configure(bg='#f72835')

        label4 = Label(window, text="Sender Email : ", font=('Arial', 20))
        label4.grid(padx=10, pady=10, row=1, column=0, sticky='W')

        label5 = Label(window, text="Receiver Email : ", font=('Arial', 20))
        label5.grid(padx=10, pady=10, row=2, column=0, sticky='W')

        label6 = Label(window, text="Email Password : ", font=('Arial', 20))
        label6.grid(padx=10, pady=10, row=3, column=0, sticky='W')

        self.box4_string =tk.StringVar(window)
        box4 = Entry(window, textvariable = self.box4_string, font='Helvetica')
        box4.grid(row=1, column=2)

        self.box5_string =tk.StringVar(window)
        box5 = Entry(window, textvariable = self.box5_string, font='Helvetica')
        box5.grid(row=2, column=2)

        self.box6_string =tk.StringVar(window)
        box6 = Entry(window, textvariable = self.box6_string, show='*', font='Helvetica')
        box6.grid(row=3, column=2)

        button3_font = font.Font(size=15)
        button3 = Button(window, text="SEND", command=self.send)
        button3['font'] = button3_font
        button3.grid(padx=10, pady=20, row=6, column=2)
