from config.db_config import db

from tabulate import tabulate
from datetime import datetime
class Addstudent:
      def __init__(self,length):
            for i in range(length):
                  self.getstudentinput()
                  self.dbinsert()
                  self.studid()
            
      def getstudentinput(self):
       
            print("""=======================================
          ENTER STUDENT DETAILS           
=======================================""")   
            self.a=input("Enter the Student Name:").upper()
            while True:
                  a=input("Enter your Birth Year(YYYY): ")
                  b=input("Enter your Birth Month(MM): ")
                  c=input("Enter your Birth Day(DD): ")
                  self.b=f"{a}-{b}-{c}"
                  if len(a) == 4 and len(b) == 2 and len(c) == 2 and a.isdigit() and b.isdigit() and c.isdigit():
                      break
                  else:
                     print("invalid")
            self.c=input("Enter your Gender:").upper()
            while True:
                  self.d=input("Enter the Email Address:").strip().lower()
                  if "@" in self.d and "." in self.d.split("@")[-1]:
                   break 
                  else:
                        print("Invalid")
            while True:
                  self.e = input("Enter Contact Number: ").strip()
                  if self.e.isdigit() and len(self.e) == 10:
                     break
                  else:
                      print("Invalid")
            self.f=input("Enter the Department:").upper()
            while True:
               self.g=input("Enter the Admission Year:")
               if len(self.g) == 4 and  self.g.isdigit() and int(self.g)<=2026 :
                  break
               else:
                  print("Invalid")
      def dbinsert(self):
            mycursor=db.cursor()
            sql = "INSERT INTO students(Name,DOB,Gender,Email,Phone,Department,Admission_year) VALUES ( %s,%s,%s,%s,%s,%s,%s)"
            val = (self.a,self.b,self.c,self.d,self.e,self.f,self.g)
            mycursor.execute(sql, val)
            self.id = mycursor._last_insert_id
         

            db.cursor().close()
            db.commit()
            
            print(mycursor.rowcount, "    record inserted ")
      def studid(self):
            mycursor=db.cursor()
            sql = "SELECT Course_ID, Course_name FROM course"
      
            mycursor.execute(sql)
            myresult=mycursor.fetchall()
            # myresult=[(1, 'computer science'), (2, 'mechanical'), (3, 'computer'), (4, 'computer'), (5, 'computer science'), (6, 'COMPUTER SCIENCE')]
            self.sid= myresult
            studentSelected=[]
            print("""=================================
        AVAILABLE COURSES
=================================""")

            for i, row in enumerate(myresult, start=1):
                  print(f"{i}:{row[1]}")    
            while True: 
                  self.c=int(input("Enter your Choice for Enroll Course:"))
                  if self.c<=10:
                        for s in (self.sid):
                              if s[0]==self.c:
                                    studentSelected.append((self.id,self.c))
                              
                        mycursor.close()
                        self.enrollments(self.id,self.c)
                        break

                  else:
                        print("Invalid choice Try Again")

      def enrollments(self,studentID,courseID):

            date = datetime.now().strftime('%Y-%m-%d')
            
            mycursor=db.cursor()
            sql = "INSERT INTO enrollments(Student_ID,Course_ID,Enrollment_Date) VALUES (%s,%s,%s)"
            val = (studentID,courseID,date)
            mycursor.execute(sql, val)
            print(f"{self.a} YOUR COURSE IS ENROLLED ")
            
           
            db.commit()
            db.cursor().close()


