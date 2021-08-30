import sys
sys.path.append(sys.path[0] + "/..")

import googleApps.tasks as googleTasks
import toolBox as tb
import talkBot as talk
from datetime import datetime as dt

lists = googleTasks.getLists()

tasksToday = []
tasksFuture = []
def getTotalTasks():
    taskBotId = tb.searchElement(lists, "title", "Bot")["id"]
    tasks = googleTasks.getTasks(taskBotId)
    #print(tasks["items"])
    nTasks = len(tasks)
    #talk.talkBot("El número de tareas que tiene pendiente son "+str(nTasks))

    counterToday = 0
    counterFuture = 0
    for t in tasks["items"]:
        today = dt.today()
        dateFull = dt.strptime(t["due"], '%Y-%m-%dT%H:%M:%S.%fZ')
        if(today.day == dateFull.day):
            tasksToday.append(t)
            counterToday += 1
        else:
            tasksFuture.append(t)
            counterFuture += 1
    talk.talkBot("El número de tareas que tiene para hoy son "+str(counterToday))
def describeTodayTask():
    task = {}
    #print(tasksToday)
    for t in tasksToday:
        talk.talkBot("La tarea "+t["title"])
        if(t["notes"] is not None and len(t["notes"]) > 0):
            talk.talkBot("Tiene como detalle: "+t["notes"])
        else:
            talk.talkBot("No tiene detalles")
   
def insertTask(title, details, dueDate):
    response = googleTasks.insertTask("YzJzNTJ3RkNJLW1sYUVfQQ", title, dueDate, details)
    if(response["id"] is not None):
        talk.talkBot("La tarea "+title+" la he añadido a tus tareas")
    else:
        talk.talkBot("Se ha generado un error para el ingreso de la tarea")

def updateTaskToCompleted(taskId):
    response = googleTasks.updateTaskToCompleted("YzJzNTJ3RkNJLW1sYUVfQQ", taskId)
    if(response["stats"] == "completed"):
        talk.talkBot("La tarea "+response["title"]+" ha sido completada")
    else:
         talk.talkBot("Se ha generado un error para la actualización de la tarea")

