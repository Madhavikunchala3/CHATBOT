responses = {
 "hi": "Hello!",
 "how are you": "I'm just a computer program, but I'm functioning well. How can I assist you?",
 "what's your name": "I'm a chatbot. You can call me ChatBot.",
 "bye": "Goodbye! Feel free to return if you have more questions.",
}

def get_response(user_input):
 user_input = user_input.lower() 
 if user_input in responses:
     return responses[user_input]
 else:
     return "I'm sorry, I don't understand that question."

print("ChatBot: Hi! How can I assist you today? (Type 'bye' to exit)")
while True:
 user_input = input("You: ")

 if user_input.lower() == 'bye':
     print("ChatBot: Goodbye!")
     break
 response = get_response(user_input)
 print("ChatBot:", response)
