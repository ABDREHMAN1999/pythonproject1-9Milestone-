import streamlit as st
import os
import sys

# ---------------- PATH SETUP ----------------
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from db.database import init_db, connect
from core.services import DocumentService

service = DocumentService()

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

        if st.button("⬅ Back"):
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
                            st.session_state.reader_mode = True
                            st.session_state.selected_doc = doc
                            st.session_state.current_page = 0
                            st.rerun()

# ================= ANALYTICS =================
with analytics_tab:
    st.write("Analytics coming soon...")