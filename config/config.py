import json
import os

class Config:
    CONFIG_FILE_NAME = 'config.json'
    def __init__(self):
        pass

    #Lê o arquivo de configuração e retorna seu conteúdo
    def __read_config_file(self):
        try:
            print("##########")
            print(os.path.dirname(os.path.abspath("config.json")))
            with open('/config/config.json') as json_file:
                print(json.load(json_file))

                return json.load(json_file)
        except:
            #Loggin here
            print("Não foi possível realizar a leitura do arquivo de configuração")

    #Sobrescreve o arquivo de configuração com o conteúdo do parâmetro 'data'
    def __write_on_config_file(self, data):
        try:
            with open(self.CONFIG_FILE_NAME, 'w') as outfile:
                json.dump(data, outfile)
        except:
            # Loggin here
            print("Não foi possível realizar a escrita do arquivo de configuração")

    #Retorna versão corrente do driver.
    def get_driver_current_version(self):
        data = self.__read_config_file()
        return data['driver']['current_version']

    #Altera a versão corrente do driver.
    def set_driver_current_version(self, new_version):
        data = self.__read_config_file()
        data['driver']['current_version'] = new_version
        self.__write_on_config_file(data)
