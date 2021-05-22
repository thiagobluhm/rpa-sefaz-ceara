class TmpTarefaLerProcesso:

    def __init__(self, navegador):
        self.navegador = navegador

    def executa(self):
        self.navegador.find_element_by_link_text("Consultar Processos").click()

        self.navegador.find_element_by_id("numeroProcesso").send_keys("10401260/2000")

        self.navegador.find_element_by_xpath("//mat-tab-body/div[1]/mat-card[1]/mat-card-content[1]/div[8]/mat-dialog-actions[1]/button[1]").click()

        self.navegador.find_element_by_xpath("//table//tbody/tr").click()

        #Obtendo CNPJ
        cnpj = self.navegador.find_element_by_xpath("//mat-tab-body/div[1]/app-detalhe-processo[1]/mat-card[1]/mat-card-content[1]/div[1]/div[2]/span[1]/p[1]").text
        print(self.__trata_cnpj(cnpj))

    def __trata_cnpj(self, cnpj):
        cnpj = cnpj.split(" ")
        cnpj = cnpj[1].replace(".", "")
        cnpj = cnpj.replace("/", "")
        cnpj = cnpj.replace("-", "")
        cnpj = cnpj.replace("@", "")
        return cnpj