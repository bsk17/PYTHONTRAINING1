import pymysql

conn = pymysql.connect(host="localhost", user="root", password="password", database="pythonbhilai")
mycursor = conn.cursor()

sql = "create table STUDENTS(name varchar(30), email varchar(30) primary key, password varchar(10))"
mycursor.execute(sql)

conn.commit()
conn.close()
