from tkinter import*
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import mysql.connector

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1380x560+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #======title====
        title = Label(self.root,text="Manage Student Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1500,height=35)

         #=====variables=====
        self.var_stud_id = StringVar()
        self.var_name = StringVar()
        self.var_Email = StringVar()
        self.var_gender = StringVar()
        self.var_doj = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_father_name = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()


        #======widgets======
        #========coloumn 1 ============
        labl_stud_id=Label(self.root,text="Student Id",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        labl_Name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        labl_Email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        labl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        labl_state=Label(self.root,text="State",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        labl_city=Label(self.root,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=310,y=220)
        labl_pin=Label(self.root,text="Pin",font=("goudy old style",15,"bold"),bg="white").place(x=475,y=220)
        labl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=260)


        #=======Entry Fields======
        self.txt_stud_id=Entry(self.root,textvariable=self.var_stud_id,font=("goudy old style",15,"bold"),bg="lightgrey")
        self.txt_stud_id.place(x=150,y=60,width=200)
        txt_Name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightgrey").place(x=150,y=100,width=200)
        txt_Email=Entry(self.root,textvariable=self.var_Email,font=("goudy old style",15,"bold"),bg="lightgrey").place(x=150,y=140,width=200)
        self.txt_Gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_Gender.place(x=150,y=180,width=200)
        self.txt_Gender.current(0)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg="lightgrey").place(x=150,y=220,width=150)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg="lightgrey").place(x=355,y=220,width=100)
        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,"bold"),bg="lightgrey").place(x=530,y=220,width=120)


        #========coloumn 2 ============
        labl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=60)
        labl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=100)
        labl_father_name=Label(self.root,text="Father's Name",font=("goudy old style",15,"bold"),bg="white").place(x=354,y=140)
        labl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=180)

        #=======Entry Fields======
        self.course_list = []
        #function call to update the list
        self.fetch_course()
        
        self.txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15,"bold"),bg="lightgrey")
        self.txt_doj.place(x=480,y=60,width=200)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="lightgrey").place(x=480,y=100,width=200)
        txt_father_name=Entry(self.root,textvariable=self.var_father_name,font=("goudy old style",15,"bold"),bg="lightgrey").place(x=480,y=140,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_course.place(x=480,y=180,width=200)
        self.txt_course.set("select")
        
        #========Text Address===========

        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="lightgrey")
        self.txt_address.place(x=150,y=260,width=500,height=100)


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
        labl__search_studentname=Label(self.root,text="Student Name",font=("goudy old style",15,"bold"),bg="white").place(x=820,y=60)
        txt_search_studentname=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightgrey").place(x=970,y=60,width=180)
        search_button=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=1170,y=60,width=120,height=28)

        #========content========
        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=820,y=100,width=470,height=340)

        scrolly=Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_frame,orient=HORIZONTAL)
        self.studentTable=ttk.Treeview(self.c_frame,columns=("stud_Id","name","email","gender","doj","contact","father's name","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.studentTable.xview)
        scrolly.config(command=self.studentTable.yview)

        for col in ("stud_Id","name","email","gender","doj","contact","father's name","course","state","city","pin","address"):
            self.studentTable.heading(col, text=col.capitalize())
            self.studentTable.column(col, width=100)
        
        self.studentTable["show"] = "headings"
        self.studentTable.pack(fill=BOTH, expand=1)

        self.studentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    # 

    def get_data(self,ev):
        self.txt_stud_id.config(state="readonly")
        r=self.studentTable.focus()
        content = self.studentTable.item(r)
        row = content["values"]
        self.var_stud_id.set(row[0])
        self.var_name.set(row[1])
        self.var_Email.set(row[2])
        self.var_gender.set(row[3])
        self.var_doj.set(row[4])
        self.var_contact.set(row[5])
        self.var_father_name.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END,row[11])


         #  Database Execution Function
    def execute_db(self, query, params):
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


    #add data to database
            
    def add(self):
        try:
            if self.var_stud_id.get() =="":
                messagebox.showerror("Input Error", "Stud_Id should be required!")
                return

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="new_password",
                database="student_management",
                auth_plugin="mysql_native_password"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM student WHERE stud_id=%s", (self.var_stud_id.get(),))
            rows = cursor.fetchone()

            if rows:
                messagebox.showerror("Error", " Stud_Id is already present", parent=self.root)
            else:
                self.execute_db("INSERT INTO student (stud_Id,name,email,gender,doj,contact,father_name,course,state,city,pin,address)  VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                                (self.var_stud_id.get(), self.var_name.get(), self.var_Email.get(),self.var_gender.get(),self.var_doj.get(),self.var_contact.get(),self.var_father_name.get(),self.var_course.get(),self.var_state.get(),self.var_city.get(),self.var_pin.get(), self.txt_address.get("1.0", "end-1c")))
                messagebox.showinfo("Success", "Student added successfully!")
                #self.clear()
                self.root.after(100, self.show)
                self.show()

            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    # delete data


    def delete(self):
        try:
            if self.var_stud_id.get() == "" :
                messagebox.showerror("Input Error", "stud_id is required!")
                return

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="new_password",
                database="student_management",
                auth_plugin="mysql_native_password"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM student WHERE stud_id=%s", (self.var_stud_id.get(),))
            row = cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Select Course from list", parent=self.root)

            else:
                op = messagebox.askyesno("confirm","Do you really want to delete?",parent =self.root)

                if op == True:
                    self.execute_db("Delete from student where stud_id = %s",(self.var_stud_id.get(),))
                    cursor.execute("SELECT COUNT(*) FROM student")
                    messagebox.showinfo("Delete", "Course Deleted successfully!",parent=self.root)
                    self.clear()
                    self.show()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    #update data 
    def update(self):
        try:
            if self.txt_stud_id.get() == "":
                messagebox.showerror("Input Error", "Stud_Id is required!")
                return

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="new_password",
                database="student_management",
                auth_plugin="mysql_native_password"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM student WHERE stud_id=%s", (self.var_stud_id.get(),))
            row = cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Select Course from list", parent=self.root)
            else:
                self.execute_db("update student set  name = %s , email = %s, gender = %s, doj = %s, contact = %s, father_name = %s, course = %s, state = %s, city =%s, pin = %s, address = %s where stud_id = %s", 
                                (self.var_name.get(), self.var_Email.get(), self.var_gender.get(),self.var_doj.get(),self.var_contact.get(),self.var_father_name.get(),self.var_course.get(),self.var_state.get(),self.var_city.get(),self.var_pin.get(),self.txt_address.get("1.0","end-1c").strip(),self.var_stud_id.get()))
                messagebox.showinfo("Success", "Course update successfully!")
                self.show()
                self.clear()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # clear the field
          
    def clear(self):
        self.show()
        self.var_stud_id.set("")
        self.var_name.set("")
        self.var_Email.set("")
        self.var_gender.set("")
        self.var_doj.set("")
        self.var_contact.set("")
        self.var_father_name.set("")
        self.var_course.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0", END)
        self.txt_stud_id.config(state=NORMAL)
      
        # search data

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

            cursor.execute("SELECT * FROM student WHERE stud_id LIKE %s OR name LIKE %s",("%" + self.var_search.get() + "%", "%" + self.var_search.get() + "%"))

            rows = cursor.fetchall()

            if rows!=None:

                self.studentTable.delete(*self.studentTable.get_children())
                for row in rows:
                    self.studentTable.insert("",END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


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

            cursor.execute("SELECT * FROM student")
            rows = cursor.fetchall()
            self.studentTable.delete(*self.studentTable.get_children())
            #cursor.execute("ALTER TABLE students AUTO_INCREMENT = 1")

            for row in rows:
                self.studentTable.insert("",END,values=row)
                conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def fetch_course(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="new_password",
                database="student_management",
                auth_plugin="mysql_native_password"
                )
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM courses")
            rows = cursor.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])
                conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")























if __name__=="__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
