from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from tkinter import messagebox
from time import strftime
from datetime import datetime
import os
import sqlite3
import numpy as np
import cv2

class Face_recognition:
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
        title_lbl=Label(f_lbl,text="Facial Recognition System",font=("times new roman",35,"bold"),fg="white",bg="black")
        title_lbl.place(x=0,y=45,width=1366,height=55)


        #imageButton1
        img1=Image.open(r"raw/facial-recognition2.png")
        img1=img1.resize((150,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        b1=Button(f_lbl,image=self.photoimg1,command=self.face_recog,cursor="hand2")
        b1.place(x=600,y=300,width=150,height=150)
        #realButton
        b1_1=Button(f_lbl,text="Start",command=self.face_recog,cursor="hand2")
        b1_1.place(x=600,y=450,width=150,height=30)




    #function for facerecog
    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbours,color,text,clf): #check here once
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

                coord=[]

                for (x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+y,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))

                    conn=sqlite3.connect('classifier_db.db')
                    my_cursor=conn.cursor()


                    my_cursor.execute("select enroll from student_details where enroll="+str(id))
                    e=my_cursor.fetchone()
                    e="+".join(e)

                    my_cursor.execute("select name from student_details where enroll="+str(id))
                    n=my_cursor.fetchone()
                    n="+".join(n)

                    my_cursor.execute("select dep from student_details where enroll="+str(id))
                    r=my_cursor.fetchone()
                    r="+".join(r)


                    
                    if confidence>83:
                        cv2.putText(img,f"ENo:{e}",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                        cv2.putText(img,f"Name:{n}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                        cv2.putText(img,f"Dep:{r}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)

                        self.mark_attendance(e,n,r)

                    else:
                        cv2.rectangle(img,(x,y),(x+y,y+w),(0,0,255),3)
                        cv2.putText(img,"unknown",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0))

                    coord=[x,y,w,h]

                return coord
        def recognize(img,clf,faceCascade):
            coord=[draw_boundry(img,faceCascade,1.1,10,(255,25,255),"face",clf)]
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classsifier.xml")


        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome",img)

            if cv2.waitKey(1)==13:
                
                video_cap.release()
                cv2.destroyAllWindows()
                break




    #marking attendance
    def mark_attendance(self,e,n,r):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            
            if((e not in name_list) and (n not in name_list) and (r not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{e},{n},{r},{dtString},{d1},Present")



        
if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.resizable(False,False)
    root.mainloop()