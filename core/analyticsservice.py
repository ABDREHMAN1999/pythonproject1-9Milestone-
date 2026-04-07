from db.database import connect, init_db
import datetime




class AnalyticsService:
    
    def update_analytics(self,document_id:int, page_number:int, time_stamp:str):
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
                       INSERT INTO page_visits
                       (document_id , page_number, time_stamp)
                       VALUES(?,?,?)
                       """, (document_id, page_number, time_stamp))
        connection.commit()
        connection.close()
        
    def get_unique_pages(self, doc_id:int):
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT COUNT(DISTINCT page_number) FROM page_visits   
            WHERE document_id = ?    
                       
                       """,(doc_id,))
        result = cursor.fetchone()
        result = result[0]
        connection.close()
        if result:
            return result
        else:
            return 0
        
    def update_analytics_table(self,button_label:str):
        time_stamp = datetime.datetime.now().isoformat()
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
                INSERT INTO analytics
                (button_label, time_stamp)
                VALUES (?,?)""",(button_label,time_stamp))
        connection.commit()
        connection.close()
        print("analytics table updated")
    
    def get_analytics_data(self):
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
                SELECT button_label , COUNT(DISTINCT time_stamp) FROM analytics
                GROUP BY button_label
                       """)
        data = cursor.fetchall()
        connection.close()
        return data
    
    def update_doc_status(self,doc_id:int, name: str , status:float):
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
                  INSERT INTO doc_completion
                  (doc_id, name, status)
                  VALUES (?,?,?)
                  
                       
                       
                       """,(doc_id,name,status))
        connection.commit()
        connection.close()
    
    def get_doc_status(self):
        init_db()
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT doc_id , name, MAX(status) FROM doc_completion GROUP BY doc_id , name
                       
                       
                       
                       """)
        doc_data = cursor.fetchall()
        connection.close()
        return doc_data
        

    