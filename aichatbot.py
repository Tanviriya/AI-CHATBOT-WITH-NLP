# Importing required libraries
import nltk
import random
import re  # For matching user inputs using regular expressions
from nltk.chat.util import Chat, reflections  # Using NLTK's built-in chatbot tools

# Step 1: Define basic patterns and their responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!", "Greetings!"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm just a bot, but thanks for asking!"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you."]
    ],
    [
        r"what is the weather in (.*)",
        ["I am sorry, I cannot provide real-time weather information."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", 
         "What do you call a fish with no eyes? Fsh!"]
    ],
    [
        r"recommend me a (.*)",
        ["Okay, let me see...", "Sure, I can help with that."]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day ahead."]
    ]
]

# Step 2: Custom recommendation responses for different categories
recommendations = {
    "movie": ["Inception", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction", "Spirited Away"],
    "book": ["To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Lord of the Rings", "The Hitchhiker's Guide to the Galaxy"],
    "restaurant": ["Delicious Burger Joint", "Italian Paradise", "Sushi Time", "The Spicy Taco Truck", "Vegan Delights"],
    "song": ["Bohemian Rhapsody", "Like a Rolling Stone", "Imagine", "Smells Like Teen Spirit", "What's Going On"],
    "game": ["The Legend of Zelda: Breath of the Wild", "Minecraft", "The Witcher 3", "Red Dead Redemption 2", "Portal 2"]
}

# Step 3: Function to get a recommendation from the category user requested
def provide_recommendation(category):
    """Returns a random recommendation from the selected category."""
    if category in recommendations:
        return random.choice(recommendations[category])
    else:
        return "Sorry, I don't have recommendations for that category."

# Step 4: Create a chatbot instance using the defined patterns
chatbot = Chat(pairs, reflections)

# Step 5: Function to run the chatbot
def start_chat():
    """Runs the chatbot and interacts with the user in a loop."""
    print("Hi! I'm your assistant chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()  # Make input lowercase for easier matching

        if user_input == 'quit':
            print("Goodbye! Have a great day ahead.")
            break

        response = None

        # Go through each pattern and see if it matches the user input
        for pattern, responses in pairs:
            match = re.match(pattern, user_input)
            if match:
                # If the user asked for a recommendation
                if pattern == r"recommend me a (.*)":
                    category = match.group(1).strip()
                    recommendation = provide_recommendation(category)
                    response = f"I recommend: {recommendation}"
                else:
                    # Pick a random response from the matched pattern
                    response = random.choice(responses)
                break

        # If a response was found, print it
        if response:
            print("Chatbot:", response)
        else:
            # Default response if no pattern matched
            print("Chatbot: I didn't understand that. Can you please rephrase?")

# Run the chatbot only if this script is the main file
if __name__ == "__main__":
    start_chat()
