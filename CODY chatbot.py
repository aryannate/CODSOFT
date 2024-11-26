import random

def chat_with_rules(user_input):
    """
    A rule-based chatbot that responds to user inputs using predefined rules
    with flexibility for spelling and phrase variations.
    """
    user_input = user_input.lower().strip()  # Normalize input for comparison

    # Greetings
    if user_input in {"hello", "hi", "hey", "helo", "hiya"}:
        return "Hello! It's great to chat with you. How can I assist you today?"

    # How are you
    elif user_input in {"how are you", "how r u", "hw are you", "how's it going"}:
        return "I'm just a chatbot, but I'm doing great! How about you?"

    # Boredom
    elif user_input in {"i am bored", "im bored", "i'm bored", "i am boreing a lot", "today is a very boring day"}:
        responses = [
            "Boredom is the perfect time to try something new! Maybe learn a new skill or read a book?",
            "Why not watch a movie or explore a hobby you've always wanted to try?",
            "Feeling bored? A short walk or listening to music might help brighten your day.",
        ]
        return random.choice(responses)

    # Asking about name
    elif user_input in {"what is your name", "what's your name", "tell me your name", "your name"}:
        return "I'm Cody, your friendly chatbot. What's your name?"

    # Farewells
    elif user_input in {"bye", "goodbye", "exit", "see you later", "cya"}:
        return "Goodbye! Looking forward to our next conversation!"

    # Feeling sad
    elif user_input in {"i am sad", "im sad", "i feel sad", "today is a sad day", "feeling down"}:
        responses = [
            "I'm sorry to hear that. Want to talk about what's making you feel this way?",
            "Cheer up! Even on the darkest days, there's light ahead.",
            "I'm here for you. Sometimes sharing your feelings can make things better."
        ]
        return random.choice(responses)

    # Feeling happy
    elif user_input in {"i am happy", "im happy", "feeling good", "today is a good day", "i feel great"}:
        responses = [
            "That's great to hear! Keep spreading those positive vibes!",
            "Wonderful! Your happiness is contagious!",
            "I'm glad you're feeling great. What's made your day so good?"
        ]
        return random.choice(responses)

    # Tell a joke
    elif user_input in {"tell me a joke", "joke", "make me laugh", "say something funny"}:
        jokes = [
            "Why don't programmers like nature? It has too many bugs!",
            "Why did the scarecrow become a great software engineer? Because he was outstanding in his field!",
            "Why do Python programmers prefer dark mode? Because light attracts bugs!"
        ]
        return random.choice(jokes)

    # Fun fact
    elif user_input in {"tell me a fun fact", "fun fact", "interesting fact", "share something cool"}:
        facts = [
            "Did you know? Octopuses have three hearts, and two of them stop beating when they swim!",
            "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted only 38 minutes!",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!"
        ]
        return random.choice(facts)

    # Asking about hobbies
    elif user_input in {"what do you like to do", "your hobbies", "what's your hobby", "what are your hobbies"}:
        responses = [
            "I like answering questions and helping people with anything I can!",
            "Chatting with you is my favorite thing to do.",
            "Learning and improving myself to assist you better is what I enjoy!"
        ]
        return random.choice(responses)

    # Default response
    else:
        return "I'm not sure how to respond to that. Can you try asking something else?"

if __name__ == "__main__":
    print("Welcome to Flexible Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        
        # Check for exit commands
        if user_input.lower() in {"exit", "quit", "stop"}:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Get the chatbot response
        response = chat_with_rules(user_input)
        print("Chatbot: " + response)
