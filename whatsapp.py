import speech_recognition
import pyttsx3
from datetime import timedelta
import pywhatkit

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)
import datetime

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
    
update = int(datetime.now()+ timedelta(minutes = 2)).strftime("%M")
strTime = int(datetime.now().strftime("%H"))

def sendMessage():
    speak("Who do you want to message, sir?")
    a = int(input('''Person 1 - 1
    Person 2 - 2: '''))
    if a == 1:
        speak("What do you want to say?")
        message = str(input("Enter your message: "))
        pywhatkit.sendwhatmsg("(enter ur number here blank for now)", message, time_hour = strTime, time_min = update)
    elif a == 2:
        pass
        