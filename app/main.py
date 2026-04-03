import streamlit as st 
import os 
import sys
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)
from db.database import init_db
from core.services import DocumentService
service = DocumentService()



base_dir = os.path.join(os.path.dirname(__file__), "..")

init_db()
st.set_page_config(page_title="DocManager", layout="wide")

st.title('📂📂📂 PDF MANAGER')

st.divider()

upload , search, Analytics = st.tabs(["Upload", "Search and view", "Analytics"])

with upload:
    st.header("Upload your pdf here: ")
    uploaded_file = st.file_uploader("Upload PDF", type = ["pdf"])
    tags = st.text_input("Tags (Comma Seperated)")
    description = st.text_area("Description")
    lecture_date = st.date_input("Lecture_date (optional)", value=None)
    submit = st.button("SUBMIT", type = "primary")
    if submit:
        if uploaded_file:
            service.upload_document(uploaded_file, tags, description, lecture_date)
            pass
        else:
            st.error("please upload a pdf file")
        
    pass

with search:
    pass 

with Analytics:
    pass 


 
