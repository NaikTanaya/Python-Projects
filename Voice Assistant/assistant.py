import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia
import smtplib
import os
import re
import pyautogui  # pip install pyautogui
import pyjokes  # pip install pyjokes
import webbrowser
from pyowm import OWM

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("welcome back sir!")

    hour = datetime.datetime.now().hour

    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("good evening")
    else:
        speak("good night")

    speak("Friday at your service. how can i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('emailid', 'password')
    server.sendmail(x, to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("path.jpg")


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "go offline" in query:
            quit()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'send email' in query:
            speak("whom do you want to send this email ")
            x = input("Enter the email id to whom you want to send email : ")
            speak("what should i send in email ?")
            y = input("What do you want to send in email : ")
            sendemail(x, y)
            speak("Email sent successfully")


        elif 'remember that' in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open("data.txt", "r")
            speak("you said me to remember that" + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("done")

        elif 'joke' or 'tell me a joke' in query:
            jokes()

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('https://youtube.com')

        elif 'google' or 'launch google' in query:
            speak("Here you go to Google\n")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('https://google.com')

        elif 'search on google' or "open on google" in query:
            speak('What do you want to search on Google, sir?')
            query2 = takeCommand()
            url = f'https://google.com/search?q=' + query2
            webbrowser.get().open(url)
            speak(f'Here is what I found for {query2} on google')

        elif 'find location' or 'find' in query:
            speak('Please mention location')
            q = takeCommand()
            url = f'https://google.nl/maps/place/' + q + '/&amp'
            webbrowser.get().open(url)
            speak(f'Here is the location of ' + q)


        elif 'open stackoverflow' or 'stack' or 'overflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif "joke" or "tell me a joke" in query:
            jokes()


