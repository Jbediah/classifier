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



        #department
        attedance_label=Label(Left_frame,text="Attendance status :",font=("times new roman",17,"bold"))
        attedance_label.grid(row=0,column=0,padx=18,pady=50,sticky=W)

        attedance_combobox=ttk.Combobox(Left_frame,font=("times new roman",17,"bold"),width=17,state="readonly")
        attedance_combobox["values"]=("Select Status","Present","Absent")
        attedance_combobox.current(0)
        attedance_combobox.grid(row=0,column=1,padx=18,pady=40,sticky=W)



        #enroll label   
        enroll_label=Label(Left_frame,text="Roll Number",font=("times new roman",17,"bold"))
        enroll_label.grid(row=2,column=0,padx=18,pady=15,sticky=W)
        enroll_label=ttk.Entry(Left_frame,width=17,font=("times new roman",17,"bold"))
        enroll_label.grid(row=2,column=1,padx=18,pady=15,sticky=W)

        #Name label   
        name_label=Label(Left_frame,text="Name",font=("times new roman",17,"bold"))
        name_label.grid(row=1,column=0,padx=18,pady=5,sticky=W)
        name_label=ttk.Entry(Left_frame,width=17,font=("times new roman",17,"bold"))
        name_label.grid(row=1,column=1,padx=18,pady=5,sticky=W)

        #branch label   
        branch_label=Label(Left_frame,text="Branch",font=("times new roman",17,"bold"))
        branch_label.grid(row=3,column=0,padx=18,pady=15,sticky=W)
        branch_label=ttk.Entry(Left_frame,width=17,font=("times new roman",17,"bold"))
        branch_label.grid(row=3,column=1,padx=18,pady=15,sticky=W)

        #time label   
        time_label=Label(Left_frame,text="Time",font=("times new roman",17,"bold"))
        time_label.grid(row=4,column=0,padx=18,pady=15,sticky=W)
        time_label=ttk.Entry(Left_frame,width=17,font=("times new roman",17,"bold"))
        time_label.grid(row=4,column=1,padx=18,pady=15,sticky=W)

        #date label   
        date_label=Label(Left_frame,text="Date",font=("times new roman",17,"bold"))
        date_label.grid(row=5,column=0,padx=18,pady=15,sticky=W)
        date_label=ttk.Entry(Left_frame,width=17,font=("times new roman",17,"bold"))
        date_label.grid(row=5,column=1,padx=18,pady=15,sticky=W)






        #rightLable Frame
        right_frame=LabelFrame(main_frame,bd=4,relief=RAISED,text="Student Details",font=("times new roman",15,"bold"))
        right_frame.place(x=630,y=10,width=550,height=500)






if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.resizable(False,False)
    root.mainloop()