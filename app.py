import streamlit as st
from pathlib import Path

# --- 1. PAGE CONFIGURATION ---
# This must be the first Streamlit command in your script
st.set_page_config(
    page_title="BAQĀ Dashboard",
    page_icon="✨",
    layout="wide"
)

# --- 2. LOAD CUSTOM CSS ---
# A function to load the local CSS file
def load_local_css(file_name):
    css_path = Path("styles") / file_name
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.error(f"CSS file not found at {css_path}")

# Call the function to load the CSS
load_local_css("style.css")

# --- 3. SESSION STATE INITIALIZATION ---
# This ensures the 'entered' flag is set to False on the first run
if "entered" not in st.session_state:
    st.session_state.entered = False

# --- 4. SPLASH SCREEN FUNCTION ---
def splash():
    """Displays the splash screen with a video and an entry button."""
    # Use st.columns to center the splash content
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="baqa-splash">', unsafe_allow_html=True)
        
        video_path = Path("assets/intro_baqa.mp4")
        if video_path.exists():
            # Read video file as bytes and display it
            st.video(str(video_path), format="video/mp4", start_time=0, loop=True, autoplay=True, muted=True)
        else:
            st.warning("Place your intro video at `assets/intro_baqa.mp4`")
        
        # The button that will trigger the state change
        if st.button("Enter Dashboard", type="primary", use_container_width=True):
            st.session_state.entered = True
            st.rerun() # Use st.rerun() which is the modern replacement for experimental_rerun
            
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. MAIN APPLICATION FUNCTION ---
def main_app():
    """Displays the main dashboard content after the user enters."""
    # --- Sidebar ---
    with st.sidebar:
        if Path("assets/logo.png").exists():
            st.image("assets/logo.png", width=60)
        st.header("Dashboard Options")
        st.write("Here you can place filters and inputs for your dashboard.")
        
        selected_option = st.selectbox("Choose a category:", ["Overall Performance", "User Analytics", "Revenue"])
        date_range = st.date_input("Select Date Range", [])

    # --- Main Content ---
    st.title("Main Control Panel")
    st.markdown("---")

    # --- KPI Cards ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class="baqa-card">
                <div class="kpi-sub">Total Users</div>
                <div class="kpi-big">1,284</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div class="baqa-card">
                <div class="kpi-sub">Completion Rate</div>
                <div class="kpi-big">93%</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """
            <div class="baqa-card">
                <div class="kpi-sub">Monthly Revenue</div>
                <div class="kpi-big">SAR 45,910</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --- Charts ---
    st.subheader("Performance Chart")
    st.bar_chart({"data": [10, 20, 15, 30, 25, 50, 45]})


# --- 6. MAIN LOGIC GATE ---
# This decides whether to show the splash screen or the main app
if not st.session_state.entered:
    splash()
else:
    main_app()
