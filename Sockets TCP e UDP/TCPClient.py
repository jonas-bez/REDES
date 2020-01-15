from socket import *
#'10.0.127.250'

serverName = 'localhost'
serverPort = 2000

clientSocket = socket(AF_INET, SOCK_STREAM)

# input() espera uma entrada do teclado para formar a msg
messagem = input('Digite uma mensagem: ')

# inicia conexao
clientSocket.connect((serverName, serverPort))


while messagem != "sair":
	
	clientSocket = socket(AF_INET, SOCK_STREAM)

	# input() espera uma entrada do teclado para formar a msg
	messagem = input('Digite uma mensagem: ')

	# inicia conexao
	clientSocket.connect((serverName, serverPort))

	# envia a msg.
	clientSocket.send(messagem.encode())

	# recebe a msg.
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

	messageDec = modifiedMessage.decode()

	# imprime a msg recebida do servidor
	print('RESPOSTA: ', messageDec)
# fecha o socket
clientSocket.close()
