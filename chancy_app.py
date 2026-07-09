import streamlit as st

st.set_page_config(
    page_title="Chancy AI",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #0B0F19;
    color: white;
}

.title {
    text-align: center;
    color: white;
    font-size: 60px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #c084fc;
    font-size: 24px;
}

.robot {
    text-align: center;
    font-size: 100px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="robot">🤖</div>', unsafe_allow_html=True)
st.markdown('<div class="title">CHANCY AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Bienvenue sur Chancy AI<br>Votre assistante personnelle en programmation</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="robot">🤖</div>', unsafe_allow_html=True)
