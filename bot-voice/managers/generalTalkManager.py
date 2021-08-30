import sys
sys.path.append(sys.path[0] + "/..")
import talkBot as talk
import json

def generalConversation(command):
    file = open("./generalAnswer.json", encoding='utf-8')
    #file = open("\generalAnswer.json", encoding='utf-8')
    data = json.load(file)
    communication = data["communication"]
    foundAnswer = False
    print(command)
    for i in communication:
        if i["k"].find(command) != -1 or command.find(i["k"]) != -1:
            talk.talkBot(i["a"])
            # print(i["o"])
            # if i["o"] in vars(__builtins__)
            #     talkBot(i["o"])
            foundAnswer = True
    if not foundAnswer:
        talk.talkBot("Aún no he sido programada para esa respuesta")