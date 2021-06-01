from robo.services.chrome_driver_api import ChromeDriverApi
from robo.navegador.navegador import Navegador
from robo.tarefas.tarefa_autenticacao import TarefaAutenticacao
#from services.chrome_driver_api import ChromeDriverApi
#Verificacao de versão do brower instalado na máquina.
class Robo:

    def __init__(self):
        #Instanciar navegador
        browser = Navegador('../drivers/chromedriver.exe')
        #Iniciando uma tarefa para testar drive
        TarefaAutenticacao(browser).executa()


    def verifica_driver(self):
        pass


