from pdfminer.high_level import extract_text
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_chunk_pdf(file_path, chunk_size=500, chunk_overlap=50):
    text = extract_text(file_path)
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_text(text)
    return chunks
