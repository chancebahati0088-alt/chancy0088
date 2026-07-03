import streamlit as st

# -----------------------------
# Configuration de la page
# -----------------------------
st.set_page_config(
    page_title="Chancy AI",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Style de la page
# -----------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(180deg,#12002b,#2a0055,#4b0082);
    color:white;
}

h1,h2,h3,p{
    color:white;
}

div.stButton > button{
    background:#8A2BE2;
    color:white;
    border-radius:15px;
    height:55px;
    width:250px;
    font-size:22px;
    font-weight:bold;
    border:none;
}

div.stButton > button:hover{
    background:#9d4edd;
}

</style>
""", unsafe_allow_html=True)
