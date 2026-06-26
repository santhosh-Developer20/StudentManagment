import mysql.connector



db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="20052009"

)
mycursor = db.cursor()

mycursor.execute("CREATE DATABASE studentrecords")