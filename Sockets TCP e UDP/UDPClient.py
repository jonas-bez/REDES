from socket import *
serverName = 'localhost'


a = "cabare da leila"

serverPort = 1024

clientSocket = socket(AF_INET, SOCK_DGRAM)

#a mensagem deve estar em bytes antes de ser enviada ao buffer de transmissão
clientSocket.sendto(a.encode(),(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)


#devemos converter a mensagem de volta para string antes de imprimí-la
print(modifiedMessage.decode())



#fecha a conexão
clientSocket.close()

