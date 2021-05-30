import eel
from robo.robo import Robo

eel.init('src')

@eel.expose
def call_robot(task):
    if task:
        robo = Robo()
        #print("Iniciando Tarefa: ", task)

eel.start('index.html', size=(1000, 600))