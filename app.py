import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Sravani & Sai Mahesh | Wedding",
    layout="wide",
    initial_sidebar_state="collapsed"
)

base_dir = os.path.dirname(os.path.abspath(__file__))

def load_image_b64(filename):
    filepath = os.path.join(base_dir, "assets", "images", filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

# Load compressed images as base64
sravani_b64 = load_image_b64("sravani_compressed.jpg")
saimahesh_b64 = load_image_b64("saimahesh_compressed.jpg")

# Build data URIs
sravani_uri = "data:image/jpeg;base64," + sravani_b64 if sravani_b64 else ""
saimahesh_uri = "data:image/jpeg;base64," + saimahesh_b64 if saimahesh_b64 else ""

# Read HTML
html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace image paths with base64
html_content = html_content.replace('src="assets/images/sravani.JPG"', 'src="' + sravani_uri + '"')
html_content = html_content.replace('src="assets/images/SaiMahesh.JPG"', 'src="' + saimahesh_uri + '"')

# Hide all Streamlit UI and make the iframe fill the screen
st.markdown("""
<style>
    #MainMenu, header, footer, [data-testid="stToolbar"],
    [data-testid="stDecoration"], [data-testid="stStatusWidget"],
    [data-testid="stHeader"] {
        display: none !important;
        visibility: hidden !important;
    }
    .stApp {
        background: transparent;
    }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    .stMainBlockContainer {
        padding: 0 !important;
    }
    iframe[title="streamlit_components.v1.components.html"] {
        width: 100vw !important;
        height: 100vh !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        border: none !important;
        z-index: 9999 !important;
    }
</style>
""", unsafe_allow_html=True)

# Render HTML
st.components.v1.html(html_content, height=6000, scrolling=True)