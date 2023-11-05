import tkinter
from tkinter import*
from tkinter import messagebox
root=tkinter.Tk()
root.title("LOGIN PAGE")
root.configure(bg="white")
#root.iconbitmap(r'login.ico')
root.geometry('1366x768')


def insert():
    user=username.get()
    passw=password.get()
    messagebox.showinfo("LOGIN SUCCESFULLY","Welcome to your account")


def signin(): 
    username=username.get()
    password=password.get()


bg =PhotoImage(file="login.png")
img=Label(root,image=bg)
img.place(x=200,y=200)

frame=Frame(root,width=400,height=400,bg="white")
frame.place(x=700,y=200)

sign_in=Label(frame,text="Welcome to Skype",fg="#0000FF",bg="white",font=("Microsoft YaHei UI",23,"bold"))
sign_in.place(x=30,y=20)

def on_entry(e):
    username.delete(0,'end')

def on_leave(e):
    name=username.get()
    if name=='':
        username.insert(0,'Username')

username= Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI",11))
username.place(x=30,y=90)
username.insert(0,"Username")
username.bind("<FocusIn>",on_entry)
username.bind("<FocusOut>",on_leave)
username.get()

Frame(frame,width=295,height=2,bg="black").place(x=25,y=114)


def on_entry(e):
    password.delete(0,'end')

def on_leave(e):
    name=password.get()
    if name=='':
        password.insert(0,'password')


password= Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI",11))
password.place(x=30,y=150)
password.insert(0,"Password")
password.bind("<FocusIn>",on_entry)
password.bind("<FocusOut>",on_leave)
password.get()



Frame(frame,width=295,height=2,bg="black").place(x=25,y=175)


Button (frame,width=40,pady=9,text="Login",bg="blue",fg="white",border=0,command=insert).place(x=35,y=205)
label=Label(frame,text="Don't have an account?",fg="black",bg="white",font=("Microsoft YaHei UI",9))
label.place(x=75,y=270)

sign_in=Button(frame,width=6,text="Sigin",border=0,bg="white",cursor='hand2',fg="blue")
sign_in.place(x=215,y=270)




root.mainloop()
