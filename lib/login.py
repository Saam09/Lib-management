import tkinter as tk
import mysql.connector
from tkinter import *


def submitact():

    user = Username.get()
    passw = password.get()

    if user == "" or passw == "":
        exit()

    print(f"The name entered by you is {user} {passw}")

    logintodb(user, passw)


def logintodb(user, passw):
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='library')
    # query1 = ("SELECT username FROM admin_details WHERE username=%s;",mail)
    cursor = cnx.cursor()
    cursor.execute(
        "SELECT password FROM admin WHERE username =\'"+user+"\';")
    dbPassword = cursor.fetchone()
    if dbPassword == []:
        return False
    else:
        x = dbPassword[0]
        if passw == x:
            print("Password Matched")
            return True
        else:
            print("Invalid Username or Password")
    return False


root = tk.Tk()
root.geometry("800x400")
root.title("Login Page")


# Defining the first row
lblfrstrow = tk.Label(root, text="Username -", )
lblfrstrow.place(x=250, y=100)

Username = tk.Entry(root, width=35)
Username.place(x=350, y=100, width=150)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.place(x=250, y=150)

password = tk.Entry(root, width=35)
password.place(x=350, y=150, width=150)

submitbtn = tk.Button(root, text="Login",
                      bg='white', command=submitact)
submitbtn.place(x=350, y=200, width=55)

root.mainloop()
