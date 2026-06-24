import streamlit as st
import random
st.set_page_config(page_title="Chancy AI", page_icon="")
# ---------------------------
# INFORMATIONS DU CREATEUR
# ---------------------------
NOM_CREATEUR = "Murhula Bahati Chance"
AGE_CREATEUR = 17
PAYS_CREATEUR = "République Démocratique du Congo"
PROVINCE_CREATEUR = "Sud-Kivu"
# ---------------------------
# CHANCY (AI)
# ---------------------------
st.title("Chancy AI")
st.write("Je suis Chancy, une intelligence artificielle en développemment")
st.write(f"Mon créateur est {NOM_CREATEUR}")
# ---------------------------
# CHAT HISTORIQUE
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
for mgs in st.session_state.messages:
    st.write(mgs)
    question = st.text_input("Écris ton message")
    # ---------------------------
    # BLANGUES
    # ---------------------------
    blangues = ["Pourquoi les développeurs aiment Python ? Parce que c'est simple !",
            "J'ai essayé de dormir... mais j'avais un bug", "Je suis une IA, je ne dors jamais !"]
    # ---------------------------
    # LOGIQUE
    # ---------------------------
if question:
    q = question.lower()
st.session_state.messages.append("Toi : " + question)
    # contenu interdit
if "sexe" in q or "porno" in q or "adulte" in q:
    reponse = "Chancy : Désolée, je ne peux pas vous aider avec cette demande. Cela fait partie des consignes données par mon créateur, Chance Bahati, m'a programmée pour respectueuse, responsable, utile à tous les utiltsateurs et suivre des règles de sécurité."
    # créateur
elif "créateur" in q or "qui t'a créé" in q or "qui t'a programméé" in q:
        reponse = f"Chancy : Mon créateur est {NOM_CREATEUR}"
    # AGE CREATEUR
elif "àge du créateur" in q or "age du créateur" in q:
        reponse = f"Chancy : Mon créateur a {CREATEUR_AGE} ans"
    # PAYS CREATEUR
elif "pays du créateur" in q:
        reponse = f"Chancy : Mon créateur vient du {PAYS_CREATEUR}"
    # REGION 
elif "province" in q or "Sud Kivu" in q:
        reponse = f"Chancy : Mon créateur vient du {REGION_CREATEUR}"
    # SALUT
elif "bonjour" in q or "salut" in q or "coucou" in q or "hey" in q or "ça va" in q:
        reponse = "Chancy : Bonjour"
    # BLAGUE
elif "blague" in q:
        renpose = random.choice(blagues)
    # DEFAULT  
else:
        reponse = "Chancy : Je suis encore en développement"
st.session_state.messages.append(reponse)
st.rerun()
st.write("---")
st.caption("Chancy AI | Projet de Chance Bahati")
