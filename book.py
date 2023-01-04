import mysql.connector
from tkinter import *
import tkinter as tk


def data():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='library')

    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM books;")
    result = cursor.fetchall()

    return result

def bBorrow():
    pass


def bReturn():
    pass



class Table:

    def __init__(self, root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, result[i][j])


# take the data
result = data()

total_rows = len(result)
total_columns = len(result[0])

root = Tk()
root.geometry("800x400")
root.title("Login Page")
t = Table(root)

Borrow = tk.Button(root, text="Borrow",
                      bg='white', command=bBorrow)
Borrow.place(x=600, y=360, width=55)

Return = tk.Button(root, text="Return",
                      bg='white', command=bReturn)
Return.place(x=700, y=360, width=55)


root.mainloop()
