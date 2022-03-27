from tkinter import *
root = Tk()
root.resizable(0,0)
root.configure(bg='#8EAAF3')
root.title('Virtual Health Assistant')
root.geometry('1500x1400')

def display():
    return 0
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
def doctor_reg_page():
    root.destroy()
    import doctor_reg_page
# Widgets
l5 = Label(root,text='Join Virtual Health Assistant',font=('Gabriola',28,'bold'),bg='#8EAAF3')
l1 = Label(root,text='Full Name',font=('Gabriola',26,'bold'),bg='#8EAAF3')
l6 = Button(root,text='Are you a Doctor? Register Here',font=('',12,'bold'),bg='#8EAAF3',command = doctor_reg_page, width = 29)
l2 = Label(root,text='E-Mail',font=('Gabriola',26,'bold'),bg='#8EAAF3')
l3 = Label(root,text='Gender',font=('Gabriola',26,'bold'),bg='#8EAAF3')
l4 = Label(root,text='Password',font=('Gabriola',26,'bold'),bg='#8EAAF3')
e1 = Entry(root,font=('Gabriola',12,'bold'),width=40,borderwidth=2)
e2 = Entry(root,font=('Gabriola',12,'bold'),width=40,borderwidth=2)
e3 = Entry(root,font=('Gabriola',12,'bold'),width=40,borderwidth=2)
e4 = Entry(root,font=('Gabriola',12,'bold'),width=40,borderwidth=2)
b1 = Button(root,text='Submit',font=('time',14),bg='#8EAAF3',command=display,width=8)
b2 = Button(root,text='Clear',font=('time',14),bg='#8EAAF3',command=clear,width=8)

# Location
l1.place(x=550,y=100)
e1.place(x=700,y=120)
l2.place(x=550,y=185)
e2.place(x=700,y=205)
e3.place(x=700,y=283)
l4.place(x=550,y=265)
l5.place(x=650,y=0)
b1.place(x=680,y=365)
b2.place(x=820,y=365)
l6.place(x=660,y=455)

root.mainloop()