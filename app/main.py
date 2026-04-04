import streamlit as st 
import os 
import sys
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)
from db.database import init_db , connect
from core.services import DocumentService
service = DocumentService()



base_dir = os.path.join(os.path.dirname(__file__), "..")

if "reader_mode" not in st.session_state:
    st.session_state.reader_mode = False
    
if "selected_doc" not in st.session_state:
    st.session_state.selected_doc= None

if "current_page" not in st.session_state:
    st.session_state.current_page = 0 

    


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
            st.success("File uploaded Sucessfully")
            pass
        else:
            st.error("please upload a pdf file")
        

with search:
    col1 , col2 = st.columns(2)
    with col1:
        tags = st.text_input("search by tags")
        tag_search_button = st.button("Search", key = "tag search", type = "primary")
    with col2:
        date = st.text_input("search by date")
        date_search_button = st.button("Search", key = "date search", type = "primary")
        
    if (tag_search_button or date_search_button) and not st.session_state.reader_mode:
        rows = service.search_doc(tags, date)
        st.subheader("Documents")
        container = st.container(border= True, height=600)
        with container:
            for doc in rows:
                c1 , c2 = st.columns([1,4])
                with c1:
                    if os.path.exists(doc[3]):
                        st.image(doc[3])
                with c2:
                    st.write(doc[1])
                    st.write(doc[4])
                    st.write(doc[5])
                    st.write(doc[7])
                    if st.button("Open",key = f"open_{doc[0]}"):
                        st.write("BUTTON CLICKED")   # 👈 ADD THIS
                        st.session_state.selected_doc = doc
                        st.session_state.current_page = 0 
                        st.session_state.reader_mode = True
                        st.rerun()
    else:
        st.write("reader mode")
        doc = st.session_state.selected_doc
        st.write(f"Reading  📖📖📖 {doc[1]}")

        

        
        
                
                    
                

with Analytics:
    pass 


 
