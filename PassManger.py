from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
from cryptography.fernet import Fernet


objects = []
window = Tk()
window.withdraw()
window.title('Email Keeper')
key = "yrkveq6loG_Zv4XkyRbeJKvJrgE5yBFmU5D9_6uP_KY="
fornet = Fernet(key)

class popupWindow(object):
    loop = FALSE
    attempts = 0

    def __init__(self,master):
        front = self.front = Toplevel(master)
        front.title('Input Password')
        front.geometry('{}x{}'.format(250,100))
        front.resizable(width=FALSE,height=FALSE)
        self.lbl = Label(front,text="Password:",font=('Courier',14),justify=CENTER)
        self.lbl.pack()
        self.ent = Entry(front,show='*',width=30)
        self.ent.pack(pady=7)
        self.btn = Button(front,text='Submit',command=self.cleanup,font=('Courier',14))
        self.btn.pack()

    def cleanup(self):
        self.value = self.ent.get()
        access = 'Sunil@9899'

        if self.value == access:
            self.loop = TRUE
            self.front.destroy()
            window.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.ent.delete(0,'end')
            messagebox.showerror('Incorrect Password', 'Incorrect Password,Attempts remaining: '+ str(5-self.attempts))

class entity_add:
    def __init__(self,master,n,p,e):
        self.password = p
        self.name = n 
        self.email = e
        self.window = master
    def write(self):
        r = open('emails.txt',"ab")
        n = self.name
        e = self.email
        p = self.password
        
        
        encryptedN = fornet.encrypt(bytes(n,encoding='ascii'))
        encryptedE = fornet.encrypt(bytes(e,encoding='ascii'))
        encryptedP = fornet.encrypt(bytes(p,encoding='ascii'))
        
        # print(encryptedN + b'')
        # print(encryptedE + b'')
        # print(encryptedP + b'')
        



#ABHHHHHHHHINAVVVVVV RAWAT 

        r.write(encryptedN + b',' + encryptedE + b',' + encryptedP + b', \n')
        # r.write(encryptedN + ',' + encryptedE + ',' + encryptedP +'\n')
        # print(encryptedN + b',' + encryptedE + b',' + encryptedP + b', \n')

        r.close()
        

class entity_display:
    def __init__(self,master,n,e,p,i):
        self.password = p
        self.name = n
        self.email = e
        self.window = master
        self.i = i

        dencryptedN = fornet.decrypt(bytes(n,encoding='ascii'))
        dencryptedE = fornet.decrypt(bytes(e,encoding='ascii'))
        dencryptedP = fornet.decrypt(bytes(p,encoding='ascii'))

        self.label_name = Label(self.window,text=dencryptedN,font=('Courier',14))
        self.label_email = Label(self.window,text=dencryptedE,font=('Courier',14))
        self.label_password = Label(self.window,text=dencryptedP,font=('Courier',14))
        self.deleteButton = Button(self.window,text='X',fg='red',command=self.delete)

    def display(self):
        self.label_name.grid(row=6 + self.i, sticky=W) 
        self.label_email.grid(row=6 + self.i,column=1)
        self.label_password.grid(row=6 + self.i, column=2, sticky =E)
        self.deleteButton.grid(row=6+self.i,column=3,sticky=E)

    def delete(self):
        answer = tkinter.messagebox.askquestion('Delete','Are you sure you want to delete this entry? ')

        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open('emails.txt','r')
            lines = f.readlines()
            f.close()

            f = open('emails.txt',"w")
            count = 0

            for line  in lines:
                if count != self.i:
                    f.write(line)
                    count +=1         

            f.close()
            readfile()


    def destroy(self):
        self.label_name.destroy()
        self.label_email.destroy()
        self.label_password.destroy()
        self.deleteButton.destroy()

#Methods

def onsubmit():
    mail = email.get()
    password = pas.get()
    naam = name.get()
    e = entity_add(window,naam,password,mail)
    e.write()
    name.delete(0,'end')
    email.delete(0,'end')
    pas.delete(0,'end')
    messagebox.showinfo('Added Entity', 'Successfully Added, \n' + 'Name: '+ naam + '\nEmail: '+ mail + '\nPassword: '+ password)
    readfile()

def clearfile():
    f = open('emails.txt',"w")
    f.close()    
def readfile():
    f = open('emails.txt','r')
    count = 0

    for line in f:
        entity_list = line.split(',')
        e = entity_display(window,entity_list[0],entity_list[1],entity_list[2],count)
        objects.append(e)
        e.display()
        count += 1
    f.close()    





# /////GUL WORK ??????
m = popupWindow(window)
entity_label = Label(window,text='Add Entity',font =('Courier',18))
# entity_label.pack()
name_label = Label(window,text='Name:',font=('Courier',14))
# name_label.pack()
email_label =Label(window,text='Email:',font=('Courier',14))
# email_label.pack()
pass_label = Label(window,text='Password:',font=('Courier',14))
# pass_label.pack()
name = Entry(window,font=('Courier',14))
# name.pack()
email = Entry(window,font=('Courier',14))
# email.pack()
pas = Entry(window,show='*',font=('Courier',14))
# pas.pack()
subBtn = Button(window,text='Add Email',command=onsubmit, font=('Courier',14))
# subBtn.pack()

entity_label.grid(columnspan=3,row=0)
name_label.grid(row=1,sticky=E,padx=3)
email_label.grid(row=2,sticky=E,padx=3)
pass_label.grid(row=3,sticky=E,padx=3)

name.grid(columnspan=3,row=1,column=1,padx=2,pady=2,sticky=W)
email.grid(columnspan=3,row=2,column=1,padx=2,pady=2,sticky=W)
pas.grid(columnspan=3,row=3,column=1,padx=2,pady=2,sticky=W)

subBtn.grid(columnspan=3,pady=4)

name_label12 = Label(window,text='Name:',font=('Courier',14))
email_label12 = Label(window,text='Email:',font=('Courier',14))
pass_label12 = Label(window,text='Password:',font=('Courier',14))

name_label12.grid(row=5)
email_label12.grid(row=5,column=1)
pass_label12.grid(row=5,column=2)

readfile()

window.mainloop()


