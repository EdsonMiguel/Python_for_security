import socket 

s =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket Criado com Sucesso!!!")

host = "localhost"
porta = 5432

s.bind((host, porta))
mensagem = input("Digitte a mensagem: ")

while 1:
    dados, end = s.recvfrom(4096)
    if dados:
        print("Servidor enviando mensagem...")
        s.sendto((mensagem.encode()), end)
