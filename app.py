import streamlit as st
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS  # FAISS au lieu Chroma

st.title("🤖 RAG Assistant - Amal AYADI")
st.write("Upload PDF → Recherche intelligente !")

uploaded_file = st.file_uploader("📄 PDF", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name
    
    # Load + split
    loader = PyPDFLoader(tmp_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    texts = splitter.split_documents(docs)
    
    # Embed + vectorstore (FAISS = stable Streamlit)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(texts, embeddings)
    
    st.success("✅ Document analysé !")
    
    query = st.text_input("🔍 Question :")
    if st.button("Rechercher") and query:
        docs = vectorstore.similarity_search(query, k=3)
        st.subheader("**Top 3 réponses :**")
        for i, doc in enumerate(docs, 1):
            st.write(f"**{i}.** {doc.page_content[:350]}...")
            st.write("---")
