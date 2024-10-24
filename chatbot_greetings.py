from chatbot_base import ChatBotBase

# Pares de entrada e resposta para saudações
greeting_pairs = [
    [
        r"oi|olá|ei|e aí",
        ["Olá!", "Oi, tudo bem?", "E aí! Como posso ajudar?"]
    ],
    [
        r"qual é o seu nome?",
        ["Eu sou um chatbot criado para ajudar com informações básicas."]
    ],
    [
        r"como você está?",
        ["Estou bem, obrigado por perguntar!", "Estou ótimo, e você?"]
    ],
    [
        r"adeus|tchau",
        ["Até mais! Tenha um ótimo dia!", "Tchau, espero que nos falemos em breve."]
    ],
]

# Criar e iniciar o chatbot para saudações
if __name__ == "__main__":
    greeting_chatbot = ChatBotBase(greeting_pairs)
    greeting_chatbot.start_chat()
