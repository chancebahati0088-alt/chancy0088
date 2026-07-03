import streamlit as st

def show_home():

    st.markdown("<h1 style='text-align:center;'>🤖 CHANCY AI</h1>", unsafe_allow_html=True)

    st.markdown(
        "<h2 style='text-align:center;'>Bienvenue sur Chancy AI</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;'>Votre assistante personnelle en programmation</h3>",
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🐍 Python")
        st.info("🌐 HTML")
        st.info("🎨 CSS")
        st.info("⚡
