from chatbot_base import ChatBotBase

# Pares de entrada e resposta adicionais para conversas mais interativas
conversation_pairs = [
    [
        r"você pode me ajudar com algo?",
        ["Claro! Como posso ajudar?", "Sim, estou aqui para ajudar!"]
    ],
    [
        r"que horas são\??",
        ["Desculpe, eu não sei as horas. Mas posso ajudar com outras coisas."]
    ],
    [
        r"onde você mora?",
        ["Eu moro na nuvem, estou disponível em qualquer lugar com acesso à internet!"]
    ],
    [
        r"você gosta de música?",
        ["Sim, eu gosto de música! Qual é o seu gênero favorito?", "Eu adoro música, especialmente eletrônica!"]
    ],
]

# Criar e iniciar o chatbot para conversas mais interativas
if __name__ == "__main__":
    conversation_chatbot = ChatBotBase(conversation_pairs)
    conversation_chatbot.start_chat()

