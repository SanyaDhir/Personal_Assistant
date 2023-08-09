import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys

#for laptop to communicate with us so we give laptop a voice
#sapify is microsoft speech API
engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme(datetime):
        hour= int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("good morning")
        elif hour>12 and hour<18:
            speak("good afternon")
        else:
            speak("good evening")

        speak("Hey Sanya, Jarvis here please let me know how can i help you")
def takecommand():
    r= sr.Recognizer() #takes input from user and converts to string
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold= 1
        audio =r.listen(source)
    try:
        print("recognizing...")
        query= r.recognize_google(audio, language="en-in")
        print("user said", query)
    except Exception as e:
        print(e)
        speak("say that again please...")
        return "none"
    return query

if __name__ == '__main__':
    wishme(datetime)
    if 1:
        query= takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...please wait")
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak= ("according to wikipedia")
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open notepad' in query:
            npath= 'C:\\windows\\system32\\notepad.exe'
            os.startfile(npath)

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open calendar' in query:
            webbrowser.open(calendar.com)

        elif 'time' in query:
            strTime= datetime.datetime.now(),strftime("%h:%m:%s")
            speak(f"the time is{strTime}")
        elif 'no thanks' in query:
            speak("thank you for using me, have a good day")
sys.exit()