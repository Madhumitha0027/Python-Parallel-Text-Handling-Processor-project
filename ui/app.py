import sys
import os

# Project root path add cheyadam (module error avoid)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import pandas as pd

from database.db_manager import fetch_all, create_table, insert_result, clear_table
from modules.text_loader import split_text, parallel_process
from modules.rule_engine import calculate_sentiment

# 🔥 multiprocessing kosam function TOP LEVEL lo undali
def process_chunk(chunk):
    score, tag = calculate_sentiment(chunk)
    insert_result(chunk, score, tag)

# ---------------- UI SETTINGS ----------------
st.set_page_config(page_title="Python Parallel Text Processor", layout="wide")

# 🔥 Professional styling
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Python Parallel Text Processor — Dashboard")

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## ⚙️ Navigation Panel")
st.sidebar.write("Python Parallel Text Processor")

page = st.sidebar.radio(
    "Navigate",
    ["Upload & Process", "Overview", "Analytics"]
)

# Ensure table exists
create_table()

# Load DB data
data = fetch_all()

# ---------------- PAGE 1 : UPLOAD ----------------
if page == "Upload & Process":

    st.header("📂 Upload & Manage Text Files")

    uploaded_file = st.file_uploader("Upload .txt file", type=["txt"])

    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        st.success("File uploaded successfully!")

        if st.button("🚀 Start Processing"):

            clear_table()

            chunks = split_text(text)

            # 🔥 TRUE MULTI-PROCESS EXECUTION
            parallel_process(chunks, process_chunk)

            st.success("✅ Processing Completed!")

# ---------------- PAGE 2 : OVERVIEW ----------------
elif page == "Overview":

    st.header("📋 Processed Records Overview")

    if data:
        df = pd.DataFrame(data, columns=["id","text","score","tag","time"])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No data available")

# ---------------- PAGE 3 : ANALYTICS ----------------
elif page == "Analytics":

    st.header("📈 Analytics Dashboard")

    if data:
        df = pd.DataFrame(data, columns=["id","text","score","tag","time"])

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Sentiment Distribution")
            tag_counts = df["tag"].value_counts()
            fig = tag_counts.plot.pie(autopct='%1.1f%%', figsize=(5,5)).figure
            st.pyplot(fig)

        with col2:
            st.subheader("Score Distribution")
            score_counts = df["score"].value_counts().sort_index()
            st.bar_chart(score_counts)

    else:
        st.info("No analytics data yet")