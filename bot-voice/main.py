import toolBox as tb
import talkBot as talk
import managers.expressionManager as em
import managers.wikiManager as wiki
import managers.spotifyManager as spotify
import managers.generalTalkManager as general
from datetime import datetime




def runBot():
    terminate = False
    #talk.welcomeMessage()
    while(not terminate):
        command = ""
        try:
            command = em.getExpresion()
            _command = tb.sanitizeCommand(command)
            print(_command)
            type = _command["type"]
            query = _command["query"]
            option = _command["option"]
            print(type, query, option)
            #talk.talkBot(command)
            if(type == "terminar"):
                terminate = True
                talk.closingMessage()
            elif(type == "wikipedia"):
                wiki.searchWikipedia(query)
            elif(type == "spotify"):
                spotify.spotifyController(option, query)
            else:
                general.generalConversation(command)
        except Exception as e:
            print(e)
            print("An error has ocurred")      

runBot()