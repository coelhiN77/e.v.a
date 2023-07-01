from requests import get
from dotenv import load_dotenv
import requests
import speech_recognition as sr
import pywhatkit as kit
import wikipedia
import pyttsx3
import datetime
import random
import webbrowser
import pyjokes
import sys
import os
import time
import cv2
import speedtest
import re

load_dotenv()
api_key = os.getenv("API_KEY")
if api_key is None:
    sys.exit("The API key was not defined correctly. Please check the .env file.")


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

desired_index = 0
for index, voice in enumerate(voices):
    if voice.name == "Microsoft Zira Desktop - English (United States)":
        desired_index = index
        break

engine.setProperty("voice", voices[desired_index].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Config Voice IA
def guidecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening now...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


greetings = [
    "Hi sir. How can I make your day better?",
    "Hi, I'm here to help. How can I be of assistance?",
    "Hi handsome, what do we have for today?" "How can I assist you today?",
    "What can I do to help you?",
    "What do you need help with?",
    "Is there anything I can do for you?",
]

helps = [
    "Sir, do you have any other work?",
    "Sir, do you need help with anything else?",
    "Sir, do you need assistance with any other matters or issues?",
    "Sir, is there something else I can help you with?",
    "Sir, is there anything else I can do for you today?",
    "Sir, are there any other matters I can attend to on your behalf?",
]


def news():
    req_url = f"http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}"

    main_page = requests.get(req_url).json()
    articles = main_page["articles"]
    head = []
    day = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
    ]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"'today's {day[i]} news is: {head[i]}")


def get_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    data = response.json()
    quote = data["content"]
    author = data["author"]
    return quote, author


def calculate(expression):
    expression = re.sub("[^0-9+\-*/().]", "", expression)
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Sorry, unable to calculate the expression."


# Config Time and Welcome
def initiate():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good Morning, its {tt}")
    elif hour > 12 and hour < 18:
        speak(f"Good Afternoon, its {tt}")
    else:
        speak(f"Good Evening, its {tt}")
    greeting = random.choice(greetings)
    speak(greeting)


if __name__ == "__main__":
    initiate()

    while True:
        if 1:
            request = guidecommand().lower()

            # Logic building for tasks here
            if "open notepad" in request:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "close notepad" in request:
                speak("Okay, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "open vscode" in request:
                speak("Opening visual studio code")
                os.system("code")

            elif "close vscode" in request:
                speak("Okay, closing visual studio code")
                os.system("taskkill /f /im code.exe")

            elif "motivational quote" in request:
                quote, author = get_quote()
                speak(quote)
                speak(f"- {author}")

            elif "my ip" in request:
                ip = get("https://api.ipify.org").text
                speak(f"your IP address is {ip}")

            elif "calculate" in request:
                speak("Sure, what is the expression?")
                expression = guidecommand().lower()
                result = calculate(expression)
                speak(f"The result is: {result}")

            elif "joke" in request:
                joke_rq = pyjokes.get_joke(language="en", category="neutral")
                speak(joke_rq)

            elif "any news" in request:
                speak("Sir, Well... let me see")
                news()

            elif "wikipedia" in request:
                speak("Searching in wikipedia...")
                request = request.place("wikipedia", "")
                results = wikipedia.summary(request, sentences=2)
                speak("according to wikipedia")
                speak(results)

            elif "open camera" in request:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow("webcam", img)
                    k = cv2.waitkey(50)
                    if k == 27:
                        break
                    cap.release()
                    cv2.destroyAllWindows()

            elif "play music" in request:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                for song in songs:
                    if song.endswith(".mp3"):
                        os.startfile(os.path.join(music_dir, song))

            elif "open prompt" in request:
                os.system("start cmd")

            elif "open email" in request:
                speak("Opening email")
                webbrowser.open("https://outlook.live.com/mail/")

            elif "open youtube" in request:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in request:
                webbrowser.open("www.facebook.com")

            elif "open twitter" in request:
                webbrowser.open("www.twitter.com")

            elif "open google" in request:
                speak("Sir, what should I search on google")
                cm = guidecommand().lower()
                webbrowser.open(f"{cm}")

            elif "play song on youtube" in request:
                kit.playonyt("see you again")

            elif "play surprise" in request:
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

            elif "send message" in request:
                kit.sendwhatmsg("+DDDANDNUMBER", "Hi, how are you?", 4, 13)
                time.sleep(120)
                speak("message has been successfully")

            elif "my sir" in request:
                webbrowser.open("https://github.com/coelhiN77")

            elif "your name" in request:
                name = "My name is EVA"
                speak(name)

            elif "my name" in request:
                creator = "Your name is coelhiN"
                speak(creator)

            elif "how old are you" in request:
                age = "I am an artificial intelligence, I don't have an age like humans"
                speak(age)

            elif "current time" in request:
                time = datetime.datetime.now().strftime("%I%M%p")
                speak(time)

            elif "bye eva" in request:
                speak("Thanks for using me sir, have a good day.")
                sys.exit()

            elif "you can sleep now" in request:
                speak("I will rest now, see you later")
                sys.exit()

            help = random.choice(helps)
            speak(help)
