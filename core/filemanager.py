from datetime import datetime
import os 
import fitz
import pymupdf
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class FileManager:
    def save_file(self,uploaded_file):
        timestamp = datetime.now().strftime("%d%m%Y%H%M%S")
        file_name = f"{timestamp}_{uploaded_file.name}"
        file_path = os.path.join(BASE_DIR,"storage", "pdf's", file_name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        return file_path
    
    def generate_thumnail(self,file_path):
        doc = fitz.open(file_path)
        page = doc.load_page(0)
        pix = page.get_pixmap()
        base_name = os.path.basename(file_path.replace(".pdf", ".jpeg"))
        thumnail_path = os.path.join(BASE_DIR,"storage","thumnails", base_name)
        pix.save(thumnail_path)
        doc.close()
        return thumnail_path
    
    def get_total_pages(self,file_path):
        doc = fitz.open(file_path)
        total = len(doc)
        return total
    
    def convert_to_images(self,file_path):
        folder_name = os.path.basename(file_path).replace(".pdf", "")
        dir_path = os.path.join(BASE_DIR, "storage", "pdf's", folder_name)
        doc = fitz.open(file_path)
        image_paths = []
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            for i in range(len(doc)):
                page = doc.load_page(i)
                matrix = pymupdf.Matrix(2,2)
                pix = page.get_pixmap(matrix=matrix)
                img_path = os.path.join(dir_path, f"{i}st_page.jpg")
                pix.save(img_path)
                image_paths.append(img_path)
        doc.close()
        return image_paths
    
    