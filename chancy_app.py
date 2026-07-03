import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Chancy AI",
    page_icon="🤖",
    layout="centered"
)

# Mémoire de l'application
if "started" not in st.session_state:
    st.session_state.started = False

# Écran d'accueil
if not st.session_state.started:

    st.title("🤖 Chancy AI")
    st.subheader("Votre professeure personnelle de programmation")

    st.write("""
Bienvenue !

Je suis **Chancy AI**, une assistante intelligente créée par **Murhula Bahati Chance**.

Je vais vous apprendre :

- 🐍 Python
- 🌐 HTML
- 🎨 CSS
- ⚡ JavaScript
- ☕ Java
""")

    if st.button("🚀 Commencer"):
        st.session_state.started = True
        st.rerun()

# Écran de discussion
else:

    st.title("💬 Discussion avec Chancy")

    question = st.text_input("Écris ton message")

    if st.button("Envoyer"):

        if question == "":
            st.warning("Écris un message.")

        elif question.lower() == "python":
            st.success("Bonjour 👋")
            st.write("""
🐍 Python est un langage de programmation très populaire.

Il est facile à apprendre et permet de créer :
- des applications
- des sites web
- des jeux
- de l'intelligence artificielle
- de l'automatisation

Veux-tu commencer le cours de Python ?
""")

        else:
            st.info("Je suis encore en apprentissage. 😊")
