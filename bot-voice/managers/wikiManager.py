import sys
sys.path.append(sys.path[0] + "/..")
#import speech_recognition as sr
import talkBot as talk
import wikipedia

def searchWikipedia(query):
    wikipedia.set_lang("es")
    info = wikipedia.summary(query, 1)
    talk.talkBot("Esto fue lo que encontré en wikipedia")
    talk.talkBot(info)


#searchWikipedia("Chile")