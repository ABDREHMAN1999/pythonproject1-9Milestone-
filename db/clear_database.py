from db.database import connect
import os 
import sys
import shutil
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)


class clearDatabase:
    def cleardatabase(self):
        storage_path_pdf = os.path.join(base_dir, "storage", "pdf's")
        for item in os.listdir(storage_path_pdf):
            path = os.path.join(storage_path_pdf,item)
            if item.endswith(".pdf"):
                os.remove(path)
            else:
                shutil.rmtree(path)
        storage_path_thumnails = os.path.join(base_dir,"Storage", "thumnails")
        for item in os.listdir(storage_path_thumnails):
            path = os.path.join(storage_path_thumnails,item)
            os.remove(path)
        
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
                      DELETE FROM docuemts
                      WHERE 1 = 1
                       """)
        cursor.execute("""
                      DELETE FROM page_visits
                      WHERE 1 = 1
                       """)
        
        cursor.execute("""
                      DELETE FROM analytics
                      WHERE 1 = 1
                       """)
        connection.commit()
        connection.close()
        
    
        print("Data base cleared")
        
    def update_db_password(self,password:str):
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
                       UPDATE db_password
                       SET password = ?
                       WHERE 1 = 1
                       """,(password,))
        connection.commit()
        connection.close()
        print("Password updated")
    
    def check_db_password(self):
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
                    SELECT password FROM db_password
                    WHERE 1 = 1  
                       """)
        password = cursor.fetchall()
        password = password[0][0]
        connection.close()
        return password
        
        