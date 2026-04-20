import streamlit as st
from pathlib import Path


def load_custom_css():
    css_path = Path("frontend/styles/custom.css")

    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)