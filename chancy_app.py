import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Chancy AI",
    page_icon="🤖",
    layout="centered"
)

# État de l'application
if "started" not in st.session_state:
    st.session_state.started = False

# Écran d'accueil
if not st.session_state.started:

    st.title("🤖 Chancy AI")

    st.subheader("Votre professeure personnelle de programmation")

    st.write(
        """
Bienvenue !

Je suis **Chancy AI**, une assistante intelligente créée par
**Murhula Bahati Chance**.

Je vais vous apprendre :

- 🐍 Python
- 🌐 HTML
- 🎨 CSS
- ⚡ JavaScript
- ☕ Java
- et bien d'autres langages.
"""
    )

    if st.button("🚀 Commencer"):
        st.session_state.started = True
        st.rerun()

# Écran du chat
else:

    st.title("💬 Discussion avec Chancy")

    question = st.text_input("Écris ton message")

    if st.button("Envoyer"):

        if question == "":
            st.warning("Écris un message.")
        else:
            st.success("Tu as écrit :")
            st.write(question)
