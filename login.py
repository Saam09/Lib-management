from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)


frame = Frame(root, width=305, height=350, bg="white")
frame.place(x=300, y=70)

heading = Label(frame, text='Sign In', fg='#57a1f8',
                bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# ----------------------------------------------
user = Entry(frame, width=25, fg='black', border=0,
             bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')

Frame(frame, width=295, height=2, bg='black').place(x=25, y=110)
# ----------------------------------------------
code = Entry(frame, width=25, fg='black', border=0,
             bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')

Frame(frame, width=295, height=2, bg='black').place(x=25, y=180)

#########################################################

Button(frame, width=35, pady=7, text="Sign in",
       bg='#57a1f8', fg='white', border=0).place(x=35, y=204)


root.mainloop()
