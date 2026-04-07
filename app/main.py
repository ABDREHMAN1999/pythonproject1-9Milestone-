import streamlit as st
import os
import sys
import datetime

# ---------------- PATH SETUP ----------------
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from db.database import init_db, connect
from core.services import DocumentService
from core.analyticsservice import AnalyticsService

service = DocumentService()
ana = AnalyticsService()

# ---------------- SESSION STATE ----------------
if "reader_mode" not in st.session_state:
    st.session_state.reader_mode = False

if "selected_doc" not in st.session_state:
    st.session_state.selected_doc = None

if "current_page" not in st.session_state:
    st.session_state.current_page = 0

if "search_results" not in st.session_state:
    st.session_state.search_results = []

# ---------------- INIT ----------------
init_db()
st.set_page_config(page_title="DocManager", layout="wide")

st.title("📂📂📂 PDF MANAGER")
st.divider()

upload_tab, search_tab, analytics_tab = st.tabs(
    ["Upload", "Search and view", "Analytics"]
)

# ================= UPLOAD =================
with upload_tab:
    st.header("Upload your pdf here:")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    upload_tags = st.text_input("Tags (Comma Seperated)")
    description = st.text_area("Description")
    lecture_date = st.date_input("Lecture_date (optional)", value=None)

    submit = st.button("SUBMIT", type="primary")

    if submit:
        if uploaded_file:
            ana.update_analytics_table("SUBMIT")
            service.upload_document(
                uploaded_file, upload_tags, description, lecture_date
            )
            st.success("File uploaded successfully")
        else:
            st.error("Please upload a PDF file")

# ================= SEARCH =================
with search_tab:

    # ---------- READER MODE ----------
    if st.session_state.reader_mode and st.session_state.selected_doc:
        st.subheader("📖 Reader Mode")

        doc = st.session_state.selected_doc

        st.write("✅ Hello - Reader Mode Active")
        st.write(f"Title: {doc[1]}")
        st.write(f"Description: {doc[4]}")
        folder_path = os.path.basename(doc[2]).replace(".pdf", "")
        img_dir = os.path.join("storage","pdf's",folder_path)
        images = sorted(os.listdir(img_dir))
        total_pages = len(images)
        current_page = st.session_state.current_page
        col1 , col2, col3 = st.columns([1,2,1])
        with col1:
            if st.button("<-previous", type = "primary") and current_page>0:
                ana.update_analytics_table("<-previous")
                st.session_state.current_page -=1
                st.rerun()
                
        with col3:
            if st.button("next->", type = "primary") and current_page<total_pages-1:
                ana.update_analytics_table("next->")
                st.session_state.current_page +=1
                st.rerun()
        img_path = os.path.join(img_dir, images[current_page])
        st.image(img_path)
        
        #recored page visit analytics
        ana.update_analytics(doc[0], st.session_state.current_page,str(datetime.datetime.now().isoformat()))
        pages_completed = ana.get_unique_pages(doc[0])
        
        progress = (pages_completed/total_pages)*100 if total_pages else 0
        st.progress(progress/100)
        st.write(f"Completed>>>{progress}%")
        
        
        with open(doc[2],"rb") as f:
            data_pdf = f.read()
        download = st.download_button("Download PDF", data = data_pdf, mime= "application/pdf", file_name=doc[1], type = "primary")
        if download:
            ana.update_analytics_table("Download")
        if st.button("⬅ Back", type = "primary"):
            ana.update_analytics_table("⬅ Back")
            st.session_state.reader_mode = False
            st.session_state.selected_doc = None
            st.rerun()
            
        

    # ---------- SEARCH MODE ----------
    else:
        col1, col2 = st.columns(2)

        with col1:
            search_tags = st.text_input("Search by tags")
            tag_search_button = st.button(
                "Search", key="tag_search", type="primary"
            )

        with col2:
            search_date = st.text_input("Search by date")
            date_search_button = st.button(
                "Search", key="date_search", type="primary"
            )

        # 👉 Store results in session state
        if tag_search_button or date_search_button:
            ana.update_analytics_table("Search")
            st.session_state.search_results = service.search_doc(
                search_tags, search_date
            )

        rows = st.session_state.search_results

        # 👉 Always display if exists
        if rows:
            st.subheader("Documents")

            container = st.container(border=True, height=600)

            with container:
                for doc in rows:
                    c1, c2 = st.columns([1, 4])

                    with c1:
                        if doc[3] and os.path.exists(doc[3]):
                            st.image(doc[3])

                    with c2:
                        st.write(doc[1])  # title
                        st.write(doc[4])  # description
                        st.write(doc[5])  # tags
                        st.write(doc[7])  # date
                        if st.button("Open", key=f"open_{doc[0]}"):
                            ana.update_analytics_table("Open")
                            st.session_state.reader_mode = True
                            st.session_state.selected_doc = doc
                            st.session_state.current_page = 0
                            st.rerun()

# ================= ANALYTICS =================
with analytics_tab:
    st.write("Analytics coming soon...")