from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from tkinter import messagebox
import os

class Home:
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
        title_lbl=Label(f_lbl,text="The Desired Heading",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lbl.place(x=0,y=45,width=1366,height=55)

        #imageButton1
        img1=Image.open(r"raw/details.png")
        img1=img1.resize((150,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        b1=Button(f_lbl,image=self.photoimg1,command=self.student_page,cursor="hand2")
        b1.place(x=200,y=250,width=150,height=150)
        #realButton
        b1_1=Button(f_lbl,text="Student Details",command=self.student_page,cursor="hand2")
        b1_1.place(x=200,y=400,width=150,height=30)

        #imageButton2
        img2=Image.open(r"raw/photos.png")
        img2=img2.resize((150,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        b2=Button(f_lbl,image=self.photoimg2,command=self.open_img,cursor="hand2")
        b2.place(x=500,y=250,width=150,height=150)
        #realButton
        b2_2=Button(f_lbl,text="Photos",command=self.open_img,cursor="hand2")
        b2_2.place(x=500,y=400,width=150,height=30)


        #imageButton3
        img3=Image.open(r"raw/train.png")
        img3=img3.resize((150,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        b3=Button(f_lbl,image=self.photoimg3,command=self.train_data_page,cursor="hand2")
        b3.place(x=800,y=250,width=150,height=150)
        #realButton
        b3_3=Button(f_lbl,text="Train Data",command=self.train_data_page,cursor="hand2")
        b3_3.place(x=800,y=400,width=150,height=30)


 ##Function to open student window
    def student_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

 ##Function to traindata  window
    def train_data_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)





    #function to open photos directory
    def open_img(self):
        messagebox.showerror("error","Acess denied!",parent=self.root)















if __name__=="__main__":
    root=Tk()
    obj=Home(root)
    root.resizable(False,False)
    root.mainloop()