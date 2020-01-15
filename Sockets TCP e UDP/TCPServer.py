
from socket import *
from datetime import datetime

serverPort = 2000
serverSocket = socket(AF_INET, SOCK_STREAM)

# atribui a porta ao socket criado
serverSocket.bind(('', serverPort))

# aceita conexões com no máximo um cliente na fila
serverSocket.listen(1)

print('The server is ready to receive')
while True:
    connectionSocket, clientAddress = serverSocket.accept()

	# recebe a mensagem do cliente em bytes
    mensagem = connectionSocket.recv(1024).decode()

    data_atual = datetime.now()

    dt_string = data_atual.strftime("%d/%m/%Y %H:%M:%S")

    #data_atual = date.today()

    messageDec = str(mensagem.upper())+' '+dt_string

    # envio tbm deve ser em bytes
    connectionSocket.send(messageDec.encode())

    connectionSocket.close()