from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x800+0+0")
        self.root.title("Classifier")

        #---------------------variables--------------
        self.var_eno=StringVar()
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_name=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_mob=StringVar()
        self.var_mail=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_faculty=StringVar()

        

        #backgroundImage
        img=Image.open(r"/home/jbediah/Documents/classifier/raw/test2.jpg")
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
        Left_frame.place(x=30,y=10,width=620,height=650)

        #current course
        current_frame=LabelFrame(Left_frame,bd=4,relief=RAISED,text="Current Details",font=("times new roman",15,"bold"))
        current_frame.place(x=20,y=30,width=580,height=180)
        
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
        course_combobox["values"]=("Select Course","CSE","CSE-Data Science","CSE-AI/ML","CS-Business Systems","Information Technology","Electrical and Electronics","Electronics and Communication","Mechanical","Civil","Automobile")
        course_combobox.current(0)
        course_combobox.grid(row=0,column=3,padx=3,pady=12,sticky=W)

        #year
        year_label=Label(current_frame,text="Year",font=("times new roman",15,"bold"))
        year_label.grid(row=1,column=0,padx=8,sticky=W)

        year_combobox=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",14,"bold"),width=17,state="readonly")
        year_combobox["values"]=("Select Year","CSE","CSE-Data Science","CSE-AI/ML","CS-Business Systems","Information Technology","Electrical and Electronics","Electronics and Communication","Mechanical","Civil","Automobile")
        year_combobox.current(0)
        year_combobox.grid(row=1,column=1,padx=3,pady=12,sticky=W)

        #semester
        sem_label=Label(current_frame,text="Semester",font=("times new roman",15,"bold"))
        sem_label.grid(row=1,column=2,padx=8,sticky=W)

        sem_combobox=ttk.Combobox(current_frame,textvariable=self.var_sem,font=("times new roman",14,"bold"),width=17,state="readonly")
        sem_combobox["values"]=("Select Semester","CSE","CSE-Data Science","CSE-AI/ML","CS-Business Systems","Information Technology","Electrical and Electronics","Electronics and Communication","Mechanical","Civil","Automobile")
        sem_combobox.current(0)
        sem_combobox.grid(row=1,column=3,padx=3,pady=12,sticky=W)



        #student information
        studentInformation_frame=LabelFrame(Left_frame,bd=4,relief=RAISED,text="Student Information",font=("times new roman",15,"bold"))
        studentInformation_frame.place(x=20,y=240,width=580,height=370)
        #Enrollment label
        enrollment_label=Label(studentInformation_frame,text="Enrollment No.",font=("times new roman",15,"bold"))
        enrollment_label.grid(row=0,column=0,padx=60,pady=7,sticky=W)
        enrollment_label=ttk.Entry(studentInformation_frame,textvariable=self.var_eno,width=17,font=("times new roman",14,"bold"))
        enrollment_label.grid(row=0,column=1,padx=60,pady=7,sticky=W)

        #Name label   
        name_label=Label(studentInformation_frame,text="Name",font=("times new roman",15,"bold"))
        name_label.grid(row=1,column=0,padx=60,pady=7,sticky=W)
        name_label=ttk.Entry(studentInformation_frame,textvariable=self.var_name,width=17,font=("times new roman",14,"bold"))
        name_label.grid(row=1,column=1,padx=60,pady=7,sticky=W)

        #Phone number label
        phnum_label=Label(studentInformation_frame,text="Phone Number",font=("times new roman",15,"bold"))
        phnum_label.grid(row=2,column=0,padx=60,pady=7,sticky=W)
        phnum_label=ttk.Entry(studentInformation_frame,textvariable=self.var_mob,width=17,font=("times new roman",14,"bold"))
        phnum_label.grid(row=2,column=1,padx=60,pady=7,sticky=W)

        #dob label
        dob_label=Label(studentInformation_frame,text="Date of birth",font=("times new roman",15,"bold"))
        dob_label.grid(row=3,column=0,padx=60,pady=7,sticky=W)
        dob_label=ttk.Entry(studentInformation_frame,textvariable=self.var_dob,width=17,font=("times new roman",14,"bold"))
        dob_label.grid(row=3,column=1,padx=60,pady=7,sticky=W)

        #email label
        email_label=Label(studentInformation_frame,text="Email",font=("times new roman",15,"bold"))
        email_label.grid(row=4,column=0,padx=60,pady=7,sticky=W)
        email_label=ttk.Entry(studentInformation_frame,textvariable=self.var_mail,width=17,font=("times new roman",14,"bold"))
        email_label.grid(row=4,column=1,padx=60,pady=7,sticky=W)

        #gender label
        gender_label=Label(studentInformation_frame,text="Gender",font=("times new roman",15,"bold"))
        gender_label.grid(row=4,column=0,padx=60,pady=7,sticky=W)
        gender_label=ttk.Entry(studentInformation_frame,textvariable=self.var_gender,width=17,font=("times new roman",14,"bold"))
        gender_label.grid(row=4,column=1,padx=60,pady=7,sticky=W)

        #facultyname label
        facultyname_label=Label(studentInformation_frame,text="Faculty Name",font=("times new roman",15,"bold"))
        facultyname_label.grid(row=4,column=0,padx=60,pady=7,sticky=W)
        facultyname_label=ttk.Entry(studentInformation_frame,textvariable=self.var_faculty,width=17,font=("times new roman",14,"bold"))
        facultyname_label.grid(row=4,column=1,padx=60,pady=7,sticky=W)


        #radiobuttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(studentInformation_frame,textvariable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
        
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(studentInformation_frame,textvariable=self.var_radio2,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #frame for buttons
        btn_frame=Frame(studentInformation_frame,bd=4,relief=RAISED)
        btn_frame.place(x=10,y=240,width=554,height=43)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",14,"bold"),width=12)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",font=("times new roman",14,"bold"),width=12)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",font=("times new roman",14,"bold"),width=12)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",font=("times new roman",14,"bold"),width=12)
        reset_btn.grid(row=0,column=3)

        #frame for buttons below

        btn_frame1=Frame(studentInformation_frame,bd=4,relief=RAISED)
        btn_frame1.place(x=10,y=284,width=554,height=43)

        take_btn=Button(btn_frame1,text="Take a Photo Sample",font=("times new roman",14,"bold"),width=27)
        take_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame1,text="Update Photo Sample",font=("times new roman",14,"bold"),width=27)
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

        self.student_table=ttk.Treeview(table_frame,column=("enrollment","dep","name","year","sem","mob","email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("enrollment",text="Enrollment")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("mob",text="MobNo")
        self.student_table.heading("email",text="Email")

        self.student_table.column("enrollment",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("mob",width=100)
        self.student_table.column("email",width=100)


        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)


     #Fuctions for various operations
    def add_data(self):
        if self.var_dep.get()=="Select Department":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
            pass    
        

















if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.resizable(False,False)
    root.mainloop()