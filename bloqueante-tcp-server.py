import time
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
connectionSocket, addr = serverSocket.accept()
print(f"Conexão estabelecida com {addr}")

try:
     while 1:
          sentence = connectionSocket.recv(1024)
          text = sentence.decode('utf-8')
          if text.lower() == 'sair':
            print("Cliente encerrou o chat")
            break

          print(f"Cliente: {text}")

          response = input('Você (Servidor): ')
          connectionSocket.send(response.encode('utf-8'))

          if response.lower() == 'sair':
               print("O servidor encerrou o chat")
               break
finally:
    connectionSocket.close()
    serverSocket.close()
    print("Conexão encerrada")
