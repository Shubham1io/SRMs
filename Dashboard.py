from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from course import CourseClass #importing CourseClass
from student import Student #importing student class
from Result import Result #importing Result class
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1530x780+0+0")
        self.root.config(bg="white")
        #-----images-----
        self.logo_dash = ImageTk.PhotoImage(file="image/ezgif-68d89e630deaf.png")
        #======title====
        title = Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)        #-----Menu---- 
        mFrame = LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="lightgrey")
        mFrame.place(x=10,y=70,width="1520",height=80)
        #----button-----
        btn_course = Button(mFrame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=80,y=5,width=200,height=40)
        btn_student = Button(mFrame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=300,y=5,width=200,height=40)
        btn_result = Button(mFrame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=520,y=5,width=200,height=40)
        btn_view_students_details = Button(mFrame,text="View student Results",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=740,y=5,width=200,height=40)
        btn_exit = Button(mFrame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1400,y=5,width=100,height=40)
        #=====content window====
        self.bgimage = Image.open("image/image.png")
        self.bgimage = self.bgimage.resize((920,400))
        self.bgimage = ImageTk.PhotoImage(self.bgimage)

        self.lbl_bg =  Label(self.root,image=self.bgimage).place(x=600,y=180,width=920,height=400)
        
        #======title====
        footer = Label(self.root,text="SRMS-Student Result Management System\nContact Us for any Technical Issue:999xxxxx01",font=("goudy old style",12,"bold"),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

        #====updates details====

        self.lbl_course = Label(self.root,text="Total Courses\n[ 0 ]" ,font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=600,y=545,width=300,height=100)

        self.lbl_Student = Label(self.root,text="Total Students\n[ 0 ]" ,font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_Student.place(x=910,y=545,width=300,height=100)

        self.lbl_Result = Label(self.root,text="Total Results\n[ 0 ]" ,font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_Result.place(x=1220,y=545,width=300,height=100)

    def add_course(self):
        self.new_wind = Toplevel(self.root)
        self.new_obj=CourseClass(self.new_wind)


    def add_student(self):
        self.new_wind = Toplevel(self.root)
        self.new_obj=Student(self.new_wind)


    def add_result(self):
        self.new_wind = Toplevel(self.root)
        self.new_obj = Result(self.new_wind)     
    









        
if __name__=="__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
    