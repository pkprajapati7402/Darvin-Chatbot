# 🎙️ Darvin: Your Voice-Activated Chatbot

Darvin is a Python-based voice-activated chatbot designed to interact with users through voice commands. It can perform web searches, play music, tell the time and date, fetch weather information, and provide Wikipedia summaries. 

## 🚀 Features

- Voice interaction using microphone and speaker
- Perform web searches
- Play music from a specified file path
- Tell the current time and date
- Fetch weather information for a specified city
- Provide summaries from Wikipedia

## 📦 Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/pkprajapati7402/darvin-chatbot.git
   cd darvin-chatbot
   ```

2. **Install Required Dependencies:**

   ```bash
   pip install speechrecognition pyttsx3 pygame requests pydub wikipedia-api
   ```

3. **API Keys:**
   - Replace `YOUR_API_KEY` and `YOUR_CX` in the `web_search` function with your Google Custom Search API key and search engine ID.
   - Replace `YOUR_OPENWEATHERMAP_API_KEY` in the `get_weather` function with your OpenWeatherMap API key.

## 🛠️ Usage

1. **Run the Program:**

   ```bash
   python main.py
   ```

2. **Interact with Darvin:**
   - **Search the Web:** Say "search for [query]" and Darvin will perform a web search.
   - **Play Music:** Say "play music" and provide the file path to play music.
   - **Get Time:** Say "what is the time" to get the current time.
   - **Get Date:** Say "what is the date" to get today's date.
   - **Get Weather:** Say "what's the weather in [city]" to get the current weather information for a specified city.
   - **Wikipedia Summary:** Say "information on [topic]" to get a summary from Wikipedia.
   - **Exit:** Say "exit" or "stop" to end the interaction.

## 📄 Example Commands

```plaintext
User: search for Python programming
Darvin: Here are the top results for Python programming...

User: play music
Darvin: Please specify the path to the music file.
User: /path/to/your/musicfile.mp3
Darvin: Playing music...

User: what is the time
Darvin: The current time is 14:30.

User: what is the date
Darvin: Today's date is 2024-05-26.

User: what's the weather in New York
Darvin: The temperature in New York is 22°C with clear sky.

User: information on Artificial Intelligence
Darvin: [Provides a summary about Artificial Intelligence from Wikipedia]
```

## 📂 File Structure

```plaintext
darvin-chatbot/
│
├── main.py         # The main script to run the chatbot
├── secret.key      # The secret key file (if any)
└── README.md       # This README file
```

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


---

Made with ❤️ by [Prince](https://github.com/pkprajapati7402)

---
