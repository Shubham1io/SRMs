from tkinter import*
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import mysql.connector

class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1380x560+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #======title====
        title = Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1500,height=35)

        #=====variables=====
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        #======widgets======
        labl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        labl_Duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        labl_Charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        labl_Description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)

        #=======Entry Fields======
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightgrey")
        self.txt_courseName.place(x=150,y=60,width=200)
        txt_Duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="lightgrey").place(x=150,y=100,width=200)
        txt_Charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,"bold"),bg="lightgrey").place(x=150,y=140,width=200)
        self.txt_Description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightgrey")
        self.txt_Description.place(x=150,y=180,width=500,height=150)

        #=======Buttons======
        self.add_button=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.add_button.place(x=150,y=400,width=110,height=40)
        self.add_button=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.add_button.place(x=270,y=400,width=110,height=40)
        self.add_button=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.add_button.place(x=390,y=400,width=110,height=40)
        self.add_button=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.add_button.place(x=510,y=400,width=110,height=40)

        #====== search pannel ===========
        self.var_search=StringVar()
        labl__search_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=820,y=60)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightgrey").place(x=970,y=60,width=180)
        search_button=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=1170,y=60,width=120,height=28)

        #========content========
        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=820,y=100,width=470,height=340)

        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)
        self.courseTable=ttk.Treeview(self.c_frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)

        for col in ("cid", "name", "duration", "charges", "description"):
            self.courseTable.heading(col, text=col.capitalize())
            self.courseTable.column(col, width=100)
        
        self.courseTable["show"] = "headings"
        self.courseTable.pack(fill=BOTH, expand=1)

        self.courseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    # clear data

    def clear(self):
        self.show()
        self.var_search.set("")
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.txt_Description.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)


    def get_data(self,ev):
        self.txt_courseName.config(state="readonly")
        r=self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_Description.delete('1.0',END)
        self.txt_Description.insert(END,row[4])

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

        # adding data into database frame


    def add(self):
        try:
            if self.var_course.get() == "" or self.var_duration.get() == "" or self.var_charges.get() == "" or self.txt_Description.get("1.0", END).strip() == "":
                messagebox.showerror("Input Error", "All fields are required!")
                return

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="new_password",
                database="student_management",
                auth_plugin="mysql_native_password"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM courses WHERE name=%s", (self.var_course.get(),))
            rows = cursor.fetchone()

            if rows:
                messagebox.showerror("Error", "Course Name already present", parent=self.root)
            else:
                self.execute_db("INSERT INTO courses (name, duration, charges, description) VALUES (%s, %s, %s, %s)", 
                                (self.var_course.get(), self.var_duration.get(), self.var_charges.get(), self.txt_Description.get("1.0", END).strip()))
                messagebox.showinfo("Success", "Course added successfully!")
                self.clear()
                self.root.after(100, self.show)
                self.show()

            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # updating values

    def update(self):
        try:
            if self.var_course.get() == "" or self.var_duration.get() == "" or self.var_charges.get() == "" or self.txt_Description.get("1.0", END).strip() == "":
                messagebox.showerror("Input Error", "All fields are required!")
                return

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="new_password",
                database="student_management",
                auth_plugin="mysql_native_password"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM courses WHERE name=%s", (self.var_course.get(),))
            row = cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Select Course from list", parent=self.root)
            else:
                self.execute_db("update courses set  duration = %s , charges = %s, description = %s where name = %s", 
                                (self.var_duration.get(), self.var_charges.get(), self.txt_Description.get("1.0", END).strip(),self.var_course.get()))
                messagebox.showinfo("Success", "Course update successfully!")
                self.show()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # delete data

    def delete(self):
        try:
            if self.var_course.get() == "" or self.var_duration.get() == "" or self.var_charges.get() == "" or self.txt_Description.get("1.0", END).strip() == "":
                messagebox.showerror("Input Error", "All fields are required!")
                return

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="new_password",
                database="student_management",
                auth_plugin="mysql_native_password"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM courses WHERE name=%s", (self.var_course.get(),))
            row = cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Select Course from list", parent=self.root)

            else:
                op = messagebox.askyesno("confirm","Do you really want to delete?",parent =self.root)

                if op == True:
                    self.execute_db("Delete from courses where name = %s",(self.var_course.get(),))
                    cursor.execute("SELECT COUNT(*) FROM courses")
                    messagebox.showinfo("Delete", "Course Deleted successfully!",parent=self.root)
                    self.clear()
                    self.show()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


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

            cursor.execute("SELECT * FROM courses where name Like %s",("%" + self.var_search.get() + "%",))
            rows = cursor.fetchall()

            self.courseTable.delete(*self.courseTable.get_children())

            for row in rows:
                self.courseTable.insert("",END,values=row)
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


        # showing data into 

    def show(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="new_password",
                database="student_management",
                auth_plugin="mysql_native_password"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM courses")
            rows = cursor.fetchall()

            self.courseTable.delete(*self.courseTable.get_children())
            #cursor.execute("ALTER TABLE courses AUTO_INCREMENT = 1")

            for row in rows:
                self.courseTable.insert("",END,values=row)
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__=="__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
