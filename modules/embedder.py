from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

def generate_embeddings(chunks):
    # Wrap each text chunk as a Document
    documents = [Document(page_content=chunk) for chunk in chunks]
    
    model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(documents, embedding=model)
    return vectorstore
