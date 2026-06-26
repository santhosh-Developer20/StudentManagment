from tabulate import tabulate
from config.db_config import db
class Viewstudent():
    def __init__(self):
        self.viewingStudent()
        self.data={}
    def viewingStudent(self):
        mycursor=db.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM students")

        myresult = mycursor.fetchall()
      
   
        std=[]
        nam=[]
        Dob=[]
        Gen=[]
        Ema=[]
        Pho=[]
        Dep=[]
        Ad=[]

        for x in myresult:
            #print(x["Student_ID"])
            std.append(x["Student_ID"])
            nam.append(x["Name"])
            Dob.append(x["DOB"].strftime("%d-%m-%Y"))
            Gen.append(x["Gender"])
            Ema.append(x["Email"])
            Pho.append(x["Phone"])
            Dep.append(x["Department"])
            Ad.append(x["Admission_year"])
            self.data={
                "Student_ID":std,
                "Name":nam,
                "DOB":Dob,
                "Gender":Gen,
                "Email":Ema,
                "Phone":Pho,
                "Department":Dep,
                "Admission_year":Ad
            }
        self.tabl()
        
    def tabl(self):
        print(tabulate(self.data,headers="keys", tablefmt="fancy_grid"))
