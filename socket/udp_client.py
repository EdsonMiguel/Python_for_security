import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket criado com Sucesso!!!")

host = 'localhost'
porta = 5432
mensagem =  input("Digite a mensagem: ")


try:
    s.sendto(mensagem.encode(),(host,porta))
    print("Cliente: "+ mensagem)
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Serivodr: "+dados)

finally:
    print("Cliente: Encerrando Conexao")
    s.close()


