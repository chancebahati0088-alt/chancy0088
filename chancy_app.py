import streamlit as st

def run_app():
    st.set_page_config(
        page_title="Chancy AI",
        page_icon="🤖",
        layout="centered"
    )

    st.title("🤖 Chancy AI")

    st.write("Bienvenue sur Chancy AI !")

    st.button("Commencer")
