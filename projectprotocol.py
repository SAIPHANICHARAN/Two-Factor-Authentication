from tkinter import *
import pandas as pd
import os

dataset = pd.read_csv('Book1.csv')
def show_entry_fields():
    #master.destroy()
    os.system("sudo ssh -i newcloud.pem ubuntu@18.222.11.52 'cd /home/ubuntu/ && python send_sms.py'")
    x= dataset.iloc[0:1,0:1].values
    y = dataset.iloc[:1,1:2].values
    z= dataset.iloc[:1,2:3].values
    k=dataset.iloc[:1,3:4].values
    print("card number: %s" % (e1.get()))
    l=e1.get()
    root = Tk()
    frame = Frame(root)
    frame.pack(side="top")
    display = Label(frame, text='DETAILS', font=('arial', 20, 'bold'), bg="yellow", fg="black").grid(columnspan=4)
    name = Label(frame, text="NAME :", font=('arial', 20, 'bold'))
    name.grid(row=3, column=0)
    name = Label(frame, text=x[0][0], font=('arial', 20, 'bold'))
    name.grid(row=3, column=1)  
    regno = Label(frame, text="REG NO.:", font=('arial', 20, 'bold'))
    regno.grid(row=5, column=0)
    regno = Label(frame, text=str(y[0][0]), font=('arial', 20, 'bold'))
    regno.grid(row=5, column=1)
    branch = Label(frame, text="BRANCH:", font=('arial', 20, 'bold'))
    branch.grid(row=7, column=0)
    branch = Label(frame, text=z[0][0], font=('arial', 20, 'bold'))
    branch.grid(row=7, column=1)
    year = Label(frame, text="YEAR :", font=('arial', 20, 'bold'))
    year.grid(row=9, column=0)
    year = Label(frame, text=k[0][0], font=('arial', 20, 'bold'))
    year.grid(row=9, column=1)

    root.mainloop()

master = Tk()
Label(master, text="card number:").grid(row=0)


e1 = Entry(master)


e1.grid(row=0, column=1)


   
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Quit', command=master.destroy).grid(row=3, column=0, sticky=W, pady=4)

mainloop( )
