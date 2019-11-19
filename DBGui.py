from tkinter import *
import mysql.connector as mc
import re
import os


# server address: softwaredb.cqj4mkbkulv0.us-east-2.rds.amazonaws.com
# user: admin
# pass: testpassword

class Books:
#Book(ISBN, Title, Publish Date, Price)

    def AddBook(self, *args):
        e_isbn = self.i_isbn.get()
        e_title = self.i_title.get()
        e_PublishDate = self.i_pub.get()
        e_price = self.i_price.get()
        conn = mc.connect(user="admin", password="testpassword", host="softwaredb.cqj4mkbkulv0.us-east-2.rds.amazonaws.com", database="tester")
        cur = conn.cursor()
        cur.execute("insert into book(ISBN, Title, Publish Date, Price) values('"+e_isbn+"', '"+e_title+"', '"+e_PublishDate+"', '"+e_price+"')")
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

        isbnEntry = Entry(mainframe, width=7, textvariable=self.i_isbn)
        titleEntry = Entry(mainframe, width=7, textvariable=self.i_title)
        pubEntry = Entry(mainframe, width=7, textvariable=self.i_pub)
        priceEntry = Entry(mainframe, width=7, textvariable=self.i_price)

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

class Users:       
    def userlogin(self):
        ultk = Tk()
        ultk.wm_attributes("-fullscreen", True)
        ultk.title('User Login')
        #ulframe = Frame(ultk, width=400, height=400, background='white').grid()
        Label(ultk, text='User Login:', font =('Caviar Dreams',26)).grid(row=3, column=2)
        uusername = StringVar()
        upassword = StringVar()
        uu = Entry(ultk, width=20, textvariable=uusername).grid(row=4, column=3)
        up = Entry(ultk, width=20, textvariable=upassword).grid(row=5, column=3)
        Label(ultk, text='Username:', font =('Caviar Dreams',26)).grid(row=4, column=1)
        Label(ultk, text='Password:', font =('Caviar Dreams',26)).grid(row=5, column=1)
        ulogin = Button(ultk, text='Login', width=10, height=2, font =('Caviar Dreams',26), fg='black', command=lambda:[Users().user(), ultk.withdraw()]).grid(row=7, column =2)
        ulback = Button(ultk, text='Back',font =('Caviar Dreams' ,26), width=10, height=2, fg='black', command=lambda:[ultk.withdraw(),Main().tk.deiconify()]).grid(row=8, column = 2)
        
    def user(self):
        utk = Tk()
        utk.wm_attributes("-fullscreen", True)
        utk.title('User')
        usearch = StringVar(utk)
        usearchcat = StringVar(utk)
        usearchcat.set("Books")
        up = Entry(utk, width=20, textvariable=usearch).grid(row=5, column=4)
        Label(utk, text='Search for:', font =('Caviar Dreams',26)).grid(row=5, column=1)
        
        # The Drop Down Menu ... Super Pain
        OptionList = [ "Books", "Authors", "Genres"] 
        utk.wm_attributes("-fullscreen", True)
        usearchcat.set(OptionList[0])
        opt = OptionMenu(utk, usearchcat, *OptionList)
        opt.config(width=10, font=('Caviar Dreams', 12))
        opt.grid(row = 5, column = 2)

        # This would be a good place to put the show books on

def main():  
    tk = Tk()
    tk.wm_attributes("-fullscreen", True)
    tk.title('The Database') 
    menu = Menu(tk)
    tk.config(menu=menu)
    file = Menu(menu) #File - Exit
    file.add_command(label="Exit", command=tk.destroy)
    frame = Frame(tk, width=400, height=400, background='white')
    frame.pack_propagate(0)    
    frame.pack()
    Label(tk, text='Select a Sign In Option', font =('Caviar Dreams',36)).pack(side = TOP)
    # Logo that we created
    img = PhotoImage(file='librarylogo.png')
    pic = Label(frame, image=img)
    pic.pack(side = BOTTOM)

    #Buttons
    adminV = Button(tk, text='Admin Login', width=20, height=3, font =('Caviar Dreams',26), fg='black', command=lambda:[Admins().adminlogin(), tk.withdraw()]).pack()
    userV = Button(tk, text='User Login', width=20, height=3, font =('Caviar Dreams',26), fg='black', command=lambda:[Users().userlogin(), tk.withdraw()]).pack()

    tk.mainloop()
    mainloop() 

if __name__ == '__main__':
        main()
