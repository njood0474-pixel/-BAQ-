import streamlit as st
from pathlib import Path
st.set_page_config(page_title="BAQĀ", page_icon="✨", layout="wide")
st.markdown(Path("styles/style.css").read_text(), unsafe_allow_html=True)

if "entered" not in st.session_state:
    st.session_state.entered = False

def splash():
    st.markdown('<div class="baqa-splash-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="baqa-splash-card">', unsafe_allow_html=True)
    video_path = Path("assets/intro_baqa.mp4")
    if video_path.exists():
        with open(video_path, "rb") as vf:
            st.video(vf.read(), autoplay=True, muted=True)
    else:
        st.markdown("**Place your intro video at** `assets/intro_baqa.mp4`", unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)
    if st.button("Enter user", type="primary"):
        st.session_state.entered = True
        st.experimental_rerun()

def topbar():
    left, right = st.columns([1,6])
    with left:
        if Path("assets/logo.png").exists():
            st.image("assets/logo.png", width=42)
    with right:
        st.markdown('<div class="baqa-title">Welcome Back</div>', unsafe_allow_html=True)

if not st.session_state.entered:
    splash()
else:
    topbar()
    st.page_link("pages/dashboard.py", label="🏠 Dashboard", icon="🏠")
    st.page_link("pages/statistics.py", label="📈 Statistics", icon="📈")
    st.page_link("pages/reports.py", label="🧾 Reports", icon="🧾")
    st.page_link("pages/physician.py", label="👩‍⚕️ Physician", icon="👩‍⚕️")
    st.page_link("pages/settings.py", label="⚙️ Settings", icon="⚙️")
