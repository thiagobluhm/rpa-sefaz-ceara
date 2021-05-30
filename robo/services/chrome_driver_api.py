import requests


class ChromeDriverApi:
    def __init__(self, browser_version):
        chrome_driver_version = self.get_chrome_driver_version(browser_version)
        self.download_chrome_driver_by_version(chrome_driver_version)

    #Obtem a versão do chromedriver compatível com a versão do Chrome instalada na máquina "browser_version"
    def get_chrome_driver_version(self, browser_version):
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{}'.format(browser_version)
        driver_version = requests.get(url).content.decode("utf-8")
        return driver_version

    def download_chrome_driver_by_version(self, version):
        url = 'https://chromedriver.storage.googleapis.com/index.html?path={}'.format(version)
        driver = requests.get(url, allow_redirect=True)

        open('../../drivers')