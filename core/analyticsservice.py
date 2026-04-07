from db.database import connect
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
        

    