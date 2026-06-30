import streamlit as st
import random

st.set_page_config(page_title="Chancy AI", page_icon="🤖", layout="centered")

# Debug flag: active = show full exception details in the app (don't enable in production)
DEBUG = False

try:
    # ---------------------------
    # INFORMATIONS DU CREATEUR
    # ---------------------------
    NOM_CREATEUR = "Murhula Bahati Chance"
    AGE_CREATEUR = 17
    PAYS_CREATEUR = "République Démocratique du Congo"
    PROVINCE_CREATEUR = "Sud-Kivu"

    # ---------------------------
    # RÉPONSES PRÉDÉFINIES
    # ---------------------------
    blagues = [
        "Pourquoi les développeurs aiment Python ? Parce que c'est simple !",
        "J'ai essayé de dormir... mais j'avais un bug",
        "Je suis une IA, je ne dors jamais !"
    ]
    forbidden_words = ["sexe", "porno", "adulte"]

    # ---------------------------
    # ETAT DE SESSION
    # ---------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "input" not in st.session_state:
        st.session_state.input = ""
    if "started" not in st.session_state:
        st.session_state.started = False

    # ---------------------------
    # BARRE LATERALE
    # ---------------------------
    st.sidebar.title("Chancy AI")
    if st.sidebar.button("Accueil"):
        st.session_state.started = False
        st.rerun()
    if st.sidebar.button("Réinitialiser l'historique"):
        st.session_state.messages = []
        st.rerun()

    # ---------------------------
    # ECRAN D'ACCUEIL
    # ---------------------------
    if not st.session_state.started:
        st.markdown("# Chancy AI 👋")
        st.write("Je suis Chancy, votre mini‑chatbot. Je peux vous aider en quoi.")
        st.write(f"Créateur : {NOM_CREATEUR} — {AGE_CREATEUR} ans — {PROVINCE_CREATEUR}, {PAYS_CREATEUR}")
        st.write("---")
        st.write("Essayez : \n- Qui t'a créé ?\n- Raconte une blague\n- D'où vient ton créateur ?")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Démarrer le chat"):
                st.session_state.started = True
                st.rerun()
        with col2:
            st.write("")
            if st.button("Voir le code sur GitHub"):
                st.write("Le code est disponible dans le dépôt GitHub du projet.")

        st.stop()

    # ---------------------------
    # INTERFACE DE CHAT
    # ---------------------------
    st.title("Chancy AI — Chat")
    st.write("Je suis Chancy — pose une question ou dis 'blague' pour que je raconte quelque chose.")
    st.write("---")

    # Affichage de l'historique
    for msg in st.session_state.messages:
        if msg.startswith("Toi :"):
            st.markdown(f"**{msg}**")
        else:
            st.markdown(f"_{msg}_")

    # Champ de saisie
    # On utilise st.session_state['input'] pour conserver l'entrée entre re-runs
    question = st.text_input("Écris ton message", value=st.session_state.input, key="input")
    if st.button("Envoyer"):
        # Récupère le texte actuellement dans session_state['input']
        q_raw = st.session_state.input or ""
        q = q_raw.strip()
        if q:
            # Sauvegarde le message utilisateur
            st.session_state.messages.append("Toi : " + q)
            q_lower = q.lower()

            # Détection des mots interdits
            if any(word in q_lower for word in forbidden_words):
                reponse = "Chancy : Désolée, je ne peux pas vous aider avec cette demande."
            elif "créateur" in q_lower or "qui t'a créé" in q_lower or "qui t'a programmé" in q_lower:
                reponse = f"Chancy : Mon créateur est {NOM_CREATEUR}"
            elif "age" in q_lower or "âge" in q_lower:
                reponse = f"Chancy : Mon créateur a {AGE_CREATEUR} ans"
            elif "pays" in q_lower or "origine" in q_lower or "d'où vient" in q_lower or "d'ou vient" in q_lower:
                reponse = f"Chancy : Mon créateur vient de {PAYS_CREATEUR}"
            elif "province" in q_lower or "sud-kivu" in q_lower or "sud kivu" in q_lower:
                reponse = f"Chancy : Mon créateur vient de la province {PROVINCE_CREATEUR}"
            elif any(g in q_lower for g in ["bonjour", "salut", "coucou", "hey", "ça va", "ca va"]):
                reponse = "Chancy : Bonjour ! Comment puis‑je t'aider ?"
            elif "blague" in q_lower or "raconte" in q_lower:
                reponse = "Chancy : " + random.choice(blagues)
            else:
                reponse = "Chancy : Je suis encore en développement — je ne comprends pas parfaitement, mais j'apprends !"

            # Ajout de la réponse et réinitialisation du champ
            st.session_state.messages.append(reponse)
            st.session_state.input = ""
            st.rerun()
        else:
            # Si l'utilisateur a appuyé sur Envoyer sans texte
            st.warning("Veuillez écrire un message avant d'envoyer.")

    st.caption("Chancy AI | Projet de Chance Bahati")

except Exception as e:
    # Friendly message shown to users
    st.error("Error running app. If this keeps happening, please contact support.")
    if DEBUG:
        # Show detailed exception in debug mode only
        st.exception(e)
    # Optional: write the traceback to a local file for diagnostics (commented out by default)
    # import traceback
    # with open('/tmp/chancy_error.log', 'a') as f:
    #     f.write(traceback.format_exc())
