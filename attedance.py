from tkinter import *   
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from tkinter import messagebox
import os
import numpy as np
import cv2

class Attendance:
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
        title_lbl=Label(f_lbl,text="Attendance Management System",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lbl.place(x=0,y=45,width=1366,height=55)


        #frame
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=70,y=160,width=1200,height=580)

        #leftLable Frame
        Left_frame=LabelFrame(main_frame,bd=4,relief=RAISED,text="Student Details",font=("times new roman",15,"bold"))
        Left_frame.place(x=30,y=10,width=550,height=500)



        #rightLable Frame
        right_frame=LabelFrame(main_frame,bd=4,relief=RAISED,text="Student Details",font=("times new roman",15,"bold"))
        right_frame.place(x=630,y=10,width=550,height=500)






if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.resizable(False,False)
    root.mainloop()