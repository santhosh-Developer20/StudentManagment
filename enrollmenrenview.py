
from tabulate import tabulate
from config.db_config import db
class Viewenroll():
    def __init__(self):
        self.viewingenroll()
        self.eno={}
    def viewingenroll(self):
        mycursor=db.cursor(dictionary=True)
            
        sql="""SELECT 
            students.Name AS name,
            course.Course_name AS course,
            enrollments.Enrollment_Date AS enroll
        FROM enrollments
        INNER JOIN students ON enrollments.Student_ID = students.Student_ID
        INNER JOIN course ON enrollments.Course_ID = course.Course_ID
        """
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        stu=[]
        cou=[]
        dat=[]

        for x in myresult:
            stu.append(x["name"])
            cou.append(x["course"])
            dat.append(x["enroll"].strftime("%d-%m-%Y"))
            self.eno={
               "Students Name":stu,
               "Course Name":cou,
               "Enrollment Date":dat
            }
        self.tab()
    def tab(self):
        print(tabulate(self.eno,headers="keys", tablefmt="fancy_grid"))