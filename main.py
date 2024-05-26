import speech_recognition as sr
import pyttsx3
import requests
import pygame
import os
from pydub import AudioSegment
from pydub.playback import play
import datetime
import wikipediaapi

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
wiki_wiki = wikipediaapi.Wikipedia('en')

# Function to speak a given text
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen and recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

# Function to perform a web search
def web_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key=YOUR_API_KEY&cx=YOUR_CX"
    response = requests.get(url)
    results = response.json().get('items', [])
    if results:
        speak(f"Here are the top results for {query}")
        for item in results[:3]:
            print(item['title'])
            speak(item['title'])
            print(item['link'])
    else:
        speak("No results found.")

# Function to play music
def play_music(file_path):
    try:
        audio = AudioSegment.from_file(file_path)
        play(audio)
        speak("Playing music.")
    except Exception as e:
        speak(f"Could not play the music. {str(e)}")

# Function to tell the current time
def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    speak(f"The current time is {current_time}")

# Function to tell the current date
def tell_date():
    today = datetime.date.today()
    speak(f"Today's date is {today}")

# Function to fetch weather information
def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    if weather_data.get("cod") != "404":
        main = weather_data["main"]
        weather_desc = weather_data["weather"][0]["description"]
        temp = main["temp"]
        speak(f"The temperature in {city} is {temp}°C with {weather_desc}.")
    else:
        speak("City not found.")

# Function to get summary from Wikipedia
def get_wikipedia_summary(topic):
    page = wiki_wiki.page(topic)
    if page.exists():
        summary = page.summary[:2000]  # Limiting summary length
        speak(summary)
    else:
        speak("Sorry, I couldn't find any information on that topic.")

# Main function to run the chatbot
def main():
    speak("Hello, I am Darvin. How can I assist you today?")
    while True:
        command = listen()
        if "search" in command:
            speak("What do you want to search for?")
            query = listen()
            if query:
                web_search(query)
        elif "play music" in command:
            speak("Please specify the path to the music file.")
            file_path = listen()
            if os.path.exists(file_path):
                play_music(file_path)
            else:
                speak("File not found. Please try again.")
        elif "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "weather" in command:
            speak("Please tell me the city name.")
            city = listen()
            if city:
                get_weather(city)
        elif "information on" in command:
            topic = command.replace("information on", "").strip()
            if topic:
                get_wikipedia_summary(topic)
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't get that. Please try again.")

if __name__ == "__main__":
    main()
