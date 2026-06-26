import mysql.connector




db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="20052009",
    database="studentrecords"

)
mycursor=db.cursor()
mycursor.execute("""CREATE TABLE enrollments (
    Enrollment_ID INT PRIMARY KEY AUTO_INCREMENT,
    Student_ID INT,
    Course_ID INT,
    Enrollment_Date DATE,
    Status VARCHAR(20),
    FOREIGN KEY (Student_ID) REFERENCES students(Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES course(Course_ID))""")