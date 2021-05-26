import eel

eel.init('src')

@eel.expose
def call_robot(task):
    if task:
        print("Iniciando Tarefa: ", task)

eel.start('index.html', size=(1000, 600))