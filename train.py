from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from tkinter import messagebox
import os
import numpy as np
import cv2

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Train Data")

        #backgroundImage
        img=Image.open(r"raw/test2.jpg")
        img=img.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1920,height=1080)

         #first Label
        title_lbl=Label(f_lbl,text="Train the Data Model",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lbl.place(x=0,y=45,width=1920,height=55)


        #imageButton1
        img1=Image.open(r"raw/train.png")
        img1=img1.resize((250,250),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        b1=Button(f_lbl,image=self.photoimg1,command=self.train_classifier,cursor="hand2")
        b1.place(x=860,y=350,width=250,height=250)
        #realButton
        b1_1=Button(f_lbl,text="Train",command=self.train_classifier,cursor="hand2")
        b1_1.place(x=860,y=600,width=250,height=30)



    #training fuction
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #greyscale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #now training the classier fr this time :|
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classsifier.xml")
        messagebox.showinfo("info","Training DataSets completed!")
        cv2.destroyAllWindows()







if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    #root.resizable(False,False)
    root.mainloop()