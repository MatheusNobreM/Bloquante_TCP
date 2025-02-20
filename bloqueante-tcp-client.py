from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

print("Conexão iniciada, Digite 'sair' para encerrar")

try:
    while 1:
        sentence = input('Você: ')
        if sentence.lower() == 'sair':
            print("Cliente encerrou o chat")
            clientSocket.send(sentence.encode('utf-8'))
            break

        clientSocket.send(sentence.encode('utf-8'))

        response = clientSocket.recv(1024).decode('utf-8')
        if response.lower() == 'sair':
            print("O servidor encerrou o chat")
            break
        print(f"Servidor: {response}")
finally:
    clientSocket.close()
    print("Conexão encerrada")
