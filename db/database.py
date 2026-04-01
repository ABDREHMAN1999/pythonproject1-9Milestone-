import os 
import sqlite3


DB_PATH = os.path.join("Data", "pdf.db")

def connect():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = connect()
    cursor  = conn.cursor()
    
    ## Data base Schema
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTs docuemts (
                       id INTEGER PRIMATY KEY AUTOINCREAMENT, 
                       name TEXT, 
                       path TEXT, 
                       thumnail_path TEXT,
                       tag TEXT,
                       description TEXT, 
                       upload_date TEXT, 
                       lecture_date TEXT, 
                       total_pages INTEGER
                   )
                   """)
    
    conn.commit()
    print("db operation successful")
    conn.close()
    