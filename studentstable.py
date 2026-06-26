import mysql.connector




db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="20052009",
    database="studentrecords"

)


mycursor=db.cursor()
mycursor.execute("""CREATE TABLE Students (
        Student_ID INT PRIMARY KEY AUTO_INCREMENT,
        Name VARCHAR(100)NOT NULL,
        DOB DATE NOT NULL,
        Gender VARCHAR(10) NOT NULL,
        Email VARCHAR(100),
        Phone VARCHAR(15) NOT NULL,
        Department VARCHAR(50),
        Admission_year YEAR
        )""")
