from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# Initialize the LLM
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192"
)

# Prompt template
template = """
Use the following context to answer the question.
If you don't know the answer, just say you don't know — don't make it up.

Context:
{context}

Question:
{question}

Answer:
"""

prompt = PromptTemplate.from_template(template)
chain = prompt | llm | StrOutputParser()

def generate_answer(context, question):
    return chain.invoke({"context": context, "question": question})
