import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import requests, json
import os
import time
import random
import pyjokes
import wikipedia
from bs4 import BeautifulSoup
import subprocess

print("|======= A.I voice assistant =======|")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =int (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning")
        speak(" Good Morning")
    elif hour>=12 and hour<17:
        print("Good Afternoon")
        speak(" Good Afternon")
    else:
        print("Good Evening")
        speak("Good Evening")
        
    Name = ("Hi, I am your assistant JARVIS..!!")
    print(Name)
    speak(Name)
    

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)

    try:
        print("recogising....")
        query=r.recognize_google(audio,language='en-in')
        print(f"you said : {query}\n")

    except Exception as e:
        print(e)
        print("sorry unable to recogised your voice..")
        return 'None'
    return query

def coin():
    toss = ['heads','tails']
    result = toss[random.randrange(0,1)]
    print(f"It's a {result}")
    speak(f"It's a {result}")


def user():
    print("What you I call you?")
    speak("What you I call you...??")
    name = command()
    print("Welcome Mister")
    speak("Welcome Mister")
    print(name)
    speak(name)
    print("how can i help you?")
    speak("how can i help you..?")

chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\\chrome.exe"

if __name__ == '__main__':
    wishme()
    user()

       # use this 👇 code syntax to run the programs on different browsers 

       # 1) CHROME
       # webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
       # webbrowser.get(using='chrome').open('google.com')

       # 2) FIREFOX                                                              👇 enter path acc. to ur system
       #  webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\Firefox.exe"))
       # webbrowser.get(using='firefox').open('google.com')

    while True:
        query=command().lower()

        if 'open google' in query:
            print("Jarvis : opening Google...")
            speak("opening google")
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get(using='chrome').open('google.com')


        elif 'open youtube' in query:
            print("Jarvis : opening youtube...")
            speak("opening youtube")
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get(using='chrome').open('youtube.com')


        elif 'open notepad' in query:
            print("Jarvis : opening Notepad")
            speak("opening notepad")
            Note = 'C:\\Windows\\system32\\notepad.exe' #insert the path location according to ur system
            os.startfile(Note)


        elif 'open steam' in query:
            print("Jarvis : opening Steam")
            speak("opening Steam")
            Steam = "C:\\Program Files (x86)\\Steam\\Steam.exe"
            os.startfile(Steam)
        
        elif 'open chrome' in query:
            print("Jarvis : opening chrome")
            speak("opening Chrome")
            os.startfile(chrome_path)

        elif 'open spotify' in query:
            print("Jarvis : opening spotify")
            speak("opening spotify")
            spotify ="C:\\Users\\ABC\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotify)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M')
            print(strTime)
            speak(f'The time now is{strTime}')

        elif 'toss a coin' in query:
            coin()

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(f"Jarvis : {joke}")
            speak(joke)

        elif'where is' in query:

            query = query.replace("where is","")
            location = query
            print("Jarvis : Here's the location")
            speak( "here's the location")
            print(location)
            speak(location)
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get(using='chrome').open(f'https://www.google.nl/maps/place/{ location} + ')

        elif 'news' in query:

            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            news =webbrowser.get(using='chrome').open("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'play song' in query or 'play music' in query:
            print("Jarvis : Playing songs...")
            speak('playing song....')
            music_directory = "C:\\Users\\Swara\\Downloads\\Songs" #Insert ur songs file location path
            song = os.listdir(music_directory)
            s = random.choice(song)
            print(s)
            os.startfile(os.path.join(music_directory,s))


        elif 'roll a dice' in query:
            dice = ['1','2','3','4','5','6']
            num = random.choice(dice)
            print(f"Jarvis : the number is {num}")
            speak(f"the number is {num}")


        elif 'exit' in query:
            print("Jarvis : ok. I am signing off...")
            speak('ok. I am signing off..')
            exit()


        elif 'stop listening' in query:
            print("Jarvis : For how much time you want to stop jarvis?")
            speak('For how much time you want to stop jarvis.')
            stop = int(command())
            speak(f"getting muted for {stop} seconds")
            print(f"Jarvis : getting muted for {stop} seconds")
            time.sleep(stop)

        elif 'shutdown system' in query or 'shutdown computer' in query or 'shutdown' in query:
                print("do you want to shut down your system (yes/no)")
                speak("do you want to shut down your system")
                if 'yes' in query: 
                    print("Hold On a Sec ! Your system is on its way to shut down")
                    speak("Hold On a Sec ! Your system is on its way to shut down") 
                    os.system("shutdown /s /t 1") 
                elif 'no' in query:
                    query=command().lower()  

        elif 'restart system' in query or 'restart computer' in query or 'restart' in query:
                print("do you want to restart  your system (yes/no)")
                speak("do you want to restart  your system")
                if 'yes' in query:
                    print("Hold On a Sec ! Your system is on its way to restart") 
                    speak("Hold On a Sec ! Your system is on its way to restart") 
                    os.system("shutdown /s /t 1") 
                elif 'no' in query:
                    query=command().lower()   

        elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")  
            print(f"searching {query}")     
            speak(f"searching {query}")      
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get(using='chrome').open(query)
            
        elif "weather" in query:

            # base URL
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q=Mumbai,in&appid=71b9baf195fc3764ac860fb88b0abc48"

            # City Name CITY = "Hyderabad"
            print("Tell the city name")
            speak("Tell the city name")
            CITY = command()
            # API key API_KEY = "Your API Key"
            API_KEY = '71b9baf195fc3764ac860fb88b0abc48'
            # upadting the URL
            URL = BASE_URL
            # HTTP request
            response = requests.get(URL)
            # checking the status code of the request
            if response.status_code == 200:
                # getting data in the json format
                data = response.json()
                # getting the main dict block
                main = data['main']
                # getting temperature
                temperature = main['temp']
                Celcius = temperature - 273.15
                # getting the humidity
                humidity = main['humidity']
                # getting the pressure
                pressure = main['pressure']
                # weather report
                report = data['weather']
                print(f"{CITY:-^30}")
                print(f"Temperature: {Celcius}°C")
                print(f"Humidity: {humidity}%")
                print(f"Pressure: {pressure}hpa")
                print(f"Weather feels like: {report[0]['description']}")
            else:
                # showing the error message
                print("Error in the HTTP request")