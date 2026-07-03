import streamlit as st
from home import show_home

st.set_page_config(
    page_title="Chancy AI",
    page_icon="🤖",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "home"

st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg,#1B0036,#4B0082,#7B2CBF);
}
</style>
""", unsafe_allow_html=True)

if st.session_state.page == "home":
    show_home()

elif st.session_state.page == "chat":

    st.title("💬 Chancy AI")

    message = st.text_input("Écris ton message")

    if st.button("Envoyer"):
        st.success(f"Vous avez écrit : {message}")
