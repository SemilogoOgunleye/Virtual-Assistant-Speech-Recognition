import datetime
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import pyautogui
import os
import random
import webbrowser
from time import sleep
import pyaudio
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

for i in range(3):
    a = input("Enter your password: ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    
    if (a==pw):
        speak("Access granted")
        sleep(0.5)
        ass_id = ("aria")
        speak(f"Hi, I am your virtual assistant, {ass_id}")
        break
    elif (i==2 and a!=pw):
        exit()
        
    elif (a!=pw):
        speak("Access denied")

    
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
        print(f"You said: {query}\n")
        query = query.replace("aria", "")
    except Exception as e:
        print("Sorry, I didnt get that")
        return "None"
    return query

    
def alarm(query):
    timehere = open("alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    

    
    
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greetme import greetMe
            greetMe()
            while True:
                query = takeCommand().lower()
                if "do not disturb" in query:
                    speak('sleeping')
                    break
                      
                elif 'hello assistant' in query or f'hello, {ass_id}' in query:
                    speak('Hello Sir, what you saying?')
                elif ('blessed' in query) or ('calm' in query) or ('good' in query):
                    speak('Say less')
                    speak('That\'s great!')
                elif ('what you saying though' in query) or ('how far') in query or ('how are you' in query):
                    speak('blessed by the grace!')
                elif 'we thank God' in query:
                    speak('All glory to God!')
                     
                elif "classics" in query:
                    speak("Playing some gospel classics")
                    a = (1,2,3,4,5)
                    b = random(a)
                      
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=XCOnRwDOI1c")
                    elif b == 2:
                        webbrowser.open("https://www.youtube.com/watch?v=Q1pGnCkt1M0")
                    elif b == 3:
                        webbrowser.open("https://www.youtube.com/watch?v=silyrvtxzFM")
                    elif b == 4:
                        webbrowser.open("https://www.youtube.com/watch?v=mC-zw0zCCtg")
                    elif b == 5:
                        webbrowser.open("https://www.youtube.com/watch?v=OvHtFPZLQj0")
                  
                elif "play" in query:
                    speak("Playing...")
                    pyautogui.press("k")
                      
                elif "pause" in query:
                    speak("Muting")
                    pyautogui.press("k")
                    speak("Video muted")
                      
                elif "mute" in query:
                    speak("Pausing...")
                    pyautogui.press("m")
                    speak("Video paused")
                    
                elif "increase volume" in query:
                    speak("Volume increasing")
                    from keyboard import volumeup
                    volumeup()
                      
                elif "decrease volume" in query:
                    speak("Volume decreasing")
                    from keyboard import volumedown
                    volumedown()
                      
                elif 'open' in query:
                    from dictapp import openappweb
                    openappweb(query)
                elif 'close' in query:
                    from dictapp import closeappweb
                    closeappweb(query)
                      
                      
                elif 'google' in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif 'youtube' in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif 'wikipedia' in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                      
                      
                elif "news" in query:
                    from newsread import latestnews
                    latestnews()
                          
                elif "calculate" in query:
                    from calculator import WolframAlpha
                    from calculator import Calc
                    query = query.replace("calculate", "")
                    query = query.replace("aria", "")
                    Calc(query)
                      
                elif "whatsapp" in query:
                    from whatsapp import sendMessage
                    sendMessage()
                      
                      
                elif 'temperature' in query:
                    search = "temperature in the Rochester"
                    url = f'https://www.google.co.uk/search?q={search}'
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"Current weather {search} is {temp}")
                
                elif "weather" in query:
                    search = "temperature in the Rochester"
                    url = f'https://www.google.co.uk/search?q={search}'
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"Current weather {search} is {temp}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 30")
                    speak("For what time sir?")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Alarm set, sir")
                  

                elif 'the time' in query:
                    strftime = datetime.datetime.now(strftime("%H:%M"))
                    speak(f"{strftime} sir")
                elif 'offline mode' in query:
                    speak('System going offline')
                    exit()
                      
                elif "remind me" in query:
                    rememberMessage = query.replace("aria", "")
                    rememberMessage = query.replace("remind me to", "")
                    rememberMessage = query.replace("set a reminder to", "")
                    speak("Your remimder is set to" + rememberMessage)
                    remember = open("reminder.txt", "a")
                    remember.write(rememberMessage) 
                    remember.close()
                elif "reminders" in query:
                    remember = open("reminder.txt", "r")
                    speak("You said I should remind you to" + remember.read())
                 
                  
                  
                elif "shutdown" in query:
                    speak("Are you sure you want to shutdown sir?")
                    shutdown = (input("Do you wish to proceed? (yes/no)"))
                    if shutdown == "yes":
                        speak("proceeding...")
                        os.system("shutdown /s /t 1")
                          
                    elif shutdown == "no":
                        speak("cancelling...")
                        break
                      
                      
                          
                      
                     
                  
                      
                      
            
        
        
        
    