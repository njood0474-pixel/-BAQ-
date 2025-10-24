import streamlit as st
st.markdown("## Settings")
st.selectbox("Language", ["English"], index=0)
st.toggle("Compact layout", value=True)
if st.button("Log out"):
    st.session_state.entered = False
    st.switch_page("app.py")