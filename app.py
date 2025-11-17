import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Starter App",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("🤖 Streamlit/Ollama Starter App")


st.sidebar.info(
    "This is a starter application showcasing Python, Streamlit, "
    "and Ollama integration examples."
)
