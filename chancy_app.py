import streamlit as st
st.set_page_config(page_title="Chancy AI", page_icon="")
st.("Chancy AI")
st.write("Je suis Chancy, une IA en développement")
st.write("Créée par Chance Bahati")
question = st.text_input("pose ta question")
if question:
    q = question.lower()
    # si on demande le créateur
    if "créateuré" in q or "creator" in q or "qui t'a créé" in q:
         st.success("Chancy : Mon créateur est Chance Bahati")
    # si on demmande le nom
    elif "nom du créateur" in q:
        st.success("Chancy : Mon créateur s'appelle Chance Bahati")
    elif:
        st.success("Chancy : Je suis encore en développement mais j'apprends chaque jour")
st.write("---")
st.caption("Chancy AI | En développement par Chance Bahati")
