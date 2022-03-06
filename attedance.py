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
        self.root.geometry("1920x1080+0+0")
        self.root.title("Classifier")

        #backgroundImage
        img=Image.open(r"raw/test2.jpg")
        img=img.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg,bd=12)
        f_lbl.place(x=0,y=0,width=1920,height=1080)

         #first Label
        title_lbl=Label(f_lbl,text="Attendance Management System",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lbl.place(x=0,y=45,width=1900,height=55)


        #frame
        main_frame=Frame(f_lbl,bd=12,relief=RIDGE)
        main_frame.place(x=100,y=160,width=1700,height=760)

        #leftLable Frame
        Left_frame=LabelFrame(main_frame,bd=12,relief=RIDGE,text="Add Attendance",font=("times new roman",20,"bold"))
        Left_frame.place(x=30,y=50,width=800,height=660)



        #department
        attedance_label=Label(Left_frame,text="Attendance status :",font=("times new roman",20,"bold"))
        attedance_label.grid(row=0,column=0,padx=65,pady=50,sticky=W)

        attedance_combobox=ttk.Combobox(Left_frame,font=("times new roman",20,"bold"),width=17,state="readonly")
        attedance_combobox["values"]=("Select Status","Present","Absent")
        attedance_combobox.current(0)
        attedance_combobox.grid(row=0,column=1,padx=65,pady=40,sticky=W)



        #enroll label   
        enroll_label=Label(Left_frame,text="Roll Number",font=("times new roman",20,"bold"))
        enroll_label.grid(row=2,column=0,padx=65,pady=15,sticky=W)
        enroll_label=ttk.Entry(Left_frame,width=17,font=("times new roman",20,"bold"))
        enroll_label.grid(row=2,column=1,padx=65,pady=15,sticky=W)

        #Name label   
        name_label=Label(Left_frame,text="Name",font=("times new roman",20,"bold"))
        name_label.grid(row=1,column=0,padx=65,pady=5,sticky=W)
        name_label=ttk.Entry(Left_frame,width=17,font=("times new roman",20,"bold"))
        name_label.grid(row=1,column=1,padx=65,pady=5,sticky=W)

        #branch label   
        branch_label=Label(Left_frame,text="Branch",font=("times new roman",20,"bold"))
        branch_label.grid(row=3,column=0,padx=65,pady=20,sticky=W)
        branch_label=ttk.Entry(Left_frame,width=17,font=("times new roman",20,"bold"))
        branch_label.grid(row=3,column=1,padx=65,pady=20,sticky=W)

        #time label   
        time_label=Label(Left_frame,text="Time",font=("times new roman",20,"bold"))
        time_label.grid(row=4,column=0,padx=65,pady=20,sticky=W)
        time_label=ttk.Entry(Left_frame,width=17,font=("times new roman",20,"bold"))
        time_label.grid(row=4,column=1,padx=65,pady=20,sticky=W)

        #date label   
        date_label=Label(Left_frame,text="Date",font=("times new roman",20,"bold"))
        date_label.grid(row=5,column=0,padx=65,pady=20,sticky=W)
        date_label=ttk.Entry(Left_frame,width=17,font=("times new roman",20,"bold"))
        date_label.grid(row=5,column=1,padx=65,pady=20,sticky=W)




        #frame for buttons
        btn_frame=Frame(Left_frame,bd=6,relief=RAISED)
        btn_frame.place(x=10,y=510,width=760,height=56)

        save_btn=Button(btn_frame,text="Export to CSV",padx=13,font=("times new roman",17,"bold"),width=14)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Import from CSV",padx=13,font=("times new roman",17,"bold"),width=14)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",padx=13,font=("times new roman",17,"bold"),width=14)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",padx=13,font=("times new roman",17,"bold"),width=14)
        reset_btn.grid(row=0,column=3)







        #rightLable Frame
        right_frame=LabelFrame(main_frame,bd=12,relief=RIDGE,text="Attendance Status",font=("times new roman",20,"bold"))
        right_frame.place(x=860,y=50,width=800,height=660)

        ##search frame
        search_frame=LabelFrame(right_frame,bd=4,relief=RAISED,text="Search Frame",font=("times new roman",15,"bold"))
        search_frame.place(x=20,y=30,width=580,height=180)

        search_label=Label(search_frame,text="Search by :",font=("times new roman",17,"bold"))
        search_label.grid(row=0,column=0,padx=15,pady=16,sticky=W)

        search_combobox=ttk.Combobox(search_frame,font=("times new roman",17,"bold"),width=17,state="readonly")
        search_combobox["values"]=("Select","Enrollment Number","Phone Number",)
        search_combobox.current(0)
        search_combobox.grid(row=0,column=1,padx=15,pady=16,sticky=W)

        search_entry=ttk.Entry(search_frame,width=14,font=("times new roman",17,"bold"))
        search_entry.grid(row=0,column=2,padx=15,pady=16,sticky=W)

        search_btn=Button(search_frame,text="Search",font=("times new roman",16,"bold"),width=8)
        search_btn.grid(row=1,column=1,pady=10)

        show_btn=Button(search_frame,text="Show all",font=("times new roman",16,"bold"),width=8)
        show_btn.grid(row=1,column=2,pady=10)


        ##table form
        table_frame=LabelFrame(right_frame,bd=4,relief=RAISED,)
        table_frame.place(x=20,y=240,width=580,height=360)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","enroll","name","mob","dob","email","gender","faculty","sample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("enroll",text="Enrollment")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("mob",text="MobNo")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("faculty",text="Faculty")
        self.student_table.heading("sample",text="PhotoSample")

        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("enroll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("mob",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("faculty",width=100)
        self.student_table.column("sample",width=100)
        
        
        


        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)


        







if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    #root.resizable(False,False)
    root.mainloop()