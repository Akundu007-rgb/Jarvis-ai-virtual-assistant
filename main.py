import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "pub_0c777691d7144bf5a41ca6b1d81d54f6"

def aiProcess(command):
    try:
        # Initialize OpenAI client with your API key
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Use the user's command in the prompt
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant."},
                {"role": "user", "content": command}
            ]
        )

        # --- Output ---
        print("--- Jarvis's Response ---")
        return (completion.choices[0].message.content)

    except Exception as e:
        # This block will catch the 'insufficient_quota' error, but uses a general error message
        print(f"An error occurred during the API call: {e}")
        print("\n💡 Action Required: Please check your OpenAI billing page.")
        print("The API key likely has insufficient credit or has reached a spending limit.")

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
