import tkinter
from tkinter import *

top=tkinter.Tk()
top.title("Note Taking App")
top.size()
top.geometry("400x400")
btn=tkinter.Button(top,text="Add New Note >>",bg='red',fg='white',command="add.py")
bt=tkinter.Button(top,text="List all Notes",bg='red',fg='white',command="Write")
#btn.pack()
btn.grid(row=1,column=0,pady=10)
bt.grid(row=1,column=1,pady=10)
Label(top,text='Search Notes',font='Bold').grid(row=2,column=0)
#top.geometry("100x100")
#Label(top,text='input').grid(row=0)
e1=Entry(top,width=40)
a=e1.grid(row=3,column=0)

bta=tkinter.Button(top,text="Search",bg='red',fg='white',command=" ")
bta.grid(row=3,column=2)
Label(top,text='--Notes--',font='Bold').grid(row=4,column=2)



top.mainloop()