# Simple RuleBase ChatBot

knowledge_base = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "good morning": "Good morning! I hope you have a great day.",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! What can I do for you?",
    "how are you": "I'm doing great! Thanks for asking.",
    "how are you doing": "I'm doing well! How can I help you?",
    "nice to meet you": "Nice to meet you too!",
    "who are you": "I'm a simple rule-based chatbot.",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "Goodbye! See you next time.",
    "exit": "Goodbye! Take care.",
    "quit": "Goodbye! Have a nice day."
}


def chatbot():

    print("==========Hello! I'm a simple rulebase chatbot.==========")
    
    print("="*50)
    while True:

        user_input = input("You: ").lower().strip()

        response = knowledge_base.get(user_input,"Sorry, I don't understand that.")

        print("Bot:", response)

        if user_input in ["bye", "goodbye", "exit", "quit"]:
            break


chatbot()