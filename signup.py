from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from home import Home
from tkinter import messagebox
import sqlite3

class SignUp:
    def __init__(self,root):
        self.root=root
        self.root.geometry("450x750+740+200")#1366x800
        self.root.title("Classifier")

        ##variable dec
        self.var_user=StringVar()
        self.var_pass=StringVar()

        #backgroundImage
        img=Image.open(r"raw/bg4.jpg")
        img=img.resize((450,750),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=750)

        #frame
        img1=Image.open(r"raw/bg1.jpg")
        img1=img1.resize((450,750),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        main_frame=Frame(f_lbl,bd=12,relief=RIDGE)
        main_frame.place(x=80,y=150,width=300,height=420)

        bg_lbl=Label(main_frame,image=self.photoimg1)
        bg_lbl.place(x=0,y=0,width=276,height=396)



        #user label   
        user_label=Label(main_frame,text="Username",bg="black",fg="white",font=("times new roman",20,"bold"))
        user_label.place(x=80,y=65)
        user_label=ttk.Entry(main_frame,textvariable=self.var_user,width=16,font=("times new roman",20,"bold"))
        user_label.place(x=30,y=105)

        #pass label   
        pass_label=Label(main_frame,text="Password",bg="black",fg="white",font=("times new roman",20,"bold"))
        pass_label.place(x=80,y=170)
        pass_label=ttk.Entry(main_frame,textvariable=self.var_pass,width=16,font=("times new roman",20,"bold"))
        pass_label.place(x=30,y=210)

        

        #button
        login_btn=Button(main_frame,command=self.sign_up,text="sign up",bg="black",fg="white",cursor="hand2",font=("times new roman",18,"bold"))
        login_btn.place(x=85,y=280)





    #fetching details from database
    def fetch_data(self):
        conn=sqlite3.connect('classifier_db.db')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from user_details")
        data=my_cursor.fetchall()

        
        conn.commit()
        conn.close()


    #on clicking sign up button
    def sign_up(self):
        if self.var_user.get()=="" or self.var_pass.get()=="":
            messagebox.showerror("error","field left blank",parent=self.root)
        else:
            try:
                conn=sqlite3.connect('classifier_db.db')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into user_details values(?,?)",(self.var_user.get(),self.var_pass.get()))

                conn.commit()
                self.fetch_data()   
                conn.close()
                messagebox.showinfo("info","user details has been added successfully!",parent=self.root)
                self.root.withdraw()

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)







if __name__=="__main__":
    root=Tk()
    obj=SignUp(root)
    root.resizable(False,False)
    root.mainloop()
