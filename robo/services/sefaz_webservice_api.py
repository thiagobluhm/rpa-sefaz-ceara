import requests

class SefazWebServiceApi:
    URL = url = "http://www3.sefaz.ce.gov.br/cadastro-webservice/services/ContribuinteService/consultarContribuintePorCodigoTodasSituacoes/2/{}"
    #Consulta um cnpj no WebService da Sefaz.
    # def __consulta_cnpj(self):


    def consulta_cnpj(self, cnpj):
        cnpjCorrigido = self.__trata_cnpj(cnpj)
        url_consulta = SefazWebServiceApi.URL.format(cnpjCorrigido)
        res = requests.get(url_consulta).json()
        if 'msg' in res:
            raise Exception("CNPJ não encontrado na consulta ao WebService Sefaz.")
        return res

    def __trata_cnpj(self, cnpj):
        cnpj = cnpj.replace(".", "")
        cnpj = cnpj.replace("/", "")
        cnpj = cnpj.replace("-", "")
        cnpj = cnpj.replace("@", "")
        cnpj = cnpj.replace(" ", "")
        return cnpj

obj = SefazWebServiceApi()
a = obj.consulta_cnpj("47960950091330")

print(a)
