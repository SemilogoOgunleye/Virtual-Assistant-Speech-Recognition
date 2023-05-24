import pyttsx3
import datetime
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
        
    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print("{query}\n")
        query = query.replace("aria", "")
    except:
        print("Sorry, I didnt get that")
        return "None"
    return query

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")
    speak("What would you like to be referred to as?")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    speak("How can I be of assistance?")
        
        