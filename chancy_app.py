import streamlit as st

# -----------------------------
# Configuration
# -----------------------------
st.set_page_config(
    page_title="Chancy AI",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Mémoire
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -----------------------------
# Style
# -----------------------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#16002E,#3A
