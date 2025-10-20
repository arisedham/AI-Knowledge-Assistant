# app/backend/rag_pipeline.py
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_classic.chains import RetrievalQA

# You must export your API key before running:
# export OPENAI_API_KEY="your-key"

def load_document(path: str):
    if path.endswith(".pdf"):
        loader = PyPDFLoader(path)
    else:
        loader = TextLoader(path)
    return loader.load()


def process_document(doc_path: str, faiss_dir: str):
    """Split document → embed → store in FAISS"""
    docs = load_document(doc_path)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    splits = text_splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(splits, embedding=embeddings)

    # save FAISS index to disk
    vectorstore.save_local(faiss_dir)


def answer_question(question: str, faiss_dir: str):
    """Retrieve context + generate answer"""
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local(faiss_dir, embeddings, allow_dangerous_deserialization=True)

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    result = qa_chain.invoke({"query": question})
    return result["result"]
