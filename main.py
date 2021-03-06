from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from home import Home
from login import Login
from signup import SignUp

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")#1366x800
        self.root.title("Classifier")

        #backgroundImage
        img=Image.open(r"raw/test2.jpg")
        img=img.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1920,height=1080)

        #first Label
        title_lbl=Label(f_lbl,text="Classifier",font=("times new roman",40,"bold"),fg="white",bg="black")
        title_lbl.place(x=0,y=50,width=1920,height=45)


        #button
        img2=Image.open(r"raw/log.png")
        img2=img2.resize((250,250),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        #imageButton1
        b1=Button(f_lbl,image=self.photoimg2,command=self.login,cursor="hand2")
        b1.place(x=300,y=350,width=250,height=250)
        #realButton
        b1_1=Button(f_lbl,text="Sign In",command=self.login,cursor="hand2")
        b1_1.place(x=300,y=600,width=250,height=30)

        #imageButton2
        img3=Image.open(r"raw/signup.png")
        img3=img3.resize((250,250),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        b2=Button(f_lbl,image=self.photoimg3,command=self.signup,cursor="hand2")
        b2.place(x=850,y=350,width=250,height=250)
        #realButton
        b2_2=Button(f_lbl,text="Sign up",command=self.signup,cursor="hand2")
        b2_2.place(x=850,y=600,width=250,height=30)

        #imageButton3
        img4=Image.open(r"raw/exit.png")
        img4=img4.resize((250,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b3=Button(f_lbl,image=self.photoimg4,command=exit,cursor="hand2")
        b3.place(x=1400,y=350,width=250,height=250)
        #realButton
        b3_3=Button(f_lbl,text="Exit",command=exit,cursor="hand2")
        b3_3.place(x=1400,y=600,width=250,height=30)


    ##Function to open a new window
    def login(self):
        self.new_window=Toplevel(self.root)
        self.new_window.resizable(False,False)
        self.app=Login(self.new_window)

    def signup(self):
        self.new_window=Toplevel(self.root)
        self.new_window.resizable(False,False)
        self.app=SignUp(self.new_window)


    def exit():
        self.root.destroy()





        






if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.resizable(False,False)
    root.mainloop()
