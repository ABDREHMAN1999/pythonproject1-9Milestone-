import streamlit as st 
import os 
import sys
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)
from db.database import init_db


base_dir = os.path.join(os.path.dirname(__file__), "..")

init_db()
st.set_page_config(page_title="DocManager", layout="wide")

st.title('📂📂📂 PDF MANAGER')

st.divider()

upload , search, Analytics = st.tabs(["Upload", "Search and view", "Analytics"])

with upload:
    pass

with search:
    pass 

with Analytics:
    pass 


 
