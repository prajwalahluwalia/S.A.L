import datetime
import os
import smtplib
import webbrowser
from typing import List, Any, Union

import pyttsx3
import speech_recognition as sr
import wikipedia

# import contact_importer
from speech_recognition import AudioData

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning Sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good aftrnoon sir")
    else:
        speak("Good evening sir")

    speak("My name is S.A.L, my master says i am a good listener, How may i help you?")


def takeCommand():
    # listens to user...
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Yes Sir?")
        r.pause_threshold=1
        '''r.energy_threshold = 400

        # check out other type of threshold for
        # that just hover over threshold text and click on mouse with 
        # ctrl button'''

        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You wanted: {query} \n")

    except Exception as e:
        # print(e)-----This is the error that occured

        print("Sorry, i dont recognize")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # comand sent to email server to identify itself when connecting to another email.
    server.starttls()  # encrypts connection
    server.ehlo()
    server.login('prajuaa0321@gmail.com', 'odzjybwvdsvlmlgf')
    server.sendmail('prajuaa0321@gmail.com', 'prajwalahluwalia03@gmail.com', content)

    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        # Logic for executing wiki
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime} \n")


        elif 'email to prajwal' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "prajuaa0321@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                speak("Email not sent")

        elif 'open charm' in query:              #open costomizable operation
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.2\\bin"
            os.startfile(codePath)

        elif 'open code' in query:              #open costomizable operation
            codePath = ("C:\\Program Files\\Microsoft VS Code\\Code.exe")
            os.startfile(codePath)

        elif 'open eclipse' in query:              #open costomizable operation
            codePath = ("C:\\Users\\Prajwal AhluWalia\\eclipse\\java-2019-063\\eclipse\\eclipse.exe")
            os.startfile(codePath)







'''#EXTRA FEATURES
elif 'play music' in query:
#speak("Do you want it from youtube")
music_dir = "place where songs are'
songs = os.listdir(music_dir)
print(songs)
os.startfile(os.path.join(music_dir, songs[0]))


        ****enhancements shuffle using random function
            display list of songs pause, next, previous  '''
