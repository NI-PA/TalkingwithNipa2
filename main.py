import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from selenium import webdriver

//node run

listener=sr.Recognizer( )
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command( ):
    try:
        with sr.Microphone() as source:
            print('listening...' )
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'nipa' in command:
                command = command.replace('nipa', ' ')
                print(command)
    except:
        pass
    return command


def run_nipa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', ' ')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif'hello' in command:
        print('Hello!!')
        talk("Hello")
        talk('How are you!')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who the person is' in command:
        person = command.replace('who the person is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'search' in command:
        googlesearch = command.replace('search',' ')
        browser = webdriver.Chrome('chromedriver.exe')
        for i in range(1):
            elements = browser.get("http://www.google.com/search?q=" + googlesearch + "&start" + str(i))
            print(elements)
            talk(elements)
    elif 'what' in command:
        googlesearch = command.replace('what',' ')
        browser = webdriver.Chrome('chromedriver.exe')
        for i in range(1):
            elements = browser.get("http://www.google.com/search?q=" + googlesearch + "&start" + str(i))
            print(elements)
            talk(elements)
    elif 'how' in command:
        googlesearch = command.replace('how',' ')
        browser = webdriver.Chrome('chromedriver.exe')
        for i in range(1):
            elements = browser.get("http://www.google.com/search?q=" + googlesearch + "&start" + str(i))
            print(elements)
            talk(elements)
    elif 'when' in command:
        googlesearch = command.replace('when',' ')
        browser = webdriver.Chrome('chromedriver.exe')
        for i in range(1):
            elements = browser.get("http://www.google.com/search?q=" + googlesearch + "&start" + str(i))
            print(elements)
            talk(elements)
    elif 'who' in command:
        googlesearch = command.replace('wh0',' ')
        browser = webdriver.Chrome('chromedriver.exe')
        for i in range(1):
            elements = browser.get("http://www.google.com/search?q=" + googlesearch + "&start" + str(i))
            print(elements)
            talk(elements)
    elif 'goodbye' in command:
        print('See you Soon !')
        talk("Will miss you")
        talk('good bye')
        quit()
    else:
        talk('Please say the command again.')


while True:
    run_nipa()
