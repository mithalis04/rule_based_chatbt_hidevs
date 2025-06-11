from chatbot import get_response

print("Welcome to the ChatBot! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").strip().lower()
    
    if user_input in ['bye', 'exit', 'quit']:
        print("Bot: Goodbye! Have a nice day! ")
        break

    response = get_response(user_input)
    print(f"Bot: {response}")
