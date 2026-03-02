def get_response(text):
    # A simple dictionary acting as our bot's memory
    responses = {
        "hello": "Hi there! How can I help you with AI today?",
        "name": "I am your Neural Chat project assistant.",
        "weather": "I'm stuck in Termux, but it feels like 0s and 1s in here!",
        "python": "Python is my native language. It's great for AI!"
    }
    
    # Check if any keyword exists in the user's input
    for word in responses:
        if word in text:
            return responses[word]
            
    return "I'm still learning! Try asking about 'Python' or 'your name'."

def start_chat():
    print("Chatbot: Hello! (Type 'quit' to exit)")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chat()

