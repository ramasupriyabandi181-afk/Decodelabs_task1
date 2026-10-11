print("Welcome to the Rule-Based AI Chatbot!")
print("Type 'bye' or 'exit' to stop.\n")

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am fine! Thank you for asking.")

    elif user_input == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user_input == "what can you do":
        print("Bot: I can greet you and answer simple questions.")

    elif user_input == "help":
        print("Bot: Try saying hi, hello, how are you, or help.")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")