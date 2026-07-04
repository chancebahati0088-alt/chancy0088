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
        st.info("⚡ JavaScript")

    with col2:
        st.info("☕ Java")
        st.info("⚙️ C")
        st.info("🖥️ C++")
        st.info("💎 C#")

    with col3:
        st.info("🐘 PHP")
        st.info("🗄️ SQL")
        st.info("📱 Flutter")
        st.info("🎯 Dart")

    st.write("")

    if st.button("🚀 COMMENCER"):
        st.session_state.page = "chat"
        st.rerun()
