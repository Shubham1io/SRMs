import mysql.connector

def execute_db():
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "new_password",
            database = "student_management",
            auth_plugin="mysql_native_password"
        )
        print(conn)
        cur = conn.cursor()
        print(cur)
        cur.execute("show databases")
        for x in cur:
                print(x)
execute_db()
print("hellow world")