import rpyc

def pedir():
    host = '127.0.0.1'
    porta = 8001
    
    cliente = rpyc.connect(host, porta)
    r = cliente.root.clt("Que horas são, mano???")
    print(f"resposta: {r}")
    
    cliente.close()

if __name__ == "__main__":
    pedir()