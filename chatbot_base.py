import nltk
from nltk.chat.util import Chat, reflections

# Definir pares de entrada e resposta
class ChatBotBase:
    def __init__(self, pairs):
        self.chatbot = Chat(pairs, reflections)

    def start_chat(self):
        print("Olá! Digite algo para começar a conversa. (Digite 'tchau' para encerrar)")
        while True:
            user_input = input("> ")
            if user_input.lower() == "tchau":
                print("Até logo!")
                break
            response = self.chatbot.respond(user_input)
            if response:
                print(response)
            else:
                print("Desculpe, não entendi. Pode repetir?")
