import streamlit as st

# ==========================================
# CONFIGURATION DE LA PAGE
# ==========================================

st.set_page_config(
    page_title="Chancy AI",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# MÉMOIRE DE L'APPLICATION
# ==========================================

if "page" not in st.session_state:
    st.session_state.page = "home"

# ==========================================
# STYLE CSS
# ==========================================

st.markdown("""
<style>

.stApp{
    background:linear-gradient(135deg,#1B0036,#4B0082,#7B2CBF);
    color:white;
}

section[data-testid="stSidebar"]{
    display:none;
}

h1,h2,h3,p{
    color:white;
}

.main-title{
    font-size:65px;
    font-weight:bold;
    text-align:center;
    margin-top:40px;
}

.subtitle{
    text-align:center;
    font-size:28px;
    color:#E9D8FD;
}

.description{
    text-align:center;
    font-size:20px;
    max-width:900px;
    margin:auto;
    color:white;
    padding-top:20px;
}

div.stButton > button{
    width:260px;
    height:60px;
    font-size:22px;
    font-weight:bold;
    border-radius:40px;
    border:none;
    background:#9D4EDD;
    color:white;
}

div.stButton > button:hover{
    background:#C77DFF;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# PAGE D'ACCUEIL
# ==========================================

if st.session_state.page == "home":

    st.markdown("<h1 class='main-title'>🤖 Chancy AI</h1>", unsafe_allow_html=True)

    st.markdown(
        "<p class='subtitle'>Bienvenue sur Chancy AI</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<p class='description'>
Je suis <b>Chancy AI</b>, votre assistante personnelle en programmation.<br><br>

Je suis conçue pour vous apprendre la programmation étape par étape,
du niveau débutant jusqu'au niveau professionnel.
</p>
""",
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        if st.button("🚀 Commencer"):
            st.session_state.page="chat"
            st.rerun()

# ==========================================
# PAGE CHAT
# ==========================================

elif st.session_state.page=="chat":

    st.title("💬 Chancy AI")

    st.write("Le chat sera construit dans le prochain cours.")
