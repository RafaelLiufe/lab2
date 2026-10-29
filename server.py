import rpyc
from rpyc.utils.server import ThreadedServer
from datetime import datetime

class Servico(rpyc.Service):
    def on_connect(self, conexao):
        print(f"{conexao} conectado.")

    def on_disconnect(self, conexao):
        print(f"{conexao} desconectado.")

    def exposed_clt(self, msg="Que horas são, mano???"):
        try:
            if msg:
                print(f"Mensagem recebida: {msg}")
                atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return atual
        except Exception as e:
            print(f"Erro: {e}")
def init():
    host = '127.0.0.1'
    porta = 8001
    
    server = ThreadedServer(Servico, hostname=host, port=porta)
    print(f"Escutando em {host}:{porta}")
    server.start()

if __name__ == "__main__":
    init()