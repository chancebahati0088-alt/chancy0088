"""
Chancy AI — interface de chat Streamlit professionnelle (version française)
Remplace l'UI simple par une interface moderne avec bulles, avatars, horodatage,
filtrage de contenu et bouton d'envoi stylé.

Exécution:
    streamlit run chancy_app.py
"""
import streamlit as st
import random
import time
import html
from datetime import datetime

# Configuration de la page
st.set_page_config(page_title="Chancy AI", page_icon="🤖", layout="centered")

# Mode debug (affiche les exceptions complètes si True — ne pas activer en production)
DEBUG = False

# ---------- Informations sur le créateur et données prédéfinies ----------
CREATOR = {
    "name": "Murhula Bahati Chance",
    "age": 17,
    "country": "République Démocratique du Congo",
    "province": "Sud-Kivu",
}

JOKES = [
    "Pourquoi les développeurs aiment Python ? Parce que c'est simple !",
    "J'ai essayé de dormir... mais j'avais un bug.",
    "Je suis une IA, je ne dors jamais !",
    "Pourquoi l'ordinateur était fatigué ? Il avait trop de bits à mâcher."
]

FORBIDDEN_WORDS = ["sexe", "porno", "adulte"]

# ---------- State de session ----------
if "messages" not in st.session_state:
    # messages: liste de dicts {role: "user"|"assistant"|"system", text: str, time: ISO str}
    st.session_state.messages = [
        {
            "role": "assistant",
            "text": (
                "Bonjour — je suis Chancy 🤖. Posez une question, demandez une blague "
                "ou interrogez-moi sur mon créateur."
            ),
            "time": datetime.utcnow().isoformat(),
        }
    ]
if "input" not in st.session_state:
    st.session_state.input = ""
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "started" not in st.session_state:
    st.session_state.started = True  # ouvrir directement en mode chat pour cette vue professionnelle

# ---------- Styles CSS (bulles, bouton, mise en page) ----------
st.markdown(
    """
    <style>
    /* Container width */
    .stApp > .main .block-container{
        max-width: 850px;
        padding-top: 1rem;
    }

    /* Zone de chat */
    .chancy-chat {
        background: #f7f9fb;
        border-radius: 12px;
        padding: 12px;
        box-shadow: 0 2px 8px rgba(20,20,20,0.04);
    }

    /* Bulles de message */
    .msg {
        display: flex;
        gap: 10px;
        margin: 8px 0;
        align-items: flex-end;
    }
    .msg .avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display:inline-flex;
        align-items:center;
        justify-content:center;
        font-size:20px;
    }
    .msg.user {
        justify-content: flex-end;
    }
    .bubble {
        max-width: 75%;
        padding: 10px 14px;
        border-radius: 14px;
        line-height: 1.4;
        font-size: 15px;
    }
    .bubble.assistant {
        background: linear-gradient(180deg, #ffffff, #f1f6fb);
        border: 1px solid rgba(0,0,0,0.04);
        border-bottom-left-radius: 4px;
    }
    .bubble.user {
        background: linear-gradient(90deg,#4b9cff,#2b6bff);
        color: white;
        border-bottom-right-radius: 4px;
    }
    .meta {
        font-size: 12px;
        color: #6b7280;
        margin-top: 4px;
    }

    /* Bouton envoyer moderne (style pour tous les boutons dans les forms) */
    .stButton>button {
        background: linear-gradient(90deg,#4b9cff,#2b6bff);
        color: white;
        border-radius: 999px;
        padding: 8px 18px;
        font-weight: 600;
        box-shadow: 0 6px 18px rgba(43,107,255,0.18);
        transition: transform .08s ease-in-out;
        border: none;
    }
    .stButton>button:active { transform: translateY(1px); }
    .stForm>div[data-testid="stForm"] { gap: 8px; }

    /* Style du champ texte */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 10px;
        padding: 12px;
        border: 1px solid #e6edf3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Barre latérale ----------
with st.sidebar:
    st.title("Chancy AI")
    st.write("Assistant conversationnel — version professionnelle")
    if st.button("Réinitialiser l'historique"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "text": (
                    "Historique réinitialisé. Bonjour — je suis Chancy 🤖. "
                    "Posez une question ou demandez une blague."
                ),
                "time": datetime.utcnow().isoformat(),
            }
        ]
        st.success("Historique effacé.")
        st.experimental_rerun()
    st.write("---")
    st.markdown("Créateur :")
    st.markdown(f"- **{CREATOR['name']}** — {CREATOR['age']} ans")
    st.markdown(f"- {CREATOR['province']}, {CREATOR['country']}")
    st.write("---")
    st.markdown("Conseils :")
    st.markdown("- Demandez une blague en tapant `blague`.")
    st.markdown("- Posez des questions sur le créateur ou sur l'application.")
    st.markdown("---")
    st.caption("Chancy AI | Projet de Chance Bahati")

# ---------- Fonctions utilitaires ----------
def now_iso():
    return datetime.utcnow().isoformat()

def add_message(role, text):
    st.session_state.messages.append({"role": role, "text": text, "time": now_iso()})

def sanitize_and_detect_forbidden(text):
    lower = text.lower()
    if any(w in lower for w in FORBIDDEN_WORDS):
        return None, True
    return text.strip(), False

def format_time(iso_ts):
    try:
        dt = datetime.fromisoformat(iso_ts)
        return dt.strftime("%H:%M")
    except Exception:
        return ""

def generate_response(user_text):
    """Logique de réponse simple pour la démonstration ; remplacer par un modèle/API si besoin."""
    q = user_text.lower()
    if "créateur" in q or "qui t'a créé" in q or "qui t a créé" in q or "qui t'a programmé" in q:
        return f"Mon créateur est {CREATOR['name']}."
    if "âge" in q or "age" in q:
        return f"Mon créateur a {CREATOR['age']} ans."
    if "pays" in q or "origine" in q or "d'où" in q or "d ou" in q:
        return f"Mon créateur vient de {CREATOR['country']}."
    if "province" in q or "sud-kivu" in q or "sud kivu" in q:
        return f"Il vient de la province {CREATOR['province']}."
    if any(g in q for g in ["bonjour", "salut", "coucou", "ça va", "ca va", "hey"]):
        return "Bonjour ! Je suis là pour aider — comment puis‑je vous aider aujourd'hui ?"
    if "blague" in q or "raconte" in q:
        return random.choice(JOKES)
    # repli
    return (
        "Je suis encore en développement — je comprends certains motifs simples. "
        "Pour des fonctionnalités plus avancées, pensez à connecter une API de modèle."
    )

# ---------- Interface principale ----------
st.title("Chancy AI")
st.write("Un assistant simple et moderne — tapez votre message et appuyez sur envoyer.")
st.write("---")

# Conteneur du chat
chat_container = st.container()
with chat_container:
    st.markdown('<div class="chancy-chat">', unsafe_allow_html=True)

    # Rendu des messages
    for m in st.session_state.messages:
        role = m.get("role", "assistant")
        text = m.get("text", "")
        ts = format_time(m.get("time", ""))
        # échapper le texte pour éviter l'injection HTML, conserver les sauts de ligne
        safe_text = html.escape(text).replace("\n", "<br>")
        if role == "user":
            # bulle utilisateur à droite
            st.markdown(
                f"""
                <div class="msg user" style="justify-content:flex-end;">
                  <div class="bubble user">{safe_text}</div>
                  <div style="display:flex;flex-direction:column;align-items:flex-end;">
                    <div class="avatar" title="Vous">🙋‍♂️</div>
                    <div class="meta">{ts}</div>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            # bulle assistant à gauche
            st.markdown(
                f"""
                <div class="msg assistant">
                  <div style="display:flex;flex-direction:column;align-items:flex-start;">
                    <div class="avatar" title="Chancy">🤖</div>
                    <div class="meta">{ts}</div>
                  </div>
                  <div class="bubble assistant" style="margin-left:6px">{safe_text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

# Formulaire d'entrée (conserve l'input entre reruns)
with st.form(key="chat_form", clear_on_submit=False):
    user_input = st.text_input("Écris ton message", value=st.session_state.input_text, key="input_text")
    submit = st.form_submit_button("Envoyer ➤")
    if submit:
        raw = st.session_state.input_text or ""
        sanitized, forbidden = sanitize_and_detect_forbidden(raw)
        if raw.strip() == "":
            st.warning("Veuillez écrire un message avant d'envoyer.")
        elif forbidden:
            add_message("user", raw.strip())
            add_message("assistant", "Désolé, je ne peux pas aider avec ce type de demande.")
            st.session_state.input_text = ""
            st.experimental_rerun()
        else:
            # Ajout du message utilisateur
            add_message("user", sanitized)
            # indicateur de saisie
            placeholder = st.empty()
            with placeholder.container():
                st.markdown(
                    """
                    <div style="display:flex;align-items:center;gap:10px">
                     <div class="avatar">🤖</div>
                     <div style="font-style:italic;color:#6b7280">Chancy est en train d'écrire...</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            # temporisation simulée pour l'effet conversation
            time.sleep(0.6 + min(1.0, len(sanitized) / 120.0))
            # génération de la réponse
            try:
                response = generate_response(sanitized)
            except Exception as e:
                response = "Oups — une erreur interne est survenue."
                if DEBUG:
                    response += f" ({e})"
            placeholder.empty()
            add_message("assistant", response)
            # vider le champ
            st.session_state.input_text = ""
            # re-run pour afficher le nouveau message
            st.experimental_rerun()

# Fin du fichier
