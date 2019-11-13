from tkinter import *
import mysql.connector as mc
import tkinter.messagebox as tm
import re
import os


# server address: softwaredb.cqj4mkbkulv0.us-east-2.rds.amazonaws.com
# user: admin
# pass: testpassword

class Books:


#Book(ISBN, Title, Publish Date, Price)
    def AddBook(self, *args):
        e_isbn = i_isbn.get()
        e_title = i_title.get()
        e_PublishDate = i_pub.get()
        e_price = i_price.get()
        conn = mc.connect(user="admin", password="testpassword", host="softwaredb.cqj4mkbkulv0.us-east-2.rds.amazonaws.com", database="book_test")
        cur = conn.cursor()
        cur.execute("insert into Book(book_isbn, book_title, book_PublishDate book_price) values('"+e_code+"', '"+e_title+"', '"+e_PublishDate+"', '"+e_price+"')")
        conn.close()

    def Book(self):
        btk = Tk()
        btk.wm_attributes("-fullscreen", True)
        btk.title("GET DATA")

        mainframe = Frame(btk)
        mainframe.pack()

        i_isbn = IntVar()
        i_title = StringVar()
        i_pub = StringVar()
        i_price = IntVar()

        isbnEntry = Entry(mainframe, width=7, textvariable=i_isbn)
        titleEntry = Entry(mainframe, width=7, textvariable=i_title)
        pubEntry = Entry(mainframe, width=7, textvariable=i_pub)
        priceEntry = Entry(mainframe, width=7, textvariable=i_price)

        isbnEntry.grid(row=4, column=1)
        titleEntry.grid(row=5, column=1)
        pubEntry.grid(row=6, column=1)
        priceEntry.grid(row=7, column=1)

        Label(mainframe, text='Book ISBN', font =('Caviar Dreams',26)).grid(row=4, column=0)
        Label(mainframe, text='Book Title', font =('Caviar Dreams',26)).grid(row=5, column=0)
        Label(mainframe, text='Book Publish Date', font =('Caviar Dreams',26)).grid(row=6, column=0)
        Label(mainframe, text='Book Price', font =('Caviar Dreams',26)).grid(row=7, column=0)

        Button(mainframe, text="Insert", command=Books().AddBook()).grid(row=8, column=1)

class Admins:       
    def adminlogin(self):
        altk = Tk()
        altk.wm_attributes("-fullscreen", True)
        altk.title('Admin Login')
        Label(altk, text='Admin Login:', font =('Caviar Dreams',26)).grid(row=3, column=2)
        adminusername = StringVar()
        adminpassword = StringVar()
        au = Entry(altk, width=20, textvariable=adminusername).grid(row=4, column=3)
        ap = Entry(altk, width=20, textvariable=adminpassword).grid(row=5, column=3)
        Label(altk, text='Username:', font =('Caviar Dreams',26)).grid(row=4, column=1)
        Label(altk, text='Password:', font =('Caviar Dreams',26)).grid(row=5, column=1)
        alogin = Button(altk, text='Login', width=10, height=2, font =('Caviar Dreams',26), fg='black', command=lambda:[Admins().admin(), altk.withdraw()]).grid(row=7, column =2)
    
        
    def admin(self):
        atk = Tk()
        atk.wm_attributes("-fullscreen", True)
        atk.title('Admin')
        addBook = Button(atk, text='Add a Book', width=20, height=3, font =('Caviar Dreams',26), fg='black', command=lambda:[Books().Book(), atk.withdraw()]).pack()

def main():  
    tk = Tk()
    tk.wm_attributes("-fullscreen", True)
    tk.title('The Database') 
    menu = Menu(tk)
    tk.config(menu=menu)
    file = Menu(menu) #File - Exit
    file.add_command(label="Exit", command=tk.destroy)
    frame = Frame(tk, width=800, height=600, background='white')
    frame.pack_propagate(0)    
    frame.pack()
    # Logo that we created
    #img = PhotoImage(file='ivancicitalianv2.png')
    #pic = Label(frame, image=img)
    #pic.pack()

    #Buttons
    adminV = Button(tk, text='Admin Login', width=20, height=3, font =('Caviar Dreams',26), fg='black', command=lambda:[Admins().adminlogin(), tk.withdraw()]).pack()
    #userV = Button(tk, text='User Login', width=20, height=3, font =('Caviar Dreams',26), fg='black', command=lambda:[admin(), tk.withdraw()]).pack()

    tk.mainloop()
    mainloop() 

if __name__ == '__main__':
        main()
