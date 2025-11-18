import streamlit as st
import sys

# Force reload of utils module to bypass caching
if 'utils' in sys.modules:
    del sys.modules['utils']

from utils import build_navigation

# Page configuration
st.set_page_config(
    page_title="AI Starter App",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Build navigation from pages directory
pages = build_navigation()

# Debug: Print URL paths to console (will appear in server logs)
print("DEBUG: Building navigation...")
for topic, page_list in pages.items():
    print(f"  Topic: {topic} - {len(page_list)} pages")

# Create navigation and run the selected page
if pages:
    pg = st.navigation(pages)
    pg.run()
else:
    # Fallback if no pages found
    st.title("🤖 Streamlit/Ollama Starter App")
    st.sidebar.info(
        "This is a starter application showcasing Python, Streamlit, "
        "and Ollama integration examples."
    )
    st.warning("No pages found in the pages directory.")
