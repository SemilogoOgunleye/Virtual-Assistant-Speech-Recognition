import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def WolframAlpha(query):
    apikey = 'WAEYYG-E2E58LYAPX'
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)
    
    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("Null value, sir")

def Calc(query):
    Term = Term.replace("aria", "")
    Term = Term.replace("multiply", "")
    Term = Term.replace("add", "")
    Term = Term.replace("divided by", "/")
    Term = Term.replace("minus", "-")
    Term = Term.replace("times", "")
    Term = Term.replace("take away", "-")
    
    Final = str(Term)
    try:
        result = WolframAlpha(Final)
        print(f"{result}")
        speak(result)
        
    except:
        speak("This is a null value")
    
    
    
    
    
    
    
    