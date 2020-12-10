import socket  ##Fornece acesso a placa de rede
import sys     ##Fornece váriaveis e funções 


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    except socket.error  as e: 
        print("A Conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso!")
    host_alvo =  input("Digite o Host ou Ip a ser conectado: ")
    porta_alvo =  int(input("Digite a porta a ser conectada: "))

    try:
        s.connect((host_alvo, porta_alvo))
        print("Cliente TCP conectado com Sucesso no host {ip}:{pt}".format(ip=host_alvo, pt=porta_alvo))
        s.shutdown(2)
    except socket.error as e:
        print("A Conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()



if __name__ =="__main__":
    main()
