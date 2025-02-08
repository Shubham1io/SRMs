from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from course import CourseClass #importing CourseClass
from student import Student #importing student class
class Result:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #======title====
        title = Label(self.root,text="Add Student Result",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1500,height=50)


        #======widgets======
        labl_select=Label(self.root,text="Select Student",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=100)
        labl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=160)
        labl_Course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=220)
        labl_marksObtained=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=280)
        labl_fullMarks=Label(self.root,text="Full Marks",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=340)



if __name__=="__main__":
    root = Tk()
    obj = Result(root)
    root.mainloop()
    