import re

def get_response(user_input):
    patterns = {
        r'hi|hello|hey': "Hello! How can I help you?",
        r'how are you': "I'm a bot, but I'm functioning well!",
        r'what is your name': "I am ChatBot 1.0",
        r'bye': "Goodbye! Have a nice day!"
    }

    for pattern, response in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "Sorry, I don't understand that."
