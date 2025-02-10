from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import mysql.connector
class Result:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #======title====
        title = Label(self.root,text="Add Student Result",font=("goudy old style",20,"bold"),bg="orange",fg="#262626",justify=CENTER).place(x=10,y=15,width=1500,height=50)
        #  variables

        self.stud_id = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks_obtained = StringVar()
        self.var_full_marks = StringVar()
        self.stud_id_list = []
        self.fetch_student()

        #======widgets======
        labl_select=Label(self.root,text="Select Student",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=100)
        labl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=160)
        labl_Course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=220)
        labl_marksObtained=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=280)
        labl_fullMarks=Label(self.root,text="Total Marks",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=340)

        # searching feature

        self.txt_student=ttk.Combobox(self.root,textvariable=self.stud_id,values=self.stud_id_list,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("select")
        search_button=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=500,y=100,width=100,height=28)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg="lightgrey",state="readonly").place(x=280,y=160,width=320)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg="lightgrey").place(x=280,y=220,width=320)
        txt_marks=Entry(self.root,textvariable=self.var_marks_obtained,font=("goudy old style",20,"bold"),bg="lightgrey").place(x=280,y=280,width=320)
        txt_fullmarks=Entry(self.root,textvariable=self.var_full_marks,font=("goudy old style",20,"bold"),bg="lightgrey").place(x=280,y=340,width=320)

        # buttons
        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="clear",font=("times new roman",15),bg="lightgray",activebackground="lightgrey",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)
        # image
        self.bgimage = Image.open("image/image1.jpg")
        self.bgimage = self.bgimage.resize((500,300))
        self.bgimage = ImageTk.PhotoImage(self.bgimage)

        self.lbl_bg =  Label(self.root,image=self.bgimage).place(x=650,y=100)
    


    #  Database Execution Function
    def execute_db(self, query, params=()):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="new_password",
                database="student_management",
                auth_plugin="mysql_native_password"
            )
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()
            cur.close()
            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")
    
    # clear
    
    def clear(self):
        self.stud_id.set("select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks_obtained.set("")
        self.var_full_marks.set("")

    #  Add Result

    def add(self):
        try:
            if self.stud_id.get() == "" or self.var_name.get() == "" :
                messagebox.showerror("Input Error", "student details are required!")
                return

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="new_password",
                database="student_management",
                auth_plugin="mysql_native_password"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Result WHERE stud_id=%s or name=%s or course=%s ", (self.stud_id.get(),self.var_name.get(),self.var_course.get()))
            rows = cursor.fetchone()

            if rows:
                messagebox.showerror("Error", "Result already present", parent=self.root)
            else:
                percentage = (int(self.var_marks_obtained.get())*100)/(int(self.var_full_marks.get()))

                self.execute_db("INSERT INTO Result (stud_id, name, course, marks_obtained, full_marks, percentage) VALUES (%s, %s, %s, %s,%s,%s)", 
                                (self.stud_id.get(), self.var_name.get(), self.var_course.get(), self.var_marks_obtained.get(),self.var_full_marks.get(),str(percentage)))
                messagebox.showinfo("Success", "Result added successfully!")
                self.clear()

            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    
    # search

    def search(self):
        try:
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="new_password",
                    database="student_management",
                    auth_plugin="mysql_native_password"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM student WHERE stud_id LIKE %s",("%" + self.stud_id.get() + "%",))

            rows = cursor.fetchone()

            if rows!=None:
                self.var_name.set(rows[0])

            else:
                messagebox.showerror("Error","No record found",parent=self.root)
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    # fetch student

    def fetch_student(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="new_password",
                database="student_management",
                auth_plugin="mysql_native_password"
                )
            cursor = conn.cursor()

            cursor.execute("SELECT stud_id FROM student")
            rows = cursor.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.stud_id_list.append(row[0])
                conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")





if __name__=="__main__":
    root = Tk()
    obj = Result(root)
    root.mainloop()
    