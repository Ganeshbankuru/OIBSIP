# task is to create a simple voice assistance that runs on voice commands using respective modules of python .
# it can help with basic tasks like responding to hello , taking screenshot,opening google,youtube and search wikepedia,tell jokes
import datetime
import webbrowser
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import pyautogui
import os


# first making text to speech engine active
engine = pyttsx3.init('sapi5')  # creating an object for pyttsx3 module
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


# defining speak function to the given input text inside the function
def speak(text):
    engine.say(text)
    engine.runAndWait()


# used for taking screenshot
def screen_shot(directory, file_name):
    file_path = os.path.join(directory, file_name)
    pic = pyautogui.screenshot()
    pic.save(file_path)
    print("photo saved succesfully... in location c:/tempphotos")


# define basic wishing function for my AI
def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 11:
        speak('good morning boss')
    elif 11 <= hour < 16:
        speak('good afternoon boss')
    else:
        speak('good evening boss')


# defining listing function to listen and return string .
def listen():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        speak('in what way i can assist you')
        print('speak somthing.......')
        # recognizer.energy_threshold = 200
        recognize.adjust_for_ambient_noise(source)
        
        audio = recognize.listen(source)
        #recognize.pause_threshold = 0.5

        try:
            string = recognize.recognize_google(audio)
            print('you said : ' + string)
        except sr.UnknownValueError:
            print('could not recognize your words')
            string = ""
        except sr.RequestError as e:
            print('jarvis request error:', e)
            string = ""
    return string


def google_search(query1):
    # Construct the Google search URL
    search_url = f"https://www.google.com/search?q={query1}"

    # Open the default web browser with the Google search URL
    webbrowser.open(search_url)


# main function starting of the jarvis programme
wish()
speak('i am your personal assistant')
while True:
    # here we will give results for requested queries
    query = listen().lower()
    if query == "":
        speak("i didn't understand your words , could you please repeat them")
    elif "happy day jarvis" in query:
        speak("then happy day boss, have a great time , good bye!")
        exit(0)
    elif 'hello' in query:
        speak("hello there")
        speak('being an artificial programme , i am very pleased with your concern')
        speak('haha! am i right boss')
    elif 'wikipedia' in query:
        speak('searching wikipedia ......')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak('According to wikipedia')
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')
    elif 'open google' in query:
        webbrowser.open('google.com')
    elif 'search' in query:
        google_search(query)
    elif 'the time' in query:
        time1 = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {time1}")
    elif 'play' in query:
        song = query.replace('play', "")
        speak('playing song '+song+' on youtube ')
        pywhatkit.playonyt(song)
    elif "joke" in query:
        speak(pyjokes.get_joke())
    elif 'about yourself' in query:
        results = wikipedia.summary('about artificial intelligence jarvis', sentences=2)
        speak(results)
    elif 'bye' in query:
        speak('ok enjoy the day then')
        exit(0)
    elif 'screenshot' in query:
        directory = "C:/tempphotos"
        file_name = "screenshotjarvis.jpg"
        screen_shot(directory, file_name)
    elif 'what are you doing' in query:
        speak('nothing but waiting for you queries')
    elif 'close the window' in query:
        pyautogui.moveTo(1900,0)
        pyautogui.click()
    else :
        speak('i can not help with that case')
    speak('boss how may i help you in another way ')
