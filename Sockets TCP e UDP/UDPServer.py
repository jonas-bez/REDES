from socket import *
from datetime import datetime
serverPort = 1024
serverSocket = socket(AF_INET, SOCK_DGRAM)
#atribui a porta ao socket criado
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

data = datetime.now()

datan = data.strftime('%d/%m/%Y %H:%M')



while True:
    #recebe a mensagem do cliente em bytes
    message, clientAddress = serverSocket.recvfrom(2048)
    
    #envio tbm deve ser em bytes
    serverSocket.sendto(message.upper().join(datan), clientAddress)
