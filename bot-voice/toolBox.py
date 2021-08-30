import json

# Search an object by attribute and by value
def searchElement(list, attribute, value):
    for i in list:
        if i[attribute] == value:
            return  i
    return "Not found"



# Si el array está compuesto por palabras claves como:
# Buscar, wikipedia, wiki y el commando viene como, "buscar algo sobre"
# Entonces debe retornar true, ya que ha encontrado una keyword
def hasCommandKeyword(arrayName, command):
    file = open("jsonAssets/commands.json", encoding="utf-8")
    data = json.load(file)
    array = data[arrayName]
    print(array)
    for i in array:
        if i in command:
            return True
    return False

def sanitizeCommand(command):
    file = open("jsonAssets/commands.json", encoding="utf-8")
    data = json.load(file)
    probability = 0
    bestMatch = {}
    bestMatch["type"] = "not found"
    bestMatch["query"] = "not found"
    bestMatch["option"] = "not found"
    option = ""
    for i in data:
        _command = command
        option = getOption(i, command)
        times = 0
        for j in data[i]:
            if(j in _command):
                times += 1
               
                _command = _command.replace(j, "").strip()
        probability_ = times*100/len(data[i])
        if(probability_ > 0 and probability_ > probability):
            probability = probability_
            bestMatch["type"] = i
            bestMatch["query"] = _command
            bestMatch["option"] = option
    return bestMatch

def getOption(app, command):
    print(app, command)
    action = ""
    if(app == "spotify"):
        if("pausar" in command):
            action = "pausar"
        elif("siguiente" in command):
            action = "siguiente"
        elif("buscar" in command):
            action = "buscar"
        elif("iniciar" in command):
            action = "iniciar"

    return action

# a = sanitizeCommand("buscar algo sobre chile")
# print(a)