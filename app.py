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

sravani_b64 = load_image_b64("sravani_compressed.jpg")
saimahesh_b64 = load_image_b64("saimahesh_compressed.jpg")

sravani_uri = "data:image/jpeg;base64," + sravani_b64 if sravani_b64 else ""
saimahesh_uri = "data:image/jpeg;base64," + saimahesh_b64 if saimahesh_b64 else ""

html_path = os.path.join(base_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace image paths with base64
html_content = html_content.replace('src="assets/images/sravani.JPG"', 'src="' + sravani_uri + '"')
html_content = html_content.replace('src="assets/images/SaiMahesh.JPG"', 'src="' + saimahesh_uri + '"')

# Fix: Force all animated elements to be visible (IntersectionObserver doesn't work in iframes)
# Also fix hero height for iframe context
fix_css = """
<style>
.animate-on-scroll {
    opacity: 1 !important;
    transform: none !important;
}
.hero {
    min-height: 700px !important;
    height: auto !important;
}
.navbar {
    position: absolute !important;
}
</style>
"""
html_content = html_content.replace("</head>", fix_css + "</head>")

# Hide Streamlit UI
st.markdown("""
<style>
#MainMenu, header, footer, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stStatusWidget"],
[data-testid="stHeader"] {
    display: none !important;
}
.block-container, .stMainBlockContainer {
    padding: 0 !important;
    max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

st.components.v1.html(html_content, height=6000, scrolling=True)
