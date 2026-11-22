from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def create_chatbot():
    """Create and train the chatbot using the English corpus."""

    chatbot = ChatBot("Assignment Bot")

    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")

    return chatbot


def main():
    """Start the terminal-based chatbot."""

    chatbot = create_chatbot()

    print("\nChatbot started. Type 'exit' to quit.\n")

    while True:
        user_input = input("user: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("bot: Goodbye!")
            break

        if not user_input:
            continue

        response = chatbot.get_response(user_input)
        print(f"bot: {response}")


if __name__ == "__main__":
    main()
