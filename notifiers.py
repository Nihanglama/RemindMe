from tkinter import font, messagebox,ttk
import tkinter as tk
from time import sleep, strftime
from tkinter import *
from tkinter.ttk import *
  

def main():
    window= tk.Tk()
    window.title("REMIND_ME")
    window.geometry("800x800")
    window.configure(bg="black")
    window.resizable(False,False)
    label1=tk.Label(fg='white',font=("itallic",20),bg="black")
    label1.pack(anchor="n")
    label=tk.Label(text="REMAIN UPTO DATE",foreground="white",bg="green",font=("Itallic",20),height=5,width=100)
    label.pack(anchor='center')

    text_area=tk.Label(text="Recent events to show",fg="black",bg="white",width=500,height=10,pady=5,padx=5)
    text_area.pack()

    add_btn=tk.Button(command=lambda:add_event(),font="itallic",bg="black",fg="blue",text="Add_Events",padx=30,pady=10)
    add_btn.place(x=310,y=400)
    add_btn.configure(activebackground='navy',activeforeground='black')

    alram_btn=tk.Button(window,command=lambda:add_alram(),text="Add_alaram",font="itallic",bg="black",fg="blue",padx=30,pady=10)
    alram_btn.place(x=310,y=470)
    alram_btn.configure(activebackground='navy',activeforeground='black')

    view_btn=tk.Button(command=lambda:view_Events(),font="itallic",bg="black",fg="blue",text="View_allEvents",padx=30,pady=10)
    view_btn.place(x=300,y=550)
    view_btn.configure(activebackground='navy',activeforeground='black')

    def check():
        c_time=strftime("%H:%M:%p")
        lis1=[]
        try:
            f=open('Time.txt','r')
            for line in f.readlines():
                words=line.replace('\n','')
                words=words.split(',')
                lis1.append(words)
            f.close()
        except FileNotFoundError as e:
            f=open('Time.txt','w')
            f.close()
        print(c_time)

        for i in range(len(lis1)):
            a_time=":".join(lis1[i])
        
            if a_time==c_time:
                text_area.config(text=c_time)
                print(a_time)
                messagebox.showinfo("Reminder","Wake UP Wake UP......")
  
        text_area.after(60000,check)
        
    check()

    # check()  

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
        f.close()
        for i in range(len(lis)):
            for j in range(len(lis[0])):
                show=tk.Entry(window2, width=20, fg='blue',bg='yellow',font=('Arial',16,'bold'))
                show.grid(row=i,column=j)
                show.insert(END,lis[i][j])
                # show.config(state=DISABLED)
    except FileNotFoundError as e:
        window2.destroy()
        messagebox.showerror("no file","File not found 404")


def add_alram():
    window3=tk.Tk()
    window3.configure(bg="black")
    window3.title("Set_Alram")
    window3.geometry("500x600")
    # window3.resizable(False,False)
    inps=ttk.LabelFrame(window3,text="Forms",border=5,borderwidth=10)
    inps.pack(fill='both',expand='yes')
    show1=tk.Label(inps,text="Hours",fg="black")
    show1.pack()
    inp1=tk.Entry(inps,fg="black",bd=5)
    inp1.pack()
    show2=tk.Label(inps,text="Minutes",fg="black")
    show2.pack()
    inp2=tk.Entry(inps,fg="black",bd=5)
    inp2.pack()
    show3=tk.Label(inps,text="AM/PM",fg="black")
    show3.pack()
    inp3=tk.Entry(inps,fg="black",bd=5)
    inp3.pack()
    set_btn=tk.Button(inps,text="SET",bg="black",fg="white",padx=20,pady=10,bd=3,command=lambda:inputs())
    set_btn.pack()
    set_btn.configure(activebackground="skyblue")


    def clear():
        inp1.delete(0,END)
        inp2.delete(0,END)
        inp3.delete(0,END)

    def inputs():
       global hour
       global minute
       global specifier
    
       hour=inp1.get()
       minute=inp2.get()
       specifier=inp3.get()
       

       if hour=="" or minute=="" or specifier=="":
           messagebox.showwarning("Error 300","Please fillup all the inputs")
           clear()
       elif hour.isalpha() or minute.isalpha() or specifier.isdigit():
           messagebox.showwarning("Error 102","Wrong input format")
           messagebox.showinfo("Guide","format: \n hour:__\nminute:__\nSpecifier:AM/PM")
           clear()

       else:
            messagebox.showinfo("200 ok","info added sucessfully")
            global m
            global hr
            m=int(minute)
            hr=int(hour)
            if int(m)>=60:
                hr+=int(m/60)
                m=(m%60)
            if int(hr)>12:
                 hr=(hr%12)

            f=open("Time.txt",'a')

            f.writelines("{},{},{}\n".format(hr,m,specifier))  
            f.close()
            window3.destroy()   
    show_al_btn=tk.Button(window3,text="Show Alaram",fg="white",bg="black",bd=4,command=lambda:show())
    show_al_btn.pack()
    def show():
        show_al_btn.destroy()
        f=open('Time.txt','r')
        lis=[]
        for line in f.readlines():
            words=line.replace('\n','')
            words=words.split(',')
            lis.append(words)
        f.close()
        def delete():
            f=open("Time.txt",'r+')
            f.truncate(0)
            messagebox.showwarning("Deleting","Are you sure to delete ?")
            frame.destroy()


        frame=ttk.LabelFrame(window3,text="Alram",borderwidth=10,border=5)
        frame.pack(fill='both',expand='yes')
        print(lis)
        if len(lis)!=0:
            for i in range(len(lis)):
                j=50
                show=tk.Label(frame,fg='blue',font=('Arial',16,'bold'),text=lis[i])
                show.pack(side=TOP)
            
                j+=50

            del_btn=tk.Button(frame,fg='white',bg='black',padx=3,pady=5,text="delete",bd=3,command=lambda:delete())
            del_btn.pack(side=TOP)
    



if __name__ == "__main__":
    main()



    
    
