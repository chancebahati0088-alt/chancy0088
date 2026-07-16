def get_response(message):

    message = message.lower().strip()

    greetings = [
        "bonjour",
        "salut",
        "coucou",
        "hello",
        "hi",
        "hey",
        "bonsoir",
        "good morning",
        "good afternoon",
        "good evening",
        "bonne journée",
        "bonne nuit",
        "ça va",
        "ca va",
        "comment vas-tu",
        "comment allez-vous",
        "yo",
        "wesh"
    ]

    thanks = [
        "merci",
        "merci beaucoup",
        "thanks",
        "thank you"
    ]

    bye = [
        "au revoir",
        "bye",
        "à bientôt",
        "a bientôt",
        "à plus",
        "a plus",
        "goodbye"
    ]

    if any(word in message for word in greetings):
        return (
            "👋 Bonjour ! Je suis Chancy AI.\n\n"
            "Je suis votre assistante personnelle en programmation.\n"
            "Comment puis-je vous aider aujourd'hui ?"
        )

    elif any(word in message for word in thanks):
        return (
            "😊 Avec plaisir !\n\n"
            "Je suis toujours prête à vous aider."
        )

    elif any(word in message for word in bye):
        return (
            "👋 Au revoir !\n\n"
            "Passez une excellente journée et bon codage. 💜"
        )

    elif "qui es-tu" in message or "qui est tu" in message:
        return (
            "Je suis Chancy AI, votre assistante personnelle en programmation.\n"
            "Je peux vous accompagner pour apprendre Python, HTML, CSS, JavaScript et bien d'autres technologies."
        )

    elif "python" in message:
        return (
            "🐍 Python est un langage simple, puissant et idéal pour débuter la programmation."
        )

    else:
        return (
            "🤖 Je suis encore en cours de développement.\n"
            "Bientôt, je pourrai répondre à beaucoup plus de questions."
        )
