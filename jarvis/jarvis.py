import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("GOOD  MORNING!")
    elif hour>= 12 and hour<18:
        speak("GOOD AFTERNOON!")
    else:
        speak("GOOD EVENING!")

    speak(" i am jarvis mam. please tell me how may i help you")


def takeCommand():
    #it takes microphones input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...........")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print('user said : {}'.format(query))
    
    except Exception as e:
        #print(e)

        print("say that again please....")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('megha20121997@gmail.com','megha1997')
    server.sendmail('megha20121997@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia..........')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
    #speak("megha ,is a good girl")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\Megha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to megha' in query:
            try:
                speak("What Should I Say?")
                content = takeCommand()
                to = "megha20121997@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend megha. i am not able to send this email...")


