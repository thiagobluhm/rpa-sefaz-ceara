from selenium import webdriver


class Navegador:

    OPCOES = ""
    TEMPO_DE_ESPERA_DE_LOCATION = 35

    def __init__(self, caminhoDriver):
        self.__set_opcoes()
        self.navegador = webdriver.Chrome(chrome_options=Navegador.OPCOES, executable_path=caminhoDriver)
        self.__configura_navegador()

    def get_navegador(self):
        return self.navegador

    #Realiza configurações no navegador
    def __configura_navegador(self):
        #Aguarda até 35 para que um elemento esteja disponível
        #na DOM para sofre alguma interação. Caso o elemento
        #esteja disponível antes
        self.navegador.implicitly_wait(Navegador.TEMPO_DE_ESPERA_DE_LOCATION)

    def __set_opcoes(self):
        Navegador.OPCOES = webdriver.ChromeOptions()
        Navegador.OPCOES.add_argument("ignore-certificate-errors")
        Navegador.OPCOES.add_argument("--disable-gpu")
