import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour <12:
        speak("Good Morning Umang")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Umang")
    else:
        speak("Good Evening Umang ")

    speak("I am Jarvis Mam, how may I help you")



def takeCommand():
    # It takes microphone input from the user and returns string output
    #Recognizing Voice
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        # (if we stop in between then don't complete the command)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please ")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Please Wait, Searching Wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            speak("Done Mam")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Done Mam")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak("Done Mam")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Done Mam")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Done Mam")

        elif 'play music' in query:
            music_dir='C:\\Users\\Umang\\Music\\mymusic'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[2]))
            speak("Done Mam")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam , the time is {strTime}")

        elif 'open vs code' in query:
            code_path = "C:\\Users\\Umang\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            speak("Done Mam")

        elif 'open photos' in query:
            code_path2 = "C:\\Users\\Umang\\Pictures"
            os.startfile(code_path2)
            speak("Done Mam")

        elif 'good job' in query:
            speak("Thankyou Mam")
