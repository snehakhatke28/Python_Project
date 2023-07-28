from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
​
​
req=Tk() #Creating instance Tk
req.title("Internship Registration")
''
req.geometry("600x600")
''
bg= ImageTk.PhotoImage(file="bg3.jpg")
#Not aalowed to expand the window
req.resizable(False, False)
''
​
def register():
    name=name_details.get()
    lastname=lastname_info.get()
    mail_id=mail_info.get()
    mobileno=phonenumber_info.get()
    Branch=branch_info.get()
    Domain=domain_info.get()
    
    if name=="":
        messagebox.showerror("Error","Please enter your first name.")
    elif lastname=="":
        messagebox.showerror("Error occured","Please enter  your lastname .")
    elif mail_id=="":
        messagebox.showerror("Error occured","Please enter  your mail_id.")
    elif mobileno=="":
        messagebox.showerror("Error","Enter mobile number.")
    elif Branch=="":
        messagebox.showerror("Error","Enter your Branch.")
    elif Domain=="":
        messagebox.showerror("Error","Enter your Domain.")
    else:
        label = Label(req, text='Registration sucessfull',font=("ariel", 20),bg="green").place(x=290,y=510)
    with open(name+".txt","w")as f:
        f.write(name+"\n")
        f.write(lastname+"\n")
        f.write(mail_id+"\n")
        f.write(mobileno+"\n")
        f.write(Branch+"\n")
        f.write(Domain+"\n")
​
def clear():
    name_entry.delete(0,END)
    lastn_entry.delete(0,END)
    m_entry.delete(0,END)
    p_entry.delete(0,END)
    branch_entry.delete(0,END)
    domain_entry.delete(0,END)
​
​
label = Label(req, text='Welcome !!Kindly fill the details.',font=("ariel", 28),bg="orange")
label.pack(ipadx=20, ipady=20)
#label = Label(req, text='First name',font=("ariel", 14).pack(pady=20, side= 'Left', anchor="w"))
#label=label(req,text="Name",font="20").place(x=12,y=70)
​
Label(req, text= "First Name", font= ('Helvetica 15 underline'),
background="gray74").pack(pady=19, side= TOP, anchor="sw")
label.pack(ipadx=24, ipady=24)
Label(req, text= "Last Name", font= ('Helvetica 15 underline'),
background="gray74").pack(pady=19, side= TOP, anchor="sw")
Label(req, text= "mail id", font= ('Helvetica 15 underline'),
background="gray74").pack(pady=19, side= TOP, anchor="sw")
Label(req, text= "Mobile no", font= ('Helvetica 15 underline'),
background="gray74").pack(pady=19, side= TOP, anchor="sw")
Label(req, text= "Branch", font= ('Helvetica 15 underline'),
background="gray74").pack(pady=19, side= TOP, anchor="sw")
Label(req, text= "Domain", font= ('Helvetica 15 underline'),
background="gray74").pack(pady=19, side= TOP, anchor="sw")
​
name_details=StringVar()
lastname_info=StringVar()
mail_info=StringVar()
phonenumber_info=StringVar()
branch_info=StringVar()
domain_info=StringVar()
#Using entry visit
#name_entry = tk.Entry(req, textvariable="First Name").grid(row=1, column=2)
​
​
name_entry=Entry(req,font="10",bd=4,textvariable=name_details)
name_entry.place(x=120,y=120)
​
lastn_entry=Entry(req,font="10",bd=4,textvariable=lastname_info)
lastn_entry.place(x=120,y=185)
m_entry=Entry(req,font="10",bd=4,textvariable=mail_info)
m_entry.place(x=120,y=250)
p_entry=Entry(req,font="10",bd=4,textvariable=phonenumber_info)
p_entry.place(x=120,y=330)
branch_entry=Entry(req,font="10",bd=4,textvariable=branch_info)
branch_entry.place(x=120,y=400)
domain_entry=Entry(req,font="10",bd=4,textvariable=domain_info)
domain_entry.place(x=120,y=460)
#Button
​
Button(req,text="Apply!",font="20",command=register).place(x=80,y=510)
​
Button(req,text="Clear",font="20",command=clear).place(x=220,y=510)
mainloop()
