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
        print("Generated ID:", cursor.lastrowid)
        connection.commit()
        connection.close()  
    def search_documents(self, tags= None, date=None):
        connection = connect()
        cursor = connection.cursor()
        query = "SELECT * FROM docuemts WHERE 1 = 1"
        params = []
        
        if tags:
            query+= " AND tag LIKE ?"
            params.append(f"%{tags}%")
        if date:
            query += " AND lecture_date = ?"
            params.append(str(date))
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        connection.close()
        return rows
    