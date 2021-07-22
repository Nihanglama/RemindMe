import datetime
import tkinter as tk
from time import strftime
from tkinter import Entry, Toplevel, font, mainloop
from tkinter.constants import END, LEFT,RIGHT, TOP
from typing import Text

def main():
    window= tk.Tk()
    window.title("Notifier")
    window.geometry("800x800")
    window.configure(bg="black")

    label1=tk.Label(fg='white',font=("itallic",20),bg="black")
    label1.pack(anchor="n")
    label=tk.Label(text="REMAIN UPTO DATE",foreground="white",bg="green",font=("Itallic",20),height=5,width=100)
    label.pack(anchor='center')

    text_area=tk.Label(text="Recent events to show",fg="black",bg="white",width=500,height=10,pady=5,padx=5)
    text_area.pack()

    view_btn=tk.Button(command=lambda:view_Events(),font="itallic",bg="black",fg="blue",text="View_allEvents",padx=30,pady=10)
    view_btn.pack(anchor='n')



    add_btn=tk.Button(command=lambda:add_event(),font="itallic",bg="black",fg="blue",text="Add_Events",padx=30,pady=10)
    add_btn.pack(anchor='n')


    def time():
        string = strftime('%H:%M:%S:%p')
        label1.config(text=string)
        label1.after(1000,time)


    time()

    tk.mainloop()

def add_event():
    window1=tk.Tk()
    window1.title("ADD_EVENTS")
    window1.geometry("500x500")
    window1.configure(bg="pink")
    show=tk.Label(window1,text="Type :")
    show.pack(side=TOP)
    inp=tk.Entry(window1,bd=5)
    inp.pack(side=TOP)

    show3=tk.Label(window1,text="Name :")
    show3.pack(side=TOP)
    inp3=tk.Entry(window1,bd=5)
    inp3.pack(side=TOP)

    show1=tk.Label(window1,text="Date :")
    show1.pack(side=TOP)
    inp1=tk.Entry(window1,bd=5)
    inp1.pack(side=TOP)

    show2=tk.Label(window1,text="Details :")
    show2.pack(side=TOP)
    inp2=tk.Entry(window1,bd=5)
    inp2.pack(side=TOP)
    def clear():
        inp.delete(0,END)
        inp1.delete(0,END)
        inp2.delete(0,END)
        inp3.delete(0,END)
        enter_btn.configure(text="Added Info")
    
    enter_btn=tk.Button(window1,font="itallic",bg="black",fg="blue",text="ADD",padx=30,pady=10,command=lambda:clear())
    enter_btn.configure(activebackground='pink',cursor='dot')
    enter_btn.pack(side=TOP)
    mainloop()




def view_Events():
    window2=tk.Tk()
    # window2.geometry("800*800")
    window2.configure(bg="Black")
    lis=[["SN","TYPE","NAME","DATE","DETAILS"],[1,"hello","loves",20,"ABCD"],
    [2,'Aaryan','Pune',18,"ABCD"],
    [3,'Rachna','Mumbai',21,"ABCD"],
    [4,'Shubham','Delhi',21,"ABCD"]]
    for i in range(5):
        for j in range(5):
            show=tk.Entry(window2, width=20, fg='blue',font=('Arial',16,'bold'))
            show.grid(row=i,column=j)
            show.insert(END,lis[i][j])




#     pass

if __name__ == "__main__":
    main()