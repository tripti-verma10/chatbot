import random

# List of responses
responses = [
    "I'm not sure I understand.",
    "That's a great question!",
    "I'm still learning, can you help me?",
    "That's a good point.",
    "I'm not sure about that.",
    "That's interesting, can you tell me more?"
]

# Dictionary of greetings and responses
greetings = {
    "hello": ["Hi!", "Hello!", "Hey!", "Hi there!", "Hello there!"],
    "hi": ["Hi!", "Hello!", "Hey!", "Hi there!", "Hello there!"],
    "hey": ["Hi!", "Hello!", "Hey!", "Hi there!", "Hello there!"],
    "hola": ["Hola!", "Hello!", "Hey!", "Hi there!", "Hello there!"],
    "hi there": ["Hi!", "Hello!", "Hey!", "Hi there!", "Hello there!"],
    "hello there": ["Hi!", "Hello!", "Hey!", "Hi there!", "Hello there!"]
}

# Dictionary of goodbyes and responses
goodbyes = {
    "goodbye": ["Goodbye!", "See you later!", "Bye!", "Take care!", "Have a great day!"],
    "bye": ["Goodbye!", "See you later!", "Bye!", "Take care!", "Have a great day!"],
    "see you later": ["Goodbye!", "See you later!", "Bye!", "Take care!", "Have a great day!"],
    "take care": ["Goodbye!", "See you later!", "Bye!", "Take care!", "Have a great day!"],
    "have a great day": ["Goodbye!", "See you later!", "Bye!", "Take care!", "Have a great day!"]
}

# Function to get a random response
def get_response(message):
    message = message.lower()
    words = message.split()
    for word in words:
        if word in greetings:
            return random.choice(greetings[word])
        elif word in goodbyes:
            return random.choice(goodbyes[word])
    return random.choice(responses)

# Test the chatbot
while True:
    message = input("You: ")
    response = get_response(message)
    print("Chatbot: " + response)