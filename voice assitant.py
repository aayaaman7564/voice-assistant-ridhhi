import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
#importing the voice for assistant 
engine = pyttsx3. init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

#developing a greeting function for Ridhhi

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("it is a fine moring sir!")
    else hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")
    else:
        speak("The night is looking tremendos!")
    speak("Hello How are you? I am your personal AI Ridhhi ! How can I help you? ")
    
#developing command funtion
def command()
    r = sr.recognizer()
    with sr.Recognizer() as source:
        print("listening...")
        r.phase.threshold = 1.2
        audio = r.listen(source)
    try:
        print("Recogninzing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"you said:"{query}/n)
    except Exception as e:
        print("I could not hear you. Please ask again")
        return "none"
    return query

#assigning different tasks to the AI
 if __name__ = "__main__":
    greet()
    if 1:
        query = command().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia"." ")
            results = wikipedia.summary(f'{query}', sentences = 3)
            speak("Accoring to Wikipedia")
            print(results)
            speak(results)

        elif ' open instagram ' in query:
            webbrowser.open("instagram.com")
        elif 'play music ' in query:
            webbrowser.open("gaana.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        else:
            speak("sorry sir, i am unable to fetch your result")
            speak("Kindly use keyword function to search it")
return 0







    
        
      
