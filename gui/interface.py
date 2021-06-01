import eel
from robo.robo import Robo
from robo.services.chrome_driver_api import ChromeDriverApi
from config.config import Config
import json

eel.init('src')

@eel.expose
def call_robot(task):
    if task:
        print("CLICOU")
        a = Config().get_driver_current_version()
        print(a)
        #Checar se o driver do navegador está atualizado
        #ChromeDriverApi().update_if_driver_is_out_of_date()

        #robo = Robo()
        #print("Iniciando Tarefa: ", task)

eel.start('index.html', size=(1000, 600))