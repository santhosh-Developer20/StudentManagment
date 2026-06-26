import mysql.connector




db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="20052009",
    database="studentrecords"

)
mycursor=db.cursor()
mycursor.execute("""create table course(
        Course_ID INT PRIMARY KEY AUTO_INCREMENT,
        Course_code char(6),
        Course_name varchar(100)
        )""")