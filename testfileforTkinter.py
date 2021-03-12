#import tkinter as tk
#from tkinter import *


#class LoginScreen:
    #def __init__(self, game):
        #self.game = game



#window = tk.Tk()
#label = tk.Label(
    #text="Type your username",
    #foreground="black",  # Set the text color to white
    #background="misty rose",
    #width = 20,
    #height = 10)  # Set the background color to black

#button = tk.Button(
    #text="Click me!",
    #width=20,
    #height=5,
    #bg="misty rose",
    #fg="indian red",)

#entry = tk.Entry(fg="black", bg="misty rose", width=20)
#name = entry.get()

#label.pack()
#entry.pack()
#button.pack()

#window.mainloop()


from tkinter import *
from functools import partial
import pyodbc

class Login:
    def __init__(self):
        self.tkWindow = Tk()
        self.tkWindow.geometry('400x150')
        self.tkWindow.title('Tkinter Login Form - pythonexamples.org')

    #def validateLogin(username, password):
    #	print("username entered :", username.get())
    #	print("password entered :", password.get())
    #	return


    def saveUsername(username):
        conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=LAPTOP-5818FKV9\SQLEXPRESS;'
                                'Database=QuizDB;'
                                'Trusted_Connection=Yes;')
        cursor = conn.cursor()
        #cursor.execute('SELECT * FROM Users')
        #username = cursor.execute('INSERT INTO Users (Username) VALUES (?), (usernameEntry)')
        #conn.commit()


        Username = self.usernameEntry
        Paassword = passwordEntry
        cursor.execute("""
        INSERT INTO Users(Username, Paassword)
        VALUES (?,?)
        """, (Username, Paassword))
        conn.commit ()

    #window
    tkWindow = Tk()
    tkWindow.geometry('400x150')
    tkWindow.title('Tkinter Login Form - pythonexamples.org')

    #username label and text entry box
    def login(self):
        usernameLabel = Label(self.tkWindow, text="User Name").grid(row=0, column=0)
        username = StringVar()
        self.usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)
        self.usernameEntry = saveUsername(username)

    #password label and password entry box
    passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

    #validateLogin = partial(validateLogin, login(), password)

    #login button
    #loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

    tkWindow.mainloop()
