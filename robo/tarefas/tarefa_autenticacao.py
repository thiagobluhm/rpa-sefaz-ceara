from robo.navegador.navegador import Navegador

#Realiza a autenticacao na plataforma Tramita
class TarefaAutenticacao:
    def __init__(self, navegador):
        self.navegador = navegador
        self.url = "https://homol2.sefaz.ce.gov.br/astra/astraLogin.do?method=prepareLogon"

    #Realiza a autenticação no tramita
    def executa(self):
        self.navegador.get(self.url)

        self.navegador.find_element_by_id('user').send_keys('009406E7')

        self.navegador.find_element_by_id('senha').send_keys('TAX7070xa!')

        self.navegador.find_element_by_css_selector("input[value='Enviar']").click()

        self.navegador.find_element_by_id("TRAMITA").click()