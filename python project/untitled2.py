from twilio.rest import Client
import random

from tkinter import *
import csv

def sms():
    i=(random.randint(1000,9999))
    account_sid = "AC27337efba74fc815e2d6f55e184a3ee5"
    auth_token  = "fce32b6eae24fd059ed94968d76235d2"
    client = Client(account_sid, auth_token)
    message = client.messages.create( to="+919629607721",from_="+12565675530",body=i)
    message2 = client.messages.create(to="+919490898515",from_="+12565675530",body=i)
    print(message.sid,"OTP Sent:",i);
    print(message2.sid,"OTP Sent:",i);

def show_entry_fields():
    sms()
    f=open("collecteddata.txt",'a')
    f.write(e1.get()+",")
    print("card number: %s" % (e1.get()))
    l=e1.get()
    k=[]
    with open('store.txt','r') as f:
        reader = list(csv.reader(f))
        print(reader)
        for row in reader:
            if(str(row[0]) == str(l)):
                k=list(row)
    print(k)
    f.close()
    root = Tk()
    
    frame = Frame(root)
    frame.pack(side="top")
    display = Label(frame, text='DETAILS', font=('arial', 30, 'bold'), bg="yellow", fg="black").grid(columnspan=4)
    name = Label(frame, text="NAME :", font=('arial', 30, 'bold'))
    name.grid(row=3, column=0)
    name = Label(frame, text=str(k[1]), font=('arial', 30, 'bold'))
    name.grid(row=3, column=1)   
    regno = Label(frame, text="REG NO.:", font=('arial', 30, 'bold'))
    regno.grid(row=5, column=0)
    regno = Label(frame, text=str(k[2]), font=('arial', 30, 'bold'))
    regno.grid(row=5, column=1)
    branch = Label(frame, text="BRANCH:", font=('arial', 30, 'bold'))
    branch.grid(row=7, column=0)
    branch = Label(frame, text=k[3], font=('arial', 30, 'bold'))
    branch.grid(row=7, column=1)
    year = Label(frame, text="YEAR :", font=('arial', 30, 'bold'))
    year.grid(row=9, column=0)
    year = Label(frame, text=k[4], font=('arial', 30, 'bold'))
    year.grid(row=9, column=1)
    Label(frame, text = "GO THE WEB PAGE",font=('arial', 30, 'bold'),bg="yellow").grid(row =10)
    Label(frame, text = "AND ENTER THE OTP",font=('arial', 30, 'bold'),bg="yellow").grid(row =11)
    Label(frame, text = "TO DOWNLOAD YOUR CONTENT!",font=('arial', 30, 'bold'),bg="yellow").grid(row =12)
    root.mainloop()

master = Tk()
Label(master,font=('arial', 20, 'bold'), text="card number:", bg = "orange").grid(row=0)


e1 = Entry(master)


e1.grid(row=0, column=1)

Label(master,font=('arial', 20, 'bold'),text="SWIPE THE CARD FOR AUTHENTICATION AND PRESS SHOW : ", bg = "yellow"  ).grid(row=4)
    
Button(master, text='Show',font=('arial', 20, 'bold'), command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Quit',font=('arial', 20, 'bold'), command=master.destroy).grid(row=3, column=0, sticky=W, pady=4)

mainloop( )


