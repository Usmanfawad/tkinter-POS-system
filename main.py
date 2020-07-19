from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import tkinter as tk
from classes import *
import sqlite3


class main_interface:
    def __init__(self):
        self.load_data()
        self.login_screen()
        


    def load_data(self):
        conn=sqlite3.connect("subway.db")
        u=  conn.cursor()
        u.execute("SELECT * FROM users")
        for all in u.fetchall():
            Users(all[0],all[1],all[2])

    def login_screen(self):

        def proceed():
            # self.root.destroy()
            user_name = username.get()
            pass_word = password.get()
            for k,v in Users.users.items():
                try:
                    if user_name or pass_word == " " or "" or None:
                        messagebox.showerror("Error","Please fill complete information")
                        self.root.destroy()
                        self.login_screen() 
                        break;
                    if v.username.lower() == user_name.lower():
                        if int(v.password) == int(pass_word):
                            self.root.destroy()
                            self.main_screen()
                        else:
                            messagebox.showinfo("Password", "Wrong password")
                            self.root.destroy()
                            self.login_screen()
                            break;
                    else:
                        messagebox.showinfo("Username", "Wrong username")
                        self.root.destroy()
                        self.login_screen()
                except:
                    pass
        #this is the login screen that will be shown each time the user opens this software
        self.root = Tk()
        self.root.geometry("1300x1000")
        canvas = Canvas(self.root, width = 1300 , height = 400)
        canvas.pack()
        img = PhotoImage(file="Subway.png") 
        canvas.create_image(-130,-200, anchor = NW, image= img)
        username = tk.StringVar()
        password = tk.StringVar()
        label_1=Label(self.root,text="Username",font='Helvetica 20 italic',height=2, width=57, fg="black").pack()
        e1     =Entry(self.root,textvariable = username,width = 30).pack()
        label_2=Label(self.root,text="Password",font='Helvetica 20 italic',height=2, width=57, fg="black").pack()
        e2     =Entry(self.root,textvariable = password,show = "*",width = 30).pack()
        Button(self.root, text="Login",command = proceed, height=2, width=10, bg="#015643", fg="white").pack()
        self.root.mainloop()

    def main_screen(self):
        self.main = Tk()
        self.main.mainloop()


x = main_interface()