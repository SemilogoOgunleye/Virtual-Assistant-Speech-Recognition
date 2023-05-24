import json
import pyttsx3
import requests

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def latestnews():
    api_dict = {"business" : "",
            "entertainment": "",
            "health": "",
            "science": "",
            "sports": "",
            "technology": ""
}

    content = None
    url = None
    speak("Which field do you want to explore? [business] , [health] , [technology] , [sports], [entertainment], [science]")
    field = input("Type your field interest: ")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
            if url is True:
                print("url not found")
                
    news = requests.get(url).text
    news = json.loads(news)
    speak("Here's the first news")
    
    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        
        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
            
    speak("That's all")
            
    
    
    