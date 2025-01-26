import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary 
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
#Pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "140499d0c57b46b2b5970ccdc15862f2"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
  
  tts = gTTS(text)
  tts.save('temp.mp3')

# Initialize Pygame's mixer
  pygame.mixer.init()

# Load the MP3 file
  pygame.mixer.music.load("temp.mp3")

# Play the MP3 file
  pygame.mixer.music.play()

# Keep the program running to allow the music to play
  while pygame.mixer.music.get_busy():
    #  pygame.time.clock().tick(10) // Need to check this line.
     pygame.mixer.music.unload()
     os.remove("temp.mp3")


def aiprocess(command):
    client=OpenAI(api_key=""), # Have to integrate OpenAI API Key here from OpenAI api.
  

    comletion=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are a virtual named JARVIS assistant, skilled in general tasks like Alexa and google cloud.,Give short response plz"},
        {'role':"user","content":command}
    ]
    )
    return comletion.choices[0].message.content


def proessCommand(c):
    if"open google" in c.lower():
        webbrowser.open("https://google.com")
       
    elif"open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif"open spotify" in c.lower():
        webbrowser.open("https://open.spotify.com")

    elif"open ai" in c.lower():
        webbrowser.open("https://chatgpt.com")

    elif"open gemini" in c.lower():
        webbrowser.open("https://gemini.google.com/app")
   
    elif"open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif 'news' in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get("articles", [])

            # print Headlines
            for article in articles:
                speak(article['title'])
    else:
        # Let OpenAi handle the request
        output = aiprocess(c)
        speak(output)
        

if __name__== "__main__":
    speak("intializing jarvis...")
while True:
    # Listen for the wake word "JARVIS"
    # obtain audio from the microphone
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
          print("Listening...")
          audio = r.listen(source, timeout=5, phrase_time_limit=1)
        word = r.recognize_google(audio)
        if(word.lower() == "jarvis"):
            speak("yes sir")
            #listen for command
            with sr.Microphone()as source:
               print("Jarvis Active...")
               audio = r.listen(source)
               command=r.recognize_google(audio)
               proessCommand(command)

    except Exception as e:
       print("Error; {0}".format(e))


