from tkinter import *
import os
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3 as sq
root = Tk()
root.geometry("2300x1200")

root.title("Newspaper Agency Automatic System")

usertype_label = Label(root, text="MASTER'S NEWSPAPER AGENCY",font=("Arial",15), pady=20)
usertype_label.grid(row=0, column=2)

create=sq.connect("registration.db")
cursor=create.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS SUBCRIPTION(
        Username str(15),
        Global_Magazine int,
        Global_Newspaper int,
        National_Magazine int,
        Bill int
    );''')

cursor.execute('''CREATE TABLE IF NOT EXISTS JOIN1(
        Name str(15),
        Phonenumber str(15),
        Doornumber str(15),
        Colony str(15),
        Distance int,
        Username str(15),
        Password str(15),
        Global_Magazine int,
        Global_Newspaper int,
        National_Magazine int,
        Bill int
    );''')

def register():
    cursor.execute('''CREATE TABLE IF NOT EXISTS REGISTRATION(
        Name str(15),
        Phonenumber str(15),
        Doornumber str(15),
        Colony str(15),
        Distance int,
        Username str(15),
        Password str(15)
    );''')

    global register_screen
    register_screen = Toplevel(root)
    register_screen.title("Register")
    register_screen.geometry("2300x1200")

    global username
    global password
    global name
    global colony
    global phonenumber
    global doornumber
    global distance
    global username_entry
    global password_entry
    global name_entry
    global colony_entry
    global phonenumber_entry
    global doornumber_entry
    global distance_entry
    
    name = StringVar()
    phonenumber = StringVar()
    colony = StringVar()
    doornumber = StringVar()
    distance = IntVar()
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="yellow").pack()
    Label(register_screen, text="").pack()

    name_lable = Label(register_screen, text="Name * ")
    name_lable.pack()
    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()
    phonenumber_lable = Label(register_screen, text="Phonenumber * ")
    phonenumber_lable.pack()
    phonenumber_entry = Entry(register_screen, textvariable=phonenumber)
    phonenumber_entry.pack()
    doornumber_lable = Label(register_screen, text="Doornumber * ")
    doornumber_lable.pack()
    doornumber_entry = Entry(register_screen, textvariable=doornumber)
    doornumber_entry.pack()
    colony_lable = Label(register_screen, text="Colony * ")
    colony_lable.pack()
    colony_entry = Entry(register_screen, textvariable=colony)
    colony_entry.pack()
    distance_lable = Label(register_screen, text="Distance * ")
    distance_lable.pack()
    distance_entry = Entry(register_screen, textvariable=distance)
    distance_entry.pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
   
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register",   width=10, height=1,bg="blue", command=register_user).pack()
    Button(register_screen, text="Back",  width=10, height=1,bg="blue", command=register_screen.destroy).pack()
    
def register_user():
    name_info = name.get()
    phonenumber_info = phonenumber.get()
    doornumber_info = doornumber.get()
    colony_info = colony.get()
    distance_info = distance.get()
    username_info = username.get()
    password_info = password.get()

    le=[name_info,phonenumber_info,doornumber_info,colony_info,distance_info,username_info,password_info]

    cursor.execute('''INSERT INTO REGISTRATION (Name,Phonenumber,Doornumber,Colony,Distance,Username,Password) 
                    VALUES(?,?,?,?,?,?,?);''',le)
    create.commit()
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


def login_m():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("2300x1200")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_m
    global password_m
    username_m = StringVar()
    password_m = StringVar()

    global username_entry
    global password_entry

    Label(login_screen, text="Username * ").pack()
    username_entry = Entry(login_screen, textvariable=username_m)
    username_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_entry = Entry(login_screen, textvariable=password_m, show='*')
    password_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=same_m).pack()
    Button(login_screen, text="Back", width=10, height=1, command=login_screen.destroy).pack()
def logout_m():
    manager_screen.destroy()
def same_m():
    global username_man
    global password_man
    username_man= username_m.get()
    password_man = password_m.get()
    cursor.execute ('SELECT Password FROM MANAGER WHERE Username = ?', (username_man,))
    pwdm = cursor.fetchone()
    if(pwdm[0]==password_man):
        manager_window()
    else:
        messagebox.showwarning("Invalid Identity","The Manager Password is wrong")  

def login_c():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("2300x1200")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_c
    global password_c
    username_c = StringVar()
    password_c = StringVar()

    global username_entry
    global password_entry

    Label(login_screen, text="Username * ").pack()
    username_entry = Entry(login_screen, textvariable=username_c)
    username_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_entry = Entry(login_screen, textvariable=password_c, show='*')
    password_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=same_c).pack()
    Button(login_screen, text="Back", width=10, height=1, command=login_screen.destroy).pack()   
def logout_c():
    customer_screen.destroy()
def same_c():
    global username_cus
    global password_cus
    username_cus = username_c.get()
    password_cus = password_c.get()
    cursor.execute ('SELECT Password FROM REGISTRATION WHERE Username = ?', (username_cus,))
    pwdc = cursor.fetchone()
 
    if(pwdc[0]==password_cus):
        customer_window()
    else:
        messagebox.showwarning("Invalid Identity","The Custmor Password is wrong")

def login_d():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("2300x1200")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_d
    global password_d
    username_d = StringVar()
    password_d = StringVar()

    global username_entry
    global password_entry

    Label(login_screen, text="Username * ").pack()
    username_entry = Entry(login_screen, textvariable=username_d)
    username_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_entry = Entry(login_screen, textvariable=password_d, show='*')
    password_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=same_d).pack()
    Button(login_screen, text="Back", width=10, height=1, command=login_screen.destroy).pack()
def logout_d():
    delivery_screen.destroy()
def same_d():
    global username_da
    global password_da
    username_da = username_d.get()
    password_da = password_d.get()
    cursor.execute ('SELECT Password FROM DELIVERYAGENT WHERE Username = ?', (username_da,))
    pwdd = cursor.fetchone()

    if(pwdd[0]==password_da):
        delivery_window()
    else:
        messagebox.showwarning("Invalid Identity","The Delivery Agent Password is wrong")

def customer_window():

    global customer_screen
    customer_screen = Toplevel(root)
    customer_screen.title("Customer Login")
    customer_screen.geometry("2300x1200")
    Label(customer_screen).pack()

    button_payment = Button(customer_screen, text="Payment", command=payment, width=20)
    button_payment.pack()
    button_select_publication = Button(customer_screen, text="Select Publications", command=select_publication, width=20)
    button_select_publication.pack()
    button_logout= Button(customer_screen, text="Logout", command=logout_c, width=20)
    button_logout.pack()

def manager_window():

    global manager_screen
    manager_screen = Toplevel(root)
    manager_screen.title("Manager Login")
    manager_screen.geometry("2300x1200")
    Label(manager_screen).pack()

    button_Display_Publication = Button(manager_screen, text="Display Publication", command=display_subscribers_list,width=20)
    button_Display_Publication.pack()

    button_Display_duer = Button(manager_screen, text="Duers", command=display_duers_list, width=20)
    button_Display_duer.pack()

    button_change_month = Button(manager_screen, text="Month change", command=change_month, width=20)
    button_change_month.pack()
    button_logout= Button(manager_screen, text="Logout", command=logout_m, width=20)
    button_logout.pack()
    mainloop()

def delivery_window():

    global delivery_screen
    delivery_screen = Toplevel(root)
    delivery_screen.title("Delivery Login")
    delivery_screen.geometry("2300x1200")
    Label(delivery_screen).pack()

    button_My_Deliveries = Button(delivery_screen, text="My deliveries", command=da_deliveries, width=20)
    button_My_Deliveries.pack()

    button_Salary = Button(delivery_screen, text="Salary", command=da_salary,width=20)
    button_Salary.pack()

    button_logout= Button(delivery_screen, text="Logout", command=logout_d, width=20)
    button_logout.pack()

def da_deliveries():
    global delivery_del
    delivery_del = Toplevel(delivery_screen)
    delivery_del.geometry("2300x1200")
    delivery_del.title("My Deliveries")
    top_ttitle = Label(delivery_del, text="Customer Name ")
    top_ttitle.grid(row=0, column=0, padx=50, pady=20)
    top_ttitle = Label(delivery_del, text="Customer Door no.")
    top_ttitle.grid(row=0, column=1, padx=50, pady=20)
    top_ttitle = Label(delivery_del, text="Customer Colony")
    top_ttitle.grid(row=0, column=2, padx=50, pady=20)
    top_ttitle = Label(delivery_del, text="Distance")
    top_ttitle.grid(row=0, column=3, padx=50, pady=20)
    top_ttitle = Label(delivery_del, text="Global Magazine")
    top_ttitle.grid(row=0, column=4, padx=50, pady=20)
    top_ttitle = Label(delivery_del, text="Global Newspaper")
    top_ttitle.grid(row=0, column=5, padx=50, pady=20)
    top_ttitle = Label(delivery_del, text="National Magazine")
    top_ttitle.grid(row=0, column=6, padx=50, pady=20)
    global var
    index1 = IntVar()
    index1=1
    index2= IntVar()
    index2=0
    var=StringVar()
    u=username_d.get()
    cursor.execute('''SELECT Colony_service FROM DELIVERYAGENT WHERE Username = ?''',(u,))
    v=cursor.fetchone()

    cursor.execute('''SELECT Name,Doornumber,Colony,Distance,Global_Magazine,Global_Newspaper,National_Magazine FROM JOIN1 WHERE Colony = ? ORDER BY Distance ASC;''',(v[0],))
    w=cursor.fetchall()

    for i in w:
        for j in i:
            var = j
            top_ttitle1 = Label(delivery_del, text=var)
            top_ttitle1.grid(row=index1, column=index2, padx=50, pady=20)
            index2+=1
        index2=0
        index1+=1 

def da_salary():
    global delivery_sal
    delivery_sal = Toplevel(delivery_screen)
    delivery_sal.geometry("2300x1200")
    delivery_sal.title("Delivery Agent Salary")
    
    top_ttitle = Label(delivery_sal, text="Delivery Agent Name")
    top_ttitle.grid(row=0, column=0, padx=50, pady=20)
    top_ttitle = Label(delivery_sal, text="Delivery Agent Monthly Salary ")
    top_ttitle.grid(row=0, column=1, padx=50, pady=20)
    global sal
    sal=0
    u=username_d.get()
    cursor.execute('''SELECT Name FROM DELIVERYAGENT WHERE Username = ?''',(u,))
    v=cursor.fetchone()
    cursor.execute('''SELECT Colony_service FROM DELIVERYAGENT WHERE Username = ?''',(u,))
    w=cursor.fetchone()
    cursor.execute('''SELECT Bill FROM JOIN1 WHERE Colony= ?''',(w[0],))
    s=cursor.fetchone()
    for i in s:
        sal+=i   
    top_ttitle = Label(delivery_sal, text=v[0])
    top_ttitle.grid(row=1, column=0, padx=50, pady=20)
    top_ttitle = Label(delivery_sal, text=0.025*sal)
    top_ttitle.grid(row=1, column=1, padx=50, pady=20)


def Bill():

    bill=150*pub1.get()+400*pub2.get()+250*pub3.get()
    c1=username_c.get()
    c2=pub1.get()
    c3=pub2.get()
    c4=pub3.get()
    l=[(c1,c2,c3,c4,bill)]
    cursor.executemany('''INSERT INTO SUBCRIPTION VALUES(?,?,?,?,?);''',l)
    create.commit()
    cursor.execute('''CREATE TABLE IF NOT EXISTS DUE(
        Username str(15),
        Due int 
    );''')
    paid1=[(username_c.get(),bill)]
    cursor.executemany('''INSERT INTO DUE (Username,Due) 
                    VALUES(?,?);''',paid1)
    cursor.execute("DELETE FROM JOIN1;")

    cursor.execute("SELECT *FROM REGISTRATION NATURAL JOIN SUBCRIPTION;")
    join1=cursor.fetchall()
    cursor.executemany('''INSERT INTO JOIN1
                    VALUES(?,?,?,?,?,?,?,?,?,?,?);''',join1)
    create.commit()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS JOIN2(
        Name str(15),
        Phonenumber str(15),
        Doornumber str(15),
        Colony str(15),
        Distance int,
        Username str(15),
        Password str(15),
        Global_Magazine int,
        Global_Newspaper int,
        National_Magazine int,
        Bill int,
        Due int 
    );''')
    cursor.execute("DELETE FROM JOIN2;")
    cursor.execute("SELECT *FROM JOIN1 NATURAL JOIN DUE;")
    join2=cursor.fetchall()
    cursor.executemany('''INSERT INTO JOIN2 
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?);''',join2 )
    create.commit()

def select_publication():
    global pub_screen
    pub_screen=Toplevel(customer_screen)
    pub_screen.title("Subscribe to the Publications")
    pub_screen.geometry("360x320")

    global pub1
    global pub2
    global pub3

    pub1 = IntVar()
    pub2 = IntVar()
    pub3 = IntVar()

    Checkbutton(pub_screen,text="Global Magazine - 150/- per month ",variable=pub1).pack()
    Checkbutton(pub_screen, text="Global Newspaper - 400/- per month ",variable=pub2).pack()
    Checkbutton(pub_screen,text="National Magazine - 250/- per month",variable=pub3).pack()

    Button(pub_screen, text="subscribe", width=10, height=1, command=Bill).pack()

    Label(pub_screen, text="").pack()
    Label(pub_screen, text="devlopers contact").pack()
    Label(pub_screen, text="note: please select choices wisely ,software will not able to revise once selected").pack()

def display_subscribers_list():
    global display_list
    display_list = Toplevel(root)
    display_list.geometry("2048x1080")
    display_list.title("List of subscribers")
    top_ttitle = Label(display_list, text="Display of the subscriber list")
    top_ttitle.grid(row=0, column=0,padx=50, pady=20)

    top_ttitle = Label(display_list, text="Name")
    top_ttitle.grid(row=1, column=0, padx=50)
    top_ttitle = Label(display_list, text="Phonenumber")
    top_ttitle.grid(row=1, column=1, padx=50)
    top_ttitle = Label(display_list, text="Doornumber")
    top_ttitle.grid(row=1, column=2, padx=50)
    top_ttitle = Label(display_list, text="Colony")
    top_ttitle.grid(row=1, column=3, padx=50)
    top_ttitle = Label(display_list, text="Global Magazine Subcription")
    top_ttitle.grid(row=1, column=4, padx=50)
    top_ttitle = Label(display_list, text="Global Newspaper Subcription")
    top_ttitle.grid(row=1, column=5, padx=50)
    top_ttitle = Label(display_list, text="National Magazine Subcription")
    top_ttitle.grid(row=1, column=6, padx=50)


    cursor.execute("SELECT Name,Phonenumber,Doornumber,Colony,Global_Magazine,Global_Newspaper,National_Magazine FROM JOIN1 ")
    pu=cursor.fetchall()

    
    index=2
    for i in pu:
            var = i
            top_ttitle1 = Label(display_list, text=var[0])
            top_ttitle1.grid(row=index, column=0, padx=50, pady=20)
            top_ttitle1 = Label(display_list, text=var[1])
            top_ttitle1.grid(row=index, column=1, padx=50, pady=20)
            top_ttitle1 = Label(display_list, text=var[2])
            top_ttitle1.grid(row=index, column=2, padx=50, pady=20)
            top_ttitle1 = Label(display_list, text=var[3])
            top_ttitle1.grid(row=index, column=3, padx=50, pady=20)
            top_ttitle1 = Label(display_list, text=var[4])
            top_ttitle1.grid(row=index, column=4, padx=50, pady=20)
            top_ttitle1 = Label(display_list, text=var[5])
            top_ttitle1.grid(row=index, column=5, padx=50, pady=20)  
            top_ttitle1 = Label(display_list, text=var[6])
            top_ttitle1.grid(row=index, column=6, padx=50, pady=20)          
            index+=1

def display_duers_list():
    global duer_list
    duer_list=Toplevel(root)
    duer_list.geometry("1500x1080")
    duer_list.title("Duer's List")
    top_ttitle = Label(duer_list, text="List of subscribers having dues")
    top_ttitle.grid(row=0, column=0,padx=50, pady=20)

    top_ttitle = Label(duer_list, text="Name")
    top_ttitle.grid(row=1, column=0,padx=50)
    top_ttitle = Label(duer_list, text="Phone number")
    top_ttitle.grid(row=1, column=1, padx=50)
    top_ttitle = Label(duer_list, text="Doornumber")
    top_ttitle.grid(row=1, column=2, padx=50)
    top_ttitle = Label(duer_list, text="Colony")
    top_ttitle.grid(row=1, column=3, padx=50)
    top_ttitle = Label(duer_list, text="Total Bill")
    top_ttitle.grid(row=1, column=4, padx=50)
    top_ttitle = Label(duer_list, text="Total Paid")
    top_ttitle.grid(row=1, column=5, padx=50)
    top_ttitle = Label(duer_list, text="Total Dues")
    top_ttitle.grid(row=1, column=6, padx=50)
    cursor.execute("SELECT Name,Phonenumber,Doornumber,Colony,Bill,Due FROM JOIN2 ")
    due=cursor.fetchall()

    
    index=2
    for i in due:
            var = i
            top_ttitle1 = Label(duer_list, text=var[0])
            top_ttitle1.grid(row=index, column=0, padx=50, pady=20)
            top_ttitle1 = Label(duer_list, text=var[1])
            top_ttitle1.grid(row=index, column=1, padx=50, pady=20)
            top_ttitle1 = Label(duer_list, text=var[2])
            top_ttitle1.grid(row=index, column=2, padx=50, pady=20)
            top_ttitle1 = Label(duer_list, text=var[3])
            top_ttitle1.grid(row=index, column=3, padx=50, pady=20)
            top_ttitle1 = Label(duer_list, text=var[4])
            top_ttitle1.grid(row=index, column=4, padx=50, pady=20)
            top_ttitle1 = Label(duer_list, text=var[5])
            top_ttitle1.grid(row=index, column=5, padx=50, pady=20)  
            top_ttitle1 = Label(duer_list, text=var[4]-var[5])
            top_ttitle1.grid(row=index, column=6, padx=50, pady=20)          
            index+=1

def due_after_payment():

    Label(pay_screen, text="Payment successful", fg="green", font=("calibri", 11)).pack()
    global p_balance
    p_balance=IntVar()
    global p_get
    cursor.execute("SELECT DUE FROM JOIN2 WHERE Username= ? ",(username_c.get(),))
    p_get=cursor.fetchone()
    p_balance=p_get[0]-p_amount.get()
    up1=[(p_balance,username_c.get())]
    cursor.executemany("UPDATE DUE SET Due = ? WHERE Username = ?;",up1)
    cursor.executemany("UPDATE JOIN2 SET Due = ? WHERE Username = ?;",up1)
    create.commit()

    global recipt_screen
    recipt_screen = Toplevel(customer_screen)
    recipt_screen.title("Recipt")
    recipt_screen.geometry("720x540")
    rec_ttitle = Label(recipt_screen, text="Payment Recipt")
    rec_ttitle.grid(row=0, column=0,padx=50, pady=20)
    
    cursor.execute("SELECT Name,Phonenumber,Due FROM JOIN2 WHERE Username=?",(username_c.get(),))
    rec=cursor.fetchone()
    rec_ttitle = Label(recipt_screen, text=rec[0])
    rec_ttitle.grid(row=3, column=0,padx=50, pady=20)
    rec_ttitle = Label(recipt_screen, text=rec[1])
    rec_ttitle.grid(row=3, column=1,padx=50, pady=20)

    rec_ttitle = Label(recipt_screen, text="Total Bill To be paid")
    rec_ttitle.grid(row=5, column=1,padx=50, pady=20)
    rec_ttitle = Label(recipt_screen, text="Amount Paid")
    rec_ttitle.grid(row=6, column=1,padx=50, pady=20)
    rec_ttitle = Label(recipt_screen, text="---------------------------")
    rec_ttitle.grid(row=7, column=1,padx=50, pady=20)
    rec_ttitle = Label(recipt_screen, text="Balance remaining")
    rec_ttitle.grid(row=8, column=1,padx=50, pady=20)
    rec_ttitle = Label(recipt_screen, text="---------------------------")
    rec_ttitle.grid(row=9, column=1,padx=50, pady=20)

    rec_ttitle = Label(recipt_screen, text=rec[2]+p_amount.get())
    rec_ttitle.grid(row=5, column=5,padx=50, pady=20)
    rec_ttitle = Label(recipt_screen, text=p_amount.get())
    rec_ttitle.grid(row=6, column=5,padx=50, pady=20)
    rec_ttitle = Label(recipt_screen, text="-------------")
    rec_ttitle.grid(row=7, column=5,padx=50, pady=20)
    rec_ttitle = Label(recipt_screen, text=p_balance)
    rec_ttitle.grid(row=8, column=5,padx=50, pady=20)
    rec_ttitle = Label(recipt_screen, text="-------------")
    rec_ttitle.grid(row=9, column=5,padx=50, pady=20)

def payment():
    global pay_screen
    pay_screen = Toplevel(customer_screen)
    pay_screen.title("Payment")
    pay_screen.geometry("720x540")
    Label(pay_screen, text="Amount still remaining to pay").pack()
    cursor.execute("SELECT DUE FROM JOIN2 WHERE Username= ? ",(username_c.get(),))
    paybill=cursor.fetchall()
    Label(pay_screen, text= paybill[0]).pack()

    Label(pay_screen, text="Enter amount to pay via cash or card ").pack()
    global p_amount
    p_amount=IntVar()
   
    global p_entry
    p_entry = Entry(pay_screen, textvariable=p_amount)
    p_entry.pack()
    Label(pay_screen, text="").pack()
    Button(pay_screen, text="Pay", width=10, height=1, command=due_after_payment).pack()
    
def change_month():
    print("changing month")
    change_mon = Tk()
    change_mon.geometry("240x40")
    change_mon.title("change month ")
    top_ttitle = Label(change_mon, text="month has been changed sucessfully ")
    top_ttitle.grid(row=0, column=0, padx=20, pady=20)
    
    cursor.execute("DELETE FROM JOIN1;")
    cursor.execute("DELETE FROM JOIN2;")
    cursor.execute("DELETE FROM DUE;")
    cursor.execute("DELETE FROM SUBCRIPTION;")
    create.commit()

def Customer():
    global cus 
    cus= Toplevel(root)
    cus.geometry("2300x1200")
    cus.title("CUSTOMER")
    button_c_login = Button(cus, text="Login", command=login_c, width=40)
    button_c_login.grid(row=3, column=1)

    button_c_register = Button(cus, text="Register", command=register, width=40)
    button_c_register.grid(row=3, column=2)

    button_c_exit= Button(cus, text="Back", width=12, height=1,command=cus.destroy)
    button_c_exit.grid(row=3, column=3)

def Manager():
    global man
    man= Toplevel(root)
    man.geometry("2300x1200")
    man.title("MANAGER")
    button_m_login = Button(man, text="Login", command=login_m, width=40)
    button_m_login.grid(row=3, column=1)
    button_m_exit= Button(man, text="Back", width=12, height=1,command=man.destroy)
    button_m_exit.grid(row=3, column=3)

def Deliveryagent():
    global da
    da =Toplevel(root)
    da.geometry("2300x1200")
    da.title("DELIVERY AGENT")
    button_da_login = Button(da, text="Login", command=login_d, width=40)
    button_da_login.grid(row=3, column=1)
    button_da_exit= Button(da, text="Back", width=12, height=1,command=da.destroy)
    button_da_exit.grid(row=3, column=3)

button_customer=Button(root, text="CUSTOMER", command=Customer, width=40)
button_customer.grid(row=6, column=2)
button_manager=Button(root, text="MANAGER", command=Manager, width=40)
button_manager.grid(row=6, column=1)
button_deliveryagent=Button(root, text="DELIVERY AGENT", command=Deliveryagent, width=40)
button_deliveryagent.grid(row=6, column=0)
button_select_nm = Button(root,text="EXIT",command=root.quit,width=40)
button_select_nm.grid(row=6,column=3)


root.mainloop()

