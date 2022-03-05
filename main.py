from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from home import Home

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x800+0+0")
        self.root.title("Classifier")

        #backgroundImage
        img=Image.open(r"raw/test2.jpg")
        img=img.resize((1366,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=800)

        #first Label
        title_lbl=Label(f_lbl,text="Classifier",font=("times new roman",40,"bold"),fg="white",bg="black")
        title_lbl.place(x=0,y=50,width=1366,height=45)


        #button
        img2=Image.open(r"raw/log.png")
        img2=img2.resize((150,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        #imageButton1
        b1=Button(f_lbl,image=self.photoimg2,command=self.homepage,cursor="hand2")
        b1.place(x=250,y=250,width=150,height=150)
        #realButton
        b1_1=Button(f_lbl,text="Sign In",command=self.homepage,cursor="hand2")
        b1_1.place(x=250,y=400,width=150,height=30)

        #imageButton2
        img3=Image.open(r"raw/signup.png")
        img3=img3.resize((150,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        b2=Button(f_lbl,image=self.photoimg3,cursor="hand2")
        b2.place(x=600,y=250,width=150,height=150)
        #realButton
        b2_2=Button(f_lbl,text="Sign up",cursor="hand2")
        b2_2.place(x=600,y=400,width=150,height=30)

        #imageButton3
        img4=Image.open(r"raw/exit.png")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b3=Button(f_lbl,image=self.photoimg4,cursor="hand2")
        b3.place(x=950,y=250,width=150,height=150)
        #realButton
        b3_3=Button(f_lbl,text="Exit",cursor="hand2")
        b3_3.place(x=950,y=400,width=150,height=30)


    ##Function to open a new window
    def homepage(self):
        self.new_window=Toplevel(self.root)
        self.app=Home(self.new_window)




        






if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.resizable(False,False)
    root.mainloop()
