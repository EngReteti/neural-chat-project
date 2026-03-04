import random

def get_response(user_input):
    # Standardizing the input
    text = user_input.lower().strip()

    # 1. Simple Keyword Database
    greetings = ["hello", "hi", "hey"]
    bot_info = ["who are you", "your name", "what are you"]
    
    # 2. Logic: Checking for matches
    if any(word in text for word in greetings):
        return "Hello! How can I help you today?"
    
    if any(word in text for word in bot_info):
        return "I am a simple Python chatbot built in Termux!"

    if "python" in text:
        return "Python is the best language for AI development."

    # 3. Fallback: If no keywords are found
    return "I'm not sure I understand that yet. I'm still a simple bot!"

def start_chat():
    print("--- Neural Chat v1.0 (Simple) ---")
    print("Type 'exit' to stop the chat.")
    
    while True:
        user_msg = input("You: ")
        
        if user_msg.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day.")
            break
            
        response = get_response(user_msg)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chat()

