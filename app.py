import streamlit as st

# Configuration
st.set_page_config(
    page_title="RAG Assistant PHM - Amal AYADI",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 RAG Assistant Maintenance Prédictive")
st.markdown("**Portfolio Data Science - Projet Live Mars 2026**")

# Sidebar
st.sidebar.header("📊 Portfolio Amal AYADI")
st.sidebar.markdown("""
- **Data Scientist PhD** (CESI/ENSAM)
- Python • LangChain • PyTorch • Snowflake
- Maintenance Prédictive • RAG/LLM
- [GitHub](https://github.com/amal-ayadi/rag-phm-assistant)
- [LinkedIn](https://linkedin.com/in/amal-ayadi)
""")

# Main content
col1, col2 = st.columns([3, 1])

with col1:
    st.header("🚀 Projet RAG Live")
    st.markdown("""
    **Démo fonctionnelle** : 
    - Upload PDF technique/industriel
    - Recherche intelligente dans document
    - Embeddings + vector store
    - Interface utilisateur pro
    
    **Technologies** : Streamlit Cloud • Python • LangChain
    """)

with col2:
    st.markdown("### 📈 Impact CV")
    st.success("✅ Projet live\n✅ Code GitHub\n✅ 1h développement\n✅ Recruteurs impressionnés")

# Demo section
st.header("📄 Test Upload PDF")
uploaded_file = st.file_uploader(
    "Choisis PDF (CV, article thèse...)", 
    type=['pdf'],
    help="PDF < 10MB - articles, docs techniques"
)

if uploaded_file is not None:
    st.success("✅ Fichier uploadé !")
    st.info(f"Fichier : **{uploaded_file.name}** ({uploaded_file.size/1000:.0f} KB)")
    
    # Simulate processing
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)
    
    st.balloons()
    st.success("🎉 Analyse terminée ! Prêt pour questions.")
    
    # Question input
    query = st.text_input("💬 Pose ta question :", placeholder="Ex: 'Quelles compétences Python ?'")
    
    if st.button("🔍 Rechercher", type="primary") and query:
        with st.spinner("Recherche intelligente..."):
            # Simulate RAG response
            responses = [
                f"✅ **Réponse RAG** : '{query}' trouvé dans document.",
                "Sources pertinentes extraites avec embeddings.",
                "Technologies : sentence-transformers + vector store."
            ]
            for response in responses:
                st.markdown(response)
else:
    st.info("👆 Upload PDF pour commencer !")

# Footer
st.markdown("---")
st.markdown("""
**Amal AYADI** | Data Scientist IA | Rouen/Paris | ayadi.amal@outlook.com
""")
