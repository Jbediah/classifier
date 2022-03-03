from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student


class Home:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x800+0+0")
        self.root.title("Classifier")

        #backgroundImage
        img=Image.open(r"/home/jbediah/Documents/classifier/raw/test2.jpg")
        img=img.resize((1366,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=800)

         #first Label
        title_lbl=Label(f_lbl,text="The Desired Heading",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lbl.place(x=0,y=45,width=1366,height=55)

        #imageButton1
        img1=Image.open(r"/home/jbediah/Documents/classifier/raw/details.png")
        img1=img1.resize((150,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        b1=Button(f_lbl,image=self.photoimg1,command=self.student_page,cursor="hand2")
        b1.place(x=600,y=250,width=150,height=150)
        #realButton
        b1_1=Button(f_lbl,text="Student Details",command=self.student_page,cursor="hand2")
        b1_1.place(x=600,y=400,width=150,height=30)


 ##Function to open a new window
    def student_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
















if __name__=="__main__":
    root=Tk()
    obj=Home(root)
    root.resizable(False,False)
    root.mainloop()