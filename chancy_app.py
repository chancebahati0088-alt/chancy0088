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
    background:#0B0F19;
}

.main{
    background:#0B0F19;
}

.block-container{
    padding-top:2rem;
    max-width:900px;
}

.robot{
    width:180px;
    height:180px;
    margin:auto;
    border-radius:50%;
    background:linear-gradient(135deg,#6C2BD9,#A855F7);
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:90px;
    box-shadow:0 0 40px rgba(168,85,247,.6);
}

.title{
    text-align:center;
    color:white;
    font-size:55px;
    font-weight:bold;
    margin-top:20px;
}

.subtitle{
    text-align:center;
    color:#C084FC;
    font-size:28px;
}

.desc{
    text-align:center;
    color:#D1D5DB;
    font-size:18px;
    margin-bottom:30px;
}

.card{
    background:rgba(124,58,237,.18);
    border:1px solid rgba(168,85,247,.45);
    border-radius:18px;
    padding:15px;
    margin-bottom:12px;
    color:white;
    font-size:18px;
    transition:.3s;
}

.card:hover{
    background:rgba(124,58,237,.35);
}

div.stButton > button{
    width:100%;
    height:60
