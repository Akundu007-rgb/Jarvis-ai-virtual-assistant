import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import os
from pathlib import Path
from dotenv import load_dotenv

try:
    from groq import Groq
except ImportError:
    Groq = None

def load_env():
    env_path = Path(__file__).parent / '.env'
    load_dotenv(dotenv_path=env_path, override=True)
    print(f"[main] Loaded .env from {env_path}, GROQ_API_KEY set: {bool(os.getenv('GROQ_API_KEY'))}")

# Load environment variables from .env file (explicitly specify path)
load_env()

# Initialize Groq client (will be set at runtime)
groq_client = None

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "pub_0c777691d7144bf5a41ca6b1d81d54f6"

def aiProcess(command):
    """Process AI request using Groq (ChatGPT-quality responses for free)"""
    global groq_client

    load_env()
    groq_api_key = os.getenv("GROQ_API_KEY")
    print(f"[main.aiProcess] GROQ_API_KEY set: {bool(groq_api_key)}")

    if Groq is None:
        return r"Groq SDK is not installed. Activate the .venv and run: .venv\Scripts\python.exe -m pip install -r requirements.txt"

    if not groq_api_key:
        return "Groq API key not configured. Please set GROQ_API_KEY environment variable."

    if not groq_client:
        groq_client = Groq(api_key=groq_api_key)
    
    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are Jarvis, a helpful AI assistant. Provide clear, accurate, and concise answers. Answer like ChatGPT or Claude - informative and well-structured. Do not make up information."
                },
                {
                    "role": "user",
                    "content": command
                }
            ],
            model="llama-3.3-70b-versatile",
            max_tokens=1024,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Groq API error: {e}")
        return f"I encountered an error processing your request: {str(e)}"

def processCommand(c) :
    if "open google" in c.lower() :
        webbrowser.open("http://google.com")

    elif "open youtube" in c.lower() :
        webbrowser.open("http://youtube.com")

    elif "open facebook" in c.lower() :
        webbrowser.open("http://facebook.com")

    elif "open linkedin" in c.lower() :
        webbrowser.open("http://linkedin.com")

    elif c.lower().startswith("play") :
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower() :
        r = requests.get(f"https://newsdata.io/api/1/latest?apikey=pub_0c777691d7144bf5a41ca6b1d81d54f6")
        
        if r.status_code == 200 :
            # ... (rest of your successful code) ...
            data = r.json()
            articles = data.get('results',[])
            for article in articles :
                speak(article['title'])
        
        else:
            #  THIS IS THE CRITICAL DEBUGGING ADDITION 
            print(f"API Error! Status Code: {r.status_code}")
            try:
                # Try to print the API's own error message
                print(f"API Error Details: {r.json().get('results')}")
            except:
                print("Could not parse API error details.")
            
            speak("I am sorry, my connection to the news service is currently not working.")

    else :
        output = aiProcess(c)
        speak(output)



def speak(text) :
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__" :
    speak("Initializing Jarvis...")

    while True :
        # Listen for the wake word "Jarvis"
        # Obtain audio from the microphone

        r = sr.Recognizer()

        print("Recognizing...")
        try :
            with sr.Microphone() as source :
                recognizer.adjust_for_ambient_noise(source) # Reduce background noise
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            
            word = r.recognize_google(audio)
            
            if(word.lower() == "hello") :
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source :
                    recognizer.adjust_for_ambient_noise(source) # Reduce background noise
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e :
            print("Error; {0}".format(e))
