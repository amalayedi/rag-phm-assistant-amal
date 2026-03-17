import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import tempfile

st.title("🤖 RAG Assistant PHM - Amal AYADI")
uploaded_file = st.file_uploader("📄 PDF technique", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name
    
    loader = PyPDFLoader(tmp_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(docs)
    
    embeddings = HuggingFaceEmbeddings()
    vectorstore = Chroma.from_documents(texts, embeddings)
    
    st.success("✅ Docs analysées !")
    
    query = st.text_input("💬 Question :")
    if st.button("🔍 Rechercher") and query:
        docs = vectorstore.similarity_search(query, k=3)
        st.write("**Top 3 passages pertinents :**")
        for i, doc in enumerate(docs, 1):
            st.write(f"**{i}.** {doc.page_content[:300]}...")
