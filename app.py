import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Sravani & Sai Mahesh | Wedding",
    page_icon="ring",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI elements for clean look
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp > header {display: none;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {border: none;}
    [data-testid="stToolbar"] {display: none;}
    [data-testid="stDecoration"] {display: none;}
    [data-testid="stStatusWidget"] {display: none;}
</style>
""", unsafe_allow_html=True)

def get_image_base64(image_path):
    """Convert image to base64 for embedding in HTML."""
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

# Get base64 encoded images (compressed versions)
base_dir = os.path.dirname(os.path.abspath(__file__))
sravani_b64 = get_image_base64(os.path.join(base_dir, "assets", "images", "sravani_compressed.jpg"))
saimahesh_b64 = get_image_base64(os.path.join(base_dir, "assets", "images", "saimahesh_compressed.jpg"))

# Read the HTML file
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace image file paths with base64 data URIs so images work in Streamlit
if sravani_b64:
    html_content = html_content.replace(
        'src="assets/images/sravani.JPG"',
        'src="data:image/jpeg;base64,' + sravani_b64 + '"'
    )

if saimahesh_b64:
    html_content = html_content.replace(
        'src="assets/images/SaiMahesh.JPG"',
        'src="data:image/jpeg;base64,' + saimahesh_b64 + '"'
    )

# Render the full HTML page
st.components.v1.html(html_content, height=8000, scrolling=True)