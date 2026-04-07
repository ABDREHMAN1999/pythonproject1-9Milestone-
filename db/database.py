import os 
import sqlite3

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "Data", "pdf.db"))

def connect():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = connect()
    cursor  = conn.cursor()
    
    ## Data base Schema
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS docuemts (
                       id INTEGER PRIMARY KEY, 
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
    
    #print("db operation successful")
    #print("Generated ID:", cursor.lastrowid)
    
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS page_visits (
                    id INTEGER PRIMARY KEY,
                    document_id INTEGER,
                    page_number INTEGER, 
                    time_stamp TEXT   
                )
                   
                   
                   
                   """)
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS analytics(
                    button_label TEXT,
                    time_stamp TEXT
                )""")
    conn.commit()
    conn.close()
    