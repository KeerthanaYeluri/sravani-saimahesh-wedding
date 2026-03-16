import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Sravani & Sai Mahesh | Wedding",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI elements
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.block-container {padding: 0 !important; max-width: 100% !important;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stStatusWidget"] {display: none;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

base_dir = os.path.dirname(os.path.abspath(__file__))

def load_image_b64(filename):
    filepath = os.path.join(base_dir, "assets", "images", filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

sravani_b64 = load_image_b64("sravani_compressed.jpg")
saimahesh_b64 = load_image_b64("saimahesh_compressed.jpg")

html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

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

st.components.v1.html(html_content, height=8000, scrolling=True)