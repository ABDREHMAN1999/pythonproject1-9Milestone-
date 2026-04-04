##upload pdf functionality
## from uploaded file -->file , tags , description , lecture date 
## from uploaded file -->thumbnail 
## from uploaded file -->folder to store the images 
## from uploaded file -->total pages 
## from uploaded file -->lecture date 
## from uploaded file --> upload date, time 
import os 
from datetime import datetime



from db.repository import DocumentRepository
from core.filemanager import FileManager
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))





class DocumentService:
    def __init__(self):
        self.repo = DocumentRepository()
        self.file = FileManager()

    
    def upload_document(self, uploaded_file, tags, description, lecture_date = None):
        doc = []
        ## save file 
        file_path = self.file.save_file(uploaded_file)

        ## generate thumbnails 
        thumb_nail_path = self.file.generate_thumnail(file_path)
        
        ## get total pages 
        total_pages = self.file.get_total_pages(file_path)
        ## convert to images 
        self.file.convert_to_images(file_path)
        ## create required variables 
        upload_date = datetime.now().strftime("%d%m%Y")
        doc = [uploaded_file.name,file_path,thumb_nail_path, tags, description, upload_date, lecture_date , total_pages]
        ## save to db
        self.repo.add_document(doc)
    
    def search_doc(self , tags , date):
        rows = self.repo.search_documents(tags=tags, date=date)
        return rows 
        
        