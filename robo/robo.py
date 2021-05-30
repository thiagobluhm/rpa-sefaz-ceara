from win32api import GetFileVersionInfo, LOWORD, HIWORD
from robo.services.chrome_driver_api import ChromeDriverApi
#from services.chrome_driver_api import ChromeDriverApi
#Verificacao de versão do brower instalado na máquina.
class Robo:

    def __init__(self):
        #Verificação versão do driver do navegador.
        self._verifica_versao_chrome()
        #Versão recomendada do driver
        ChromeDriverApi("91.0.4472")
        #Instanciar navegador

    def verifica_driver(self):
        pass

    def _verifica_versao_chrome(self):
        try:
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            major_and_minor = GetFileVersionInfo(chrome_path, '\\')["ProductVersionMS"]
            build = GetFileVersionInfo(chrome_path, '\\')["ProductVersionLS"]
        except:
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            major_and_minor = GetFileVersionInfo(chrome_path, '\\')["ProductVersionMS"]
            build = GetFileVersionInfo(chrome_path, '\\')["ProductVersionLS"]

        #print(f"{HIWORD(major_and_minor)}.{LOWORD(major_and_minor)}.{HIWORD(build)}.{LOWORD(build)}")
        return f"{HIWORD(major_and_minor)}.{LOWORD(major_and_minor)}"
        return f
