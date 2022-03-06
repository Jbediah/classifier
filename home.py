from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_recognition
from tkinter import messagebox
import os

class Home:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Classifier")

        #backgroundImage
        img=Image.open(r"raw/test2.jpg")
        img=img.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1920,height=1080)

         #first Label
        title_lbl=Label(f_lbl,text="HOME",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lbl.place(x=0,y=45,width=1920,height=45)

        #imageButton1
        img1=Image.open(r"raw/details.png")
        img1=img1.resize((250,250),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        b1=Button(f_lbl,image=self.photoimg1,command=self.student_page,cursor="hand2")
        b1.place(x=120,y=210,width=250,height=250)
        #realButton
        b1_1=Button(f_lbl,text="Student Details",command=self.student_page,cursor="hand2")
        b1_1.place(x=120,y=460,width=250,height=30)

        #imageButton2
        img2=Image.open(r"raw/photos.png")
        img2=img2.resize((250,250),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        b2=Button(f_lbl,image=self.photoimg2,command=self.open_img,cursor="hand2")
        b2.place(x=485,y=600,width=250,height=250)
        #realButton
        b2_2=Button(f_lbl,text="Photos",command=self.open_img,cursor="hand2")
        b2_2.place(x=485,y=850,width=250,height=30)


        #imageButton3
        img3=Image.open(r"raw/train.png")
        img3=img3.resize((250,250),Image.ANTIALIAS) 
        self.photoimg3=ImageTk.PhotoImage(img3)


        b3=Button(f_lbl,image=self.photoimg3,command=self.train_data_page,cursor="hand2")
        b3.place(x=850,y=210,width=250,height=250)
        #realButton
        b3_3=Button(f_lbl,text="Train Data",command=self.train_data_page,cursor="hand2")
        b3_3.place(x=850,y=460,width=250,height=30)

        #imageButton4
        img4=Image.open(r"raw/facial-recognition.png")
        img4=img4.resize((250,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)


        b4=Button(f_lbl,image=self.photoimg4,command=self.facial_recog_page,cursor="hand2")
        b4.place(x=1550,y=210,width=250,height=250)
        #realButton
        b4_4=Button(f_lbl,text="Attendance",command=self.facial_recog_page,cursor="hand2")
        b4_4.place(x=1550,y=460,width=250,height=30)


        #imageButton5
        img5=Image.open(r"raw/attendance.png")
        img5=img5.resize((250,250),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)


        b5=Button(f_lbl,image=self.photoimg5,command=self.facial_recog_page,cursor="hand2")
        b5.place(x=1200,y=600,width=250,height=250)
        #realButton
        b5_5=Button(f_lbl,text="Show Attendance",command=self.facial_recog_page,cursor="hand2")
        b5_5.place(x=1200,y=850,width=250,height=30)


 ##Function to open student window
    def student_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

 ##Function to traindata  window
    def train_data_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

##Function to facialrecog  window
    def facial_recog_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)




    #function to open photos directory
    def open_img(self):
        messagebox.showerror("error","Acess denied!",parent=self.root)















if __name__=="__main__":
    root=Tk()
    obj=Home(root)
    #root.resizable(False,False)
    root.mainloop()