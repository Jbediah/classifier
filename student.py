from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import cv2
import os


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x800+0+0")
        self.root.title("Classifier")

        #---------------------variables--------------
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_eno=StringVar()
        self.var_name=StringVar()
        self.var_mob=StringVar()
        self.var_dob=StringVar()
        self.var_mail=StringVar()
        self.var_gender=StringVar()
        self.var_faculty=StringVar()
        self.var_radio=StringVar()

        

        #backgroundImage
        img=Image.open(r"raw/test2.jpg")
        img=img.resize((1500,1000),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=800)

         #first Label
        title_lbl=Label(f_lbl,text="Student Details",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lbl.place(x=0,y=20,width=1366,height=35)

        

        #frame
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=10,y=80,width=1320,height=700)

        #leftLable Frame
        Left_frame=LabelFrame(main_frame,bd=4,relief=RAISED,text="Student Details",font=("times new roman",15,"bold"))
        Left_frame.place(x=30,y=10,width=620,height=670)

        #current course
        current_frame=LabelFrame(Left_frame,bd=4,relief=RAISED,text="Current Details",font=("times new roman",15,"bold"))
        current_frame.place(x=20,y=30,width=580,height=140)
        
        #department
        dep_label=Label(current_frame,text="Department",font=("times new roman",15,"bold"))
        dep_label.grid(row=0,column=0,padx=8,pady=10,sticky=W)

        dep_combobox=ttk.Combobox(current_frame,textvariable=self.var_dep,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combobox["values"]=("Select Department","CSE","CSE-Data Science","CSE-AI/ML","CS-Business Systems","Information Technology","Electrical and Electronics","Electronics and Communication","Mechanical","Civil","Automobile")
        dep_combobox.current(0)
        dep_combobox.grid(row=0,column=1,padx=3,pady=12,sticky=W)

        #course
        course_label=Label(current_frame,text="Course",font=("times new roman",15,"bold"))
        course_label.grid(row=0,column=2,padx=8,sticky=W)

        course_combobox=ttk.Combobox(current_frame,textvariable=self.var_course,font=("times new roman",14,"bold"),width=17,state="readonly")
        course_combobox["values"]=("Select Course","Mathematics","Data Structures","Operating Systems","Database Management System","OOP","Data Science","Software Engineering","Python","Discrete Structures","Computer Networks")
        course_combobox.current(0)
        course_combobox.grid(row=0,column=3,padx=3,pady=12,sticky=W)

        #year
        year_label=Label(current_frame,text="Year",font=("times new roman",15,"bold"))
        year_label.grid(row=1,column=0,padx=8,sticky=W)

        year_combobox=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",14,"bold"),width=17,state="readonly")
        year_combobox["values"]=("Select Year","1","2","3","4")
        year_combobox.current(0)
        year_combobox.grid(row=1,column=1,padx=3,pady=12,sticky=W)

        #semester
        sem_label=Label(current_frame,text="Semester",font=("times new roman",15,"bold"))
        sem_label.grid(row=1,column=2,padx=8,sticky=W)

        sem_combobox=ttk.Combobox(current_frame,textvariable=self.var_sem,font=("times new roman",14,"bold"),width=17,state="readonly")
        sem_combobox["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combobox.current(0)
        sem_combobox.grid(row=1,column=3,padx=3,pady=12,sticky=W)



        #student information
        studentInformation_frame=LabelFrame(Left_frame,bd=4,relief=RAISED,text="Student Information",font=("times new roman",15,"bold"))
        studentInformation_frame.place(x=20,y=180,width=580,height=440)
        #Enrollment label
        enrollment_label=Label(studentInformation_frame,text="Student ID",font=("times new roman",14,"bold"))
        enrollment_label.grid(row=0,column=0,padx=40,pady=7,sticky=W)
        enrollment_label=ttk.Entry(studentInformation_frame,textvariable=self.var_eno,width=17,font=("times new roman",14,"bold"))
        enrollment_label.grid(row=0,column=1,padx=40,pady=7,sticky=W)

        #Name label   
        name_label=Label(studentInformation_frame,text="Name",font=("times new roman",14,"bold"))
        name_label.grid(row=1,column=0,padx=40,pady=7,sticky=W)
        name_label=ttk.Entry(studentInformation_frame,textvariable=self.var_name,width=17,font=("times new roman",14,"bold"))
        name_label.grid(row=1,column=1,padx=40,pady=7,sticky=W)

        #Phone number label
        phnum_label=Label(studentInformation_frame,text="Phone Number",font=("times new roman",14,"bold"))
        phnum_label.grid(row=2,column=0,padx=40,pady=7,sticky=W)
        phnum_label=ttk.Entry(studentInformation_frame,textvariable=self.var_mob,width=17,font=("times new roman",14,"bold"))
        phnum_label.grid(row=2,column=1,padx=40,pady=7,sticky=W)

        #dob label
        dob_label=Label(studentInformation_frame,text="Date of birth",font=("times new roman",14,"bold"))
        dob_label.grid(row=3,column=0,padx=40,pady=7,sticky=W)
        dob_label=ttk.Entry(studentInformation_frame,textvariable=self.var_dob,width=17,font=("times new roman",14,"bold"))
        dob_label.grid(row=3,column=1,padx=40,pady=7,sticky=W)

        #email label
        email_label=Label(studentInformation_frame,text="Email",font=("times new roman",14,"bold"))
        email_label.grid(row=4,column=0,padx=40,pady=7,sticky=W)
        email_label=ttk.Entry(studentInformation_frame,textvariable=self.var_mail,width=17,font=("times new roman",14,"bold"))
        email_label.grid(row=4,column=1,padx=40,pady=7,sticky=W)

        #gender label
        gender_label=Label(studentInformation_frame,text="Gender",font=("times new roman",14,"bold"))
        gender_label.grid(row=5,column=0,padx=40,pady=7,sticky=W)
        #gender_label=ttk.Entry(studentInformation_frame,textvariable=self.var_gender,width=17,font=("times new roman",14,"bold"))
        #gender_label.grid(row=5,column=1,padx=40,pady=7,sticky=W)

        ###combobox here
        gender_combobox=ttk.Combobox(studentInformation_frame,textvariable=self.var_gender,font=("times new roman",14,"bold"),width=17,state="readonly")
        gender_combobox["values"]=("Select Gender","Male","Female")
        gender_combobox.current(0)
        gender_combobox.grid(row=5,column=1,padx=40,pady=7,sticky=W)

        #facultyname label
        facultyname_label=Label(studentInformation_frame,text="Faculty Name",font=("times new roman",14,"bold"))
        facultyname_label.grid(row=6,column=0,padx=40,pady=7,sticky=W)
        facultyname_label=ttk.Entry(studentInformation_frame,textvariable=self.var_faculty,width=17,font=("times new roman",14,"bold"))
        facultyname_label.grid(row=6,column=1,padx=40,pady=7,sticky=W)


        #radiobuttons
        radiobtn1=ttk.Radiobutton(studentInformation_frame,variable=self.var_radio,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=7,column=0)
        
        radiobtn2=ttk.Radiobutton(studentInformation_frame,variable=self.var_radio,text="No Photo Sample",value="No")
        radiobtn2.grid(row=7,column=1)

        #frame for buttons
        btn_frame=Frame(studentInformation_frame,bd=4,relief=RAISED)
        btn_frame.place(x=10,y=320,width=554,height=43)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",14,"bold"),width=12)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",14,"bold"),width=12)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",14,"bold"),width=12)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,font=("times new roman",14,"bold"),width=12)
        reset_btn.grid(row=0,column=3)

        #frame for buttons below

        btn_frame1=Frame(studentInformation_frame,bd=4,relief=RAISED)
        btn_frame1.place(x=10,y=360,width=554,height=43)

        take_btn=Button(btn_frame1,text="Take a Photo Sample",command=self.generate_dataset,font=("times new roman",14,"bold"),width=27)
        take_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame1,text="Update Photo Sample",command=self.generate_dataset,font=("times new roman",14,"bold"),width=27)
        update_btn.grid(row=0,column=1)





        #RightLable Frame
        Right_frame=LabelFrame(main_frame,bd=4,relief=RAISED,text="Student Details",font=("times new roman",15,"bold"))
        Right_frame.place(x=680,y=10,width=620,height=650)


        ##search frame
        search_frame=LabelFrame(Right_frame,bd=4,relief=RAISED,text="Search Frame",font=("times new roman",15,"bold"))
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
        table_frame=LabelFrame(Right_frame,bd=4,relief=RAISED,)
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


        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


     #Fuctions for various operations
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Department" or self.var_year.get()=="Select Department" or self.var_sem.get()=="Select Department" or self.var_eno.get()=="" or self.var_name.get()=="" or self.var_mob.get()=="" or self.var_dob.get()=="" or self.var_mail.get()=="" or self.var_gender.get()=="" or self.var_faculty.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
            try:
                conn=sqlite3.connect('classifier_db.db')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_details values(?,?,?,?,?,?,?,?,?,?,?,?)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_eno.get(),self.var_name.get(),self.var_mob.get(),self.var_dob.get(),self.var_mail.get(),self.var_gender.get(),self.var_faculty.get(),self.var_radio.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("info","Student details has been added successfully!",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #fetching details from database
    def fetch_data(self):
        conn=sqlite3.connect('classifier_db.db')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_details")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor function.....to show details in fields from table
    
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_eno.set(data[4]),
        self.var_name.set(data[5]),
        self.var_mob.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_mail.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_faculty.set(data[10]),
        self.var_radio.set(data[11]),


    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Department" or self.var_year.get()=="Select Department" or self.var_sem.get()=="Select Department" or self.var_eno.get()=="" or self.var_name.get()=="" or self.var_mob.get()=="" or self.var_dob.get()=="" or self.var_mail.get()=="" or self.var_gender.get()=="" or self.var_faculty.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        
        else:
            try:
                Update=messagebox.askyesno("update","Do you want to update with these details?",parent=self.root)
                if Update>0:
                    conn=sqlite3.connect('classifier_db.db')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student_details set dep=?,course=?,year=?,sem=?,name=?,mob=?,dob=?,mail=?,gender=?,faculty=?,sample=? where enroll=?",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_name.get(),self.var_mob.get(),self.var_dob.get(),self.var_mail.get(),self.var_gender.get(),self.var_faculty.get(),self.var_radio.get(),self.var_eno.get()))

                else:
                    if not Update:
                        return
                messagebox.showinfo("success","student details updated successfully!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)



    #delete function
    def delete_data(self):
        if self.var_eno.get()=="":
            messagebox.showerror("error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("info","Are you sure you want to delete this student",parent=self.root)
                
                if delete>0:
                    conn=sqlite3.connect('classifier_db.db')
                    my_cursor=conn.cursor()
                    sql="delete from student_details where enroll=?"
                    val=(self.var_eno.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("info","Successfully deleted student details !",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)



    #reset fuction
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_eno.set("")
        self.var_name.set("")
        self.var_mob.set("")
        self.var_dob.set("")
        self.var_mail.set("")
        self.var_gender.set("Select Gender")
        self.var_faculty.set("")
        self.var_radio.set("")

        


    #OPEN CV PART
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Department" or self.var_year.get()=="Select Department" or self.var_sem.get()=="Select Department" or self.var_eno.get()=="" or self.var_name.get()=="" or self.var_mob.get()=="" or self.var_dob.get()=="" or self.var_mail.get()=="" or self.var_gender.get()=="" or self.var_faculty.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        
        else:
            try:
                conn=sqlite3.connect('classifier_db.db')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_details")
                myresult=my_cursor.fetchall()
                id=0
                
                for x in myresult:
                    id+=1
                id=self.var_eno .get()
                my_cursor.execute("update student_details set dep=?,course=?,year=?,sem=?,name=?,mob=?,dob=?,mail=?,gender=?,faculty=?,sample=? where enroll=?",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_name.get(),self.var_mob.get(),self.var_dob.get(),self.var_mail.get(),self.var_gender.get(),self.var_faculty.get(),self.var_radio.get(),self.var_eno.get()))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #loading data from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scalingFactor=1.3 and Minimum neighbou3=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame), (450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating datasets completed!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
  

                


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.resizable(False,False)
    root.mainloop()