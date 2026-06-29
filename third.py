def chatbot():
    print("=" * 40)
    print("🤖 Smart ChatBot")
    print("Type 'help' to see commands")
    print("Type 'bye' to exit")
    print("=" * 40)

    while True:
        user = input("\nYou: ").lower().strip()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")
        
        elif user == "how are you":
            print("Bot: I'm doing great! How about you?")
        
        elif user == "name":
            print("Bot: My name is SmartBot.")
        
        elif user == "age":
            print("Bot: I don't have an age. I'm a computer program!")
        
        elif user == "creator":
            print("Bot: I was created by a Python programmer.")
        
        elif user == "time":
            from datetime import datetime
            print("Bot:", datetime.now().strftime("%H:%M:%S"))
        
        elif user == "date":
            from datetime import datetime
            print("Bot:", datetime.now().strftime("%d-%m-%Y"))
        
        elif user == "srk":
            print("Bot: Shah Rukh Khan is known as the King of Bollywood!")
        
        elif user == "help":
            print("""
Available Commands:
- hello
- how are you
- name
- age
- creator
- time
- date
- srk
- bye
""")
        
        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break
        
        else:
            print("Bot: Sorry, I don't understand that command.")

chatbot()