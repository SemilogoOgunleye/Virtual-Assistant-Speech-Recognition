import pyttsx3
import speech_recognition
import pywhatkit
import wikipedia
import webbrowser

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
    
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices") 
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    query = takeCommand()
    if 'google' in query:
        speak('Searching...')
        import wikipedia as googleScrap
        query = query.replace("aria", "")
        query = query.replace("google", "")
        query = query.replace("google search", "")
        speak('This is what I found')
        
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query, 1)
        speak(result)
        
    except:
        speak('I couldn\'t find the information you were looking for')

def searchYoutube(query):
    query = takeCommand()
    if 'youtube' in query:
        speak('Searching...')
        query = query.replace("youtube", "")
        query = query.replace("aria", "")
        query = query.replace("youtube search ", "")
        speak('This is what I found')
        web = 'https://www.youtube.com/results?search_query=' + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak('playing...')
        
def searchWikipedia(query):
    query = takeCommand()
    if 'wikipedia' in query:
        speak('Searching...')
        query = query.replace("wiki", "")
        query = query.replace("wiki search", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("wiki", "")
        query = query.replace("aria", "")
        result1 = wikipedia.search(query, sentences = 2)
        print(result1)
        speak(result1)
        
        
        
