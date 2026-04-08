from db.database import connect


class clearDatabase:
    
    def cleardatabase(self):
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
        connection.close()
        return password
        
        