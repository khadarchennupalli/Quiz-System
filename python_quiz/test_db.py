import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",          
        password="khadar@2001",  
        database="quiz"
    )

try:
    db = connect_db()
    print("Connection successful!")
    db.close()
except Exception as e:
    print("Connection failed:", e)
