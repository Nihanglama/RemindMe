from functools import singledispatch
from tkinter import messagebox
import tkinter as tk
from time import strftime
from tkinter import *
from tkinter.ttk import *
def main():
    window= tk.Tk()
    window.title("REMIND_ME")
    window.geometry("800x800")
    window.configure(bg="black")
    window.resizable(False,False)
    logo=PhotoImage(file="notification.png")
    window.iconphoto(False,logo)

    label1=tk.Label(fg='white',font=("itallic",20),bg="black")
    label1.pack(anchor="n")
    label=tk.Label(text="REMAIN UPTO DATE",foreground="white",bg="green",font=("Itallic",20),height=5,width=100)
    label.pack(anchor='center')

    text_area=tk.Label(text="Recent events to show",fg="black",bg="white",width=500,height=10,pady=5,padx=5)
    text_area.pack()

    view_btn=tk.Button(command=lambda:view_Events(),font="itallic",bg="black",fg="blue",text="View_allEvents",padx=30,pady=10)
    view_btn.place(x=300,y=470)
    view_btn.configure(activebackground='navy',activeforeground='black')

    add_btn=tk.Button(command=lambda:add_event(),font="itallic",bg="black",fg="blue",text="Add_Events",padx=30,pady=10)
    add_btn.place(x=310,y=400)
    add_btn.configure(activebackground='navy',activeforeground='black')


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
    window1.resizable(False,False)

    show=tk.Label(window1,text="Type :")
    show.pack(side=TOP)
    # kind=StringVar()
    inp=tk.Entry(window1,bd=5)
    inp.pack(side=TOP)

    show1=tk.Label(window1,text="Date :")
    show1.pack(side=TOP)
    # Date=StringVar()
    inp1=tk.Entry(window1,bd=5)
    inp1.pack(side=TOP)

    show2=tk.Label(window1,text="Details :")
    show2.pack(side=TOP)
    # Details=StringVar()
    inp2=tk.Entry(window1,bd=5)
    inp2.pack(side=TOP)

    show3=tk.Label(window1,text="Name :")
    show3.pack(side=TOP)
    # Name=StringVar()
    inp3=tk.Entry(window1,bd=5)
    inp3.pack(side=TOP)

    def inputs():
       global types
       global names
       global Dates
       global Detail
       types=inp.get()
       names=inp3.get()
       Dates=inp1.get()
       Detail=inp2.get()
       print(types,names,Dates,Detail)

       if type=="" or names=="" or Dates=="" or Detail=="":
           messagebox.showwarning("Error 300","Please fillup all the inputs")
           clear()
       else:
            messagebox.showinfo("200 ok","info added sucessfully")
            f=open("Database.txt",'a')
            f.writelines("{},{},{},{}\n".format(types,names,Dates,Detail))  
            f.close()
            window1.destroy()




    def clear():
        inp.delete(0,END)
        inp1.delete(0,END)
        inp2.delete(0,END)
        inp3.delete(0,END)
    
    enter_btn=tk.Button(window1,font="itallic",bg="black",fg="blue",text="ADD",padx=30,pady=10,command=lambda:inputs())
    enter_btn.configure(activebackground='pink',cursor='dot')
    enter_btn.pack(side=TOP)
    mainloop()
   




def view_Events():
    window2=tk.Tk()
    window2.configure(bg="Black")
    window2.title("View_Events")
    window2.resizable(False,False)
    try:
        f=open('Database.txt','r')
        lis=[['Events','Name','Date','Details']]
        for i in f.readlines():
            info=i.split(',')
            lis.append(info)

        for i in range(len(lis)):
            for j in range(len(lis[0])):
                show=tk.Entry(window2, width=20, fg='blue',bg='yellow',font=('Arial',16,'bold'))
                show.grid(row=i,column=j)
                show.insert(END,lis[i][j])
                # show.config(state=DISABLED)
    except FileNotFoundError as e:
        window2.destroy()
        messagebox.showerror("no file","File not found 404")


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    class hello:
    	name=None
    	_age=None
    	__love=None
    	
    	def hello():
    		pass
    	def _hi():
    		pass
    	def __sit():
    		pass
    
