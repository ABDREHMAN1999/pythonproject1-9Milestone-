from db.database import connect


class DocumentRepository:
    
    def add_document(self,doc:list): 
        connection = connect()
        cursor = connection.cursor()
        print("inserting document in database")
        cursor.execute("""
                       INSERT INTO docuemts(
                           name , path , thumnail_path , tag , description , upload_date, lecture_date , total_pages
                       )values(?,?,?,?,?,?,?,?)
                       """,(doc[0],doc[1],doc[2],doc[3],doc[4],doc[5],doc[6], doc[7]))
        connection.commit()
        connection.close()
    