import requests
import zipfile
from config.config import Config
import json
from urllib.request import urlretrieve
from win32api import GetFileVersionInfo, LOWORD, HIWORD


class ChromeDriverApi:

    ZIP_DRIVER_PATH = '../drivers/chromedriver_win32.zip'
    DRIVER_PATH = '../drivers/'

    def __init__(self):
        pass


    def update_if_driver_is_out_of_date(self):
        print("########")
        current_chrome_version = self._verifica_versao_chrome()
        recommended_chrome_driver_version = self.get_chrome_driver_version(current_chrome_version)
        if self.verify_if_driver_is_updated(recommended_chrome_driver_version):
            print("DRIVER DESATUALIZADO. INICIANDO ATUALIZAÇÃO...")
            self.download_chrome_driver_by_version(recommended_chrome_driver_version)
            self._unzip_file(self.ZIP_DRIVER_PATH, self.DRIVER_PATH)
            Config().set_driver_current_version(recommended_chrome_driver_version)
            print("ATUALIZAÇÃO DE DRIVER CONCLUÍDA.")

    #Obtem a especificação da versão do chromedriver compatível com a versão do Chrome instalada na máquina "browser_version"
    def get_chrome_driver_version(self, browser_version):
        print("OBTENDO DRIVER ADEQUADO")
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{}'.format(browser_version)
        driver_version = requests.get(url).content.decode("utf-8")
        print("DRIVER VERSÂO: ", driver_version)
        return driver_version

    #Retorna true se o driver estiver atualizado conforme a versão do browser instalada.
    def verify_if_driver_is_updated(self, recommended_drive_version):
        current_version = Config().get_driver_current_version()
        if current_version == "":
            return False
        else:
            if current_version == recommended_drive_version:
                return True
            else:
                return False

    #Baixa a verão do chromedriver conforme o parâmetro "version".
    def download_chrome_driver_by_version(self, version):
        print("INICIANDO DOWNLOAD DO DRIVER...")
        #url = 'https://chromedriver.storage.googleapis.com/index.html?path={}'.format(version)
        url = 'https://chromedriver.storage.googleapis.com/{}/chromedriver_win32.zip'.format(version)
        destination = self.ZIP_DRIVER_PATH

        download = urlretrieve(url, destination)
        print('DOWNLOAD DE DRIVER CONCLUÍDO')


    #Descompacta um arquivo no formato .zip.
    def _unzip_file(self, file_path, dest_path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(dest_path)

    #Retorna a versão isntalada do chrome.
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