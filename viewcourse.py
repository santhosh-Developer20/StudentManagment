from tabulate import tabulate
from config.db_config import db
class Viewcourse():
    def __init__(self):
        self.viewingcourse()
        self.cos={}
    def viewingcourse(self):
        mycursor=db.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM course")

        myresult = mycursor.fetchall()
        ci=[]
        co=[]
        cc=[]

        for x in myresult:
            ci.append(x["Course_ID"])
            co.append(x["Course_code"])
            cc.append(x["Course_name"])
            self.cos={
               "Course_ID":ci,
               "Course_code":co,
               "Course_name":cc
            }
        self.tab()
    def tab(self):
        print(tabulate(self.cos,headers="keys", tablefmt="fancy_grid"))
