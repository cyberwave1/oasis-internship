import speech_recognition as sr
import webbrowser
import pyttsx3
from bs4 import BeautifulSoup
import requests

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice rate
engine.setProperty('rate', 150)

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get audio input
def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand audio")
        return None

# Function to get first search result
def get_search_result(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the first search result
    result = soup.find('div', class_='g')
    if result:
        # Extract the text content
        return result.find('a').text
    else:
        return None

# Dictionary of greetings and responses
greetings = {
    "hey": "hello there, how can I assist you today?",
    "morning": "good morning to you too!",
    "hello": "hi there, what would you like to do?",
    "hi": "hey! what can I help you with today?",
    "how are you": "I'm doing well, thank you for asking! How are you?",
    "what's up": "Not much, just waiting to assist you. What can I do for you?",
    "good morning": "Good morning! What can I do for you today?",
    "good evening": "Good evening! How can I help you?",
    "good afternoon": "Good afternoon! What would you like to know?"
}

# Main loop
while True:
    # Listen for keyword activation
    text = get_audio()
    if text and "cyber" in text:
        speak("I'm listening. What would you like me to search for?")

        # Get search query
        query = get_audio()
        if query and "search" in text:
            # Perform Google search
            search_result = get_search_result(query)
            if search_result:
                speak(f"Here's the first search result for '{query}': {search_result}")
            else:
                speak(f"Sorry, couldn't find any results for '{query}'.")
        else:
            speak("Sorry, I couldn't understand your query.")
    elif text in greetings:
        speak(greetings[text])  # Respond to greetings from the dictionary
    else:
        # Not activated or not a greeting, don't speak anything this time
        pass
