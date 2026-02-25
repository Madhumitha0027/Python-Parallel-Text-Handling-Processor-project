# Python-Parallel-Text-Handling-Processor-project

## 📌 Project Overview
Python Parallel Text Handling Processor is a scalable text processing system developed using Python.  
The application processes large volumes of textual data using parallel execution techniques and stores results in an SQLite database.  
The project also includes performance benchmarking, scalability testing, and an interactive Streamlit dashboard.

---

## 🚀 Implemented Features
- Text and CSV file processing
- Text chunking for large dataset handling
- Parallel execution (Single, ThreadPoolExecutor, Multiprocessing)
- Performance benchmarking and scalability testing
- SQLite database integration
- Database indexing for optimized queries
- Bulk data insertion
- Streamlit-based analytics dashboard

---

## 🔄 System Flow
User Upload  
↓  
Text Chunking  
↓  
Parallel Processing  
↓  
SQLite Database Storage  
↓  
Streamlit Dashboard

---

## 🔄 System Flow

The system follows a structured pipeline to process large-scale text data efficiently.

1️⃣ **User Upload**  
Users upload text or CSV files through the Streamlit interface. The system reads and prepares the input data for processing.

2️⃣ **Text Chunking**  
Large text content is divided into smaller chunks to make processing faster and more scalable.

3️⃣ **Parallel Processing**  
Chunks are processed using different execution strategies such as single execution, threading, or multiprocessing to improve performance.

4️⃣ **Database Storage**  
Processed results are stored in an SQLite database. Indexing is used to improve query speed and data retrieval.

5️⃣ **Analytics Dashboard**  
The stored data is displayed in the Streamlit dashboard where users can view records, analytics, and summary information.

 ---
 
## ⚙️ Technologies Used
- Python
- Streamlit
- SQLite
- concurrent.futures
- Pandas

---

## 📂 Project Structure

```
parallel_text_processor/
│
├── ui/
│   └── app.py                # Streamlit dashboard
│
├── modules/
│   ├── text_loader.py        # Text chunking & parallel loader
│   └── rule_engine.py        # Weighted sentiment scoring
│
├── database/
│   └── db_manager.py         # SQLite database operations
│
├── benchmark_test.py         # Performance & scalability testing
├── main.py                   # Core processing script
├── texts.db                  # SQLite database file
├── README.md
```
---

## ▶️ How to Run

Run UI:
streamlit run ui/app.py

Run Benchmark Tests:
python benchmark_test.py

---
