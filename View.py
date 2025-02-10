from tkinter import*
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import mysql.connector

class View:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #======title====
        title = Label(self.root,text="View Student Result",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1500,height=50)


        # Searching feature............


        self.var_search = StringVar()
        self.var_rid = ""

        labl__search=Label(self.root,text="Search by Stud_id",font=("goudy old style",20,"bold"),bg="white").place(x=300,y=100)
        txt_search_stud_id=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20,"bold"),bg="lightgrey").place(x=520,y=100,width=150)
        search_button=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=680,y=100,width=100,height=35)
        btn_clear=Button(self.root,text="clear",font=("times new roman",15),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=800,y=100,width=120,height=35)

        # result labels

        labl_stud_id=Label(self.root,text="Student Id",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        labl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        labl_Course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        labl_marksObtained=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        labl_fullMarks=Label(self.root,text="Total Marks",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        labl_percentage=Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)


        self.stud_id=Label(self.root,text="",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.stud_id.place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root,text="",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.Course=Label(self.root,text="",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.Course.place(x=450,y=280,width=150,height=50)
        self.marksObtained=Label(self.root,text="",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marksObtained.place(x=600,y=280,width=150,height=50)
        self.fullMarks=Label(self.root,text="",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.fullMarks.place(x=750,y=280,width=150,height=50)
        self.percentage=Label(self.root,text="",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.percentage.place(x=900,y=280,width=150,height=50)


        # delete button

        btn_delete=Button(self.root,text="Delete",font=("times new roman",15),bg="Red",fg="white",cursor="hand2",command=self.delete).place(x=500,y=350,width=150,height=35)



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

            if self.var_search.get()=="":
                messagebox.showerror("Error","search field is required",parent=self.root)
            else:
                cursor.execute("SELECT * FROM Result WHERE stud_id LIKE %s",( self.var_search.get(),))
                rows = cursor.fetchone()
                if rows!=None:
                    self.var_rid = rows[0]
                    self.stud_id.config(text=rows[1])
                    self.name.config(text=rows[2])
                    self.Course.config(text=rows[3])
                    self.marksObtained.config(text=rows[4])
                    self.fullMarks.config(text=rows[5])
                    self.percentage.config(text=rows[6])
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def clear(self):
        self.var_rid = ""
        self.stud_id.config(text="")
        self.name.config(text="")
        self.Course.config(text="")
        self.marksObtained.config(text="")
        self.fullMarks.config(text="")
        self.percentage.config(text="")
        self.var_search.set("")


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

        
    # delete 

    def delete(self):
        try:
            if self.var_rid == "" :
                messagebox.showerror("Input Error", "Search Student Result First!")
                return

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="new_password",
                database="student_management",
                auth_plugin="mysql_native_password"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Result WHERE Rid=%s", (self.var_rid,))
            row = cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid Student Result", parent=self.root)

            else:
                op = messagebox.askyesno("confirm","Do you really want to delete?",parent =self.root)

                if op == True:
                    self.execute_db("Delete from Result where Rid = %s",(self.var_rid,))
                    cursor.execute("SELECT COUNT(*) FROM student")
                    messagebox.showinfo("Delete", "Result Deleted successfully!",parent=self.root)
                    self.clear()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    


if __name__=="__main__":
    root = Tk()
    obj = View(root)
    root.mainloop()
    