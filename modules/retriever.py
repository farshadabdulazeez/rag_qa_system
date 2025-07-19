def retrieve_chunks(vectorstore, query, k=8):
    docs = vectorstore.similarity_search(query, k=k)
    context = "\n\n".join([doc.page_content for doc in docs])
    return context
