st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Écris ton message…"):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    reponse = "Bonjour ! Je suis Chancy AI, votre assistante personnelle en programmation."
    st.session_state.messages.append(
        {"role": "assistant", "content": reponse}
    )

    with st.chat_message("assistant"):
        st.write(reponse)
