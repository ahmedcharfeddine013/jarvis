import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import random
import string

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)


def greeting():
    speak("Hello mister Ahmed Charfeddine")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("say it again please")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 5874)
    server.ehlo()
    server.starttls()
    server.login("ahmedcharfeddine75@gmail.com", "Raszeby013*")
    server.sendmail("ahmedcharfeddine75@gmail.com", to, content)
    server.close()


def generate_random_name(length=5):
    # """Generate a random name for saving images."""
    letters_and_digits = string.ascii_letters + string.digits
    return "".join(random.choice(letters_and_digits) for _ in range(length))


def screenshot():
    img = pyautogui.screenshot()
    imgName = generate_random_name()
    img.save("screenshot/" + imgName + ".png")


if __name__ == "__main__":
    greeting()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "stupid" in query:
            speak("i am sorry mister Ahmed Charfeddine")
        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should i say ?")
                content = takeCommand()
                to = "ahmedcharfeddine75@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("sorry there was an error")
        # elif "in Chrome":
        #     speak("what should i search?")
        #     chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        #     search = takeCommand().lower()
        #     wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        # elif 'play songs' in query:
        #     songs_dir = ''
        elif "remember that" in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said to me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("you said me to remember that" + remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Screenshot done!")
        elif "offline" in query:
            speak("Sorry to leave you mister Ahmed Charfeddine")
            quit()
