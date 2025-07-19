# 📘 RAG QA System (with Groq API + Streamlit)

This is a **Retrieval-Augmented Generation (RAG)** based Question Answering system that allows you to:

- Upload any **PDF**
- Ask **natural language questions**
- Get answers **based on the actual content** of the uploaded document

It uses **LangChain**, **Groq API (LLM)**, and **Streamlit** for an interactive user interface.

---

## 🚀 Features

✅ Upload and parse PDF files  
✅ Chunk and embed content using Sentence Transformers  
✅ Store embeddings in a FAISS vector store  
✅ Query the PDF context using natural language  
✅ Use **Groq API** for fast and accurate LLM responses  
✅ Simple and beautiful **Streamlit UI**

---

## 🧠 Architecture

1. **PDF Loader** – Reads and chunks PDF  
2. **Embedder** – Generates vector embeddings  
3. **Retriever** – Retrieves most similar chunks  
4. **Generator** – Uses Groq LLM to answer based on retrieved context

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/farshadabdulazeez/rag_qa_system.git
cd rag_qa_system



