import os
import streamlit as st
from dotenv import load_dotenv
from modules.loader import load_and_chunk_pdf
from modules.embedder import generate_embeddings
from modules.retriever import retrieve_chunks
from modules.generator import generate_answer

load_dotenv()
st.set_page_config(page_title="📘 RAG QA System", layout="wide")

st.title("📘 RAG QA System")
st.markdown("Upload a PDF and ask questions based on its content.")

uploaded_file = st.file_uploader("📎 Upload PDF", type="pdf")

if uploaded_file:
    with st.spinner("🔍 Processing document..."):
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        chunks = load_and_chunk_pdf("temp.pdf")

        vectorstore = generate_embeddings(chunks)

        query = st.text_input("🧠 Ask a question:")
        if query:
            with st.spinner("🤖 Generating answer..."):
                context = retrieve_chunks(vectorstore, query)
                answer = generate_answer(context, query)
                st.markdown("### 💬 Answer")
                st.markdown(f"> {answer}")
