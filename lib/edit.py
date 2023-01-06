import tkinter as tk
import mysql.connector
from tkinter import *


def bBorrow():

    sno = Username.get()
    if sno == "":
        print("Invalid Entry")
        exit()

    print(f"The Sno entered by you is {sno}")

    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='library')
    cursor = cnx.cursor()
    query = "UPDATE books SET Quantity = Quantity+1 WHERE Sno=\'"+sno+"\';"
    cursor.execute(query)
    cnx.commit()
    print("Book Borrowed")
    cursor.close()
    cnx.close()
    lblfrstrow = tk.Label(root, text="Book Borrowed", )
    lblfrstrow.place(x=350, y=250)


def rReturn():
    sno = Username.get()
    if sno == "":
        print("Invalid Entry")
        exit()

    print(f"The Sno entered by you is {sno}")

    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='library')
    cursor = cnx.cursor()
    query = "UPDATE books SET Quantity = Quantity-1 WHERE Sno=\'"+sno+"\';"
    cursor.execute(query)
    cnx.commit()
    print("Book Returned")
    cursor.close()
    cnx.close()
    lblfrstrow = tk.Label(root, text="Book Returned", )
    lblfrstrow.place(x=350, y=250)


root = tk.Tk()
root.geometry("800x400")
root.title("Edit Page")

# Defining the first row
lblfrstrow = tk.Label(root, text="Enter Sno-", )
lblfrstrow.place(x=250, y=100)

Username = tk.Entry(root, width=35)
Username.place(x=350, y=100, width=150)

Borrowbtn = tk.Button(root, text="Borrow",
                      bg='white', command=bBorrow)
Borrowbtn.place(x=350, y=200, width=55)

Returnbtn = tk.Button(root, text="Return",
                      bg='white', command=rReturn)
Returnbtn.place(x=450, y=200, width=55)

Exitbtn = tk.Button(root, text="Exit",
                      bg='white', command=exit)
Exitbtn.place(x=550, y=200, width=55)

root.mainloop()
