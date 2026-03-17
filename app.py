import streamlit as st
import os
import tempfile

st.set_page_config(page_title="RAG Assistant - Amal AYADI", layout="wide")

st.title("🤖 RAG Assistant Maintenance Prédictive")
st.markdown("**Portfolio Data Science - Projet Live Mars 2026**")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Fonctionnalités
    - 📄
