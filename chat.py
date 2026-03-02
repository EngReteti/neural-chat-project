def start_chat():
    print("Chatbot: Hello! I am your AI assistant. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
            
        # This is where we will add AI logic later
        print(f"Chatbot: You said '{user_input}'. That's interesting!")

if __name__ == "__main__":
    start_chat()
