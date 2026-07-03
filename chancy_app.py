import streamlit as st

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

h1,h2,h3,p{
    color:white;
    text-align:center;
}

div.stButton > button{
    width:250px;
    height:55px;
    border:none;
    border-radius:30px;
    background:#9D4EDD;
    color:white;
    font-size:20px;
    font-weight:bold;
}

div.stButton > button:hover{
    background:#C77DFF;
}
</style>
""", unsafe_allow_html=True)

if st.session_state.page == "home":

    st.markdown("<h1>🤖 CHANCY AI</h1>", unsafe_allow_html=True)

    st.markdown("<h2>Bienvenue sur Chancy AI</h2>", unsafe_allow_html=True)

    st.markdown("<h3>Votre assistante personnelle en programmation</h3>", unsafe_allow_html=True)

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

else:

    st.title("💬 Chancy AI")

    st.text_input("Écris ton message")

    if st.button("Envoyer"):
        st.success("Le chat sera développé à l'étape suivante.")
