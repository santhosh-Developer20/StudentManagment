from config.db_config import db
class Addcourse():
    def __init__(self,length):
        for i in range(length):
            self.getcourseinput()
            self.dbinsert()
    def getcourseinput(self):
        print("""==============================
     ENTER COURSE DETAILS
==============================""")
        import random
        
        self.b = input("Enter the Course Name:").upper()
        x=self.b[:2].upper()
        self.a = f"{x}{random.randint(1000,9999)}"
    def dbinsert(self):
            mycursor=db.cursor()
            sql = "INSERT INTO course(Course_code,Course_name) VALUES ( %s,%s)"
            val = (self.a,self.b)
            mycursor.execute(sql, val)
            id = mycursor._last_insert_id
            db.cursor().close()
            db.commit()
            
            print(mycursor.rowcount, "record inserted ")
