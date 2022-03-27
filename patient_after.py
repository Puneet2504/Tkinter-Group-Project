from tkinter import *
from tkinter import ttk
root = Tk()
root.resizable(0,0)
root.configure(bg='#8EAAF3')
root.title('Virtual Health Assistant')
root.geometry('1500x1500')

# Widgets
l1 = Label(root,text='Welcome',font=('Gabriola',28,'bold'),bg='#8EAAF3')
l2 = Label(root,text='Consultancy Status',font=('Gabriola',28,'bold'),bg='#8EAAF3')
l3 = Label(root,text='Name: ',font=('Gabriola',20,'bold'),bg='#8EAAF3')
l4 = Label(root,text='E-Mail:',font=('Gabriola',20,'bold'),bg='#8EAAF3')
b1 = Button(root,text='Book Meeting',font=('Gabriola',20,'bold'),bg='#8EAAF3',width = 16)
b2 = Button(root,text='Receipt',font=('Gabriola',20,'bold'),bg='#8EAAF3',width = 16)
b3 = Button(root,text='Logout',font=('Gabriola',16,'bold'),bg='#8EAAF3',width = 15)
treev = ttk.Treeview(root,selectmode="browse")
 
# Calling pack method w.r.to treeview
treev.pack(side ='right')
# Constructing vertical scrollbar
# with treeview
treev["columns"] = ("1", "2", "3", "4", "5", "6")
treev['show'] = 'headings'
treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='se')
treev.column("3", width = 90, anchor ='se')
treev.heading("1", text ="Sr.No.")
treev.heading("2", text ="Doctor Name")
treev.heading("3", text ="Department")
treev.heading("4", text ="Status")
treev.heading("5", text ="Timing")
treev.heading("6", text ="Meeting Link")

# Location
l1.place(x=650,y=0)
l2.place(x=600,y=320)
l3.place(x=10,y=0)
l4.place(x=10,y=60)
b1.place(x=460,y=160)
b2.place(x=740,y=160)
b3.place(x=1350,y=0)
treev.place(x =300,y=400)
root.mainloop()