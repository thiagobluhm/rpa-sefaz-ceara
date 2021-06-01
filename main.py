from robo.navegador.navegador import Navegador
from robo.tarefas.tarefa_autenticacao import TarefaAutenticacao
from robo.tarefas.tmp_tarefa_ler_proceso import TmpTarefaLerProcesso

#Instanciando navegador conforme versão correta do driver.

browser = Navegador("drivers/chromedriverORIGINAL.exe").get_navegador()

#instanciando tarefa

autenticacao = TarefaAutenticacao(browser)

autenticacao.executa()

ler_proceso = TmpTarefaLerProcesso(browser)

ler_proceso.executa()