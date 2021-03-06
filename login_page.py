from cProfile import label
from tkinter import *
root = Tk()
root.geometry("1400x1400")
root.title("Virtual Health Assistant")
root.configure(bg="#8EAAF3")
mylabel=Label(root,text="Login Page",font=("Gabriola",28,"bold"),fg="black",bg="#8EAAF3")
mylabel.pack()

def clear_text():
    e1.delete(0,END)
    e2.delete(0,END)

def display():
    s1=e1.get()
    s2=e2.get()
def patient_reg_page():
    root.destroy()
    import patient_reg_page 
    

l1=Label(root,text="Enter UserName : ",bg="#8EAAF3",anchor=CENTER,font=("Gabriola",24,"bold"))
l1.place(x=450,y=100)
e1=Entry(root,font=("Gabriola",12),width=40,borderwidth=2)
e1.place(x=660,y=116)

l2=Label(root,text="Enter PassWord : ",bg="#8EAAF3",anchor=CENTER,font=("Gabriola",24,"bold"))
l2.place(x=450,y=180)
e2=Entry(root,show="$",font=("Gabriola",12),borderwidth=3,width=40)
e2.place(x=660,y=194)

b1=Button(root,text="Submit",padx=10,font=("time",14,"bold"),command=display,bg="#8EAAF3")
b1.place(x=580,y=300)
b2=Button(root,text="Clear",padx=10,font=("time",14,"bold"),command=clear_text,bg="#8EAAF3")
b2.place(x=740,y=300)

l6 = Button(root,text='Not Registered? Register Here',font=('',12,'bold'),bg='#8EAAF3',command = patient_reg_page, width = 29)
l6.place(x=550, y = 380)
root.mainloop()