📄 Document Manager with Analytics
A simple yet structured Document Management System built using Streamlit and SQLite, designed to upload, manage, and analyze document usage.


🚀 Overview
This project allows users to:
Upload and manage documents
Track page-level interactions
Analyze document usage through basic analytics
It is built with a focus on clean architecture principles, separating UI, business logic, and database layers.


Project structure : 


DocManager/
│
├── app/
│   ├── main.py                  # Streamlit application entry point
│   └── data_baseclear.ipynb     # Notebook for DB testing/clearing
│
├── core/
│   ├── analyticsservice.py      # Analytics logic (page tracking, counts)
│   ├── filemanager.py           # File handling (upload, storage)
│   └── services.py              # Document service logic
│
├── Data/
│   └── pdf.db                  # SQLite database file
│
├── db/
│   └── database.py             # DB connection and initialization
│
├── storage/
│   ├── pdfs/                  # Stored uploaded PDF files
│   └── thumbnails/            # Generated thumbnails (if any)
│
├── .venv/                     # Virtual environment
├── .vscode/                   # VS Code settings
├── .python-version            # Python version config
├── pyproject.toml             # Project dependencies/config
├── uv.lock                    # Dependency lock file
├── README.md                  # Project documentation
└── rough.ipynb                # Experimentation notebook


🧠 Key Features
📂 Upload and store documents
🗃️ Persistent storage using SQLite
📊 Track page visits per document
🔍 Count unique pages viewed
🖥️ Interactive UI with Streamlit


⚙️ Tech Stack
Python
Streamlit – UI framework
SQLite – Lightweight database


🤝 Contribution
This is a learning project, but suggestions and improvements are always welcome!