#import required modules

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener=sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#defining a talk function

def talk(text):
    engine.say(text)
    engine.runAndWait()

#function for commands

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening......")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'suzy' in command:
                talk(command)
    except:
        pass
    return command

def run_suzy():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who are you' in command:
        talk('Thank you for asking, i am SUZY, personal assistant developed by Ahnusha')
    else:
        talk('Please say the command again.')

while True:
    run_suzy()
