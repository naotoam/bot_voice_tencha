import pyttsx3
from datetime import datetime


tenchaBot = pyttsx3.init()

def talkBot(text, language=0):
    voices = tenchaBot.getProperty("voices")    
    tenchaBot.setProperty("voice", voices[language].id)
    tenchaBot.setProperty("rate", 150)
    tenchaBot.say(text)
    tenchaBot.runAndWait()

def welcomeMessage():
    now = datetime.now()
    current_time = now.hour
    if(current_time >= 6 and current_time <= 10):
        talkBot("Buenos días Naoto. ¿Cómo estuvo su noche de sueño?")
    elif(current_time >10 and current_time <= 12):
        talkBot("Buenos días Naoto. ¿Cómo ha estado su mañana?")
    elif(current_time > 12 and current_time <= 20):
        talkBot("Buenas tardes Naoto. ¿Cómo ha estado su día?")
    elif(current_time > 20 and current_time < 6):
        talkBot("Buenas noches Naoto.")

def closingMessage():
    now = datetime.now()
    current_time = now.hour
    if(current_time >= 6 and current_time <= 12):
        talkBot("Que tengas un buen días Naoto.")
    elif(current_time > 12 and current_time <= 20):
        talkBot("Que tengas una buena tarde Naoto")
    elif(current_time > 20 and current_time < 6):
        talkBot("Buenas noches Naoto, que descanses.")   