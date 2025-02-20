import threading
import sys
from socket import *

def handle_client(connectionSocket, addr):
    print(f"Conexão estabelecida com {addr}")

    def listen_for_messages():
        while True:
            try:
                message = connectionSocket.recv(1024).decode('utf-8')
                if not message:
                    break
                if message.lower() == 'sair':
                    print(f"\nCliente encerrou o chat")
                    break

                # Limpar linha atual do terminal
                sys.stdout.write("\r" + " " * len(prompt) + "\r")
                print(f"Cliente : {message}")
                # Reimprimir o prompt para o servidor continuar digitando
                sys.stdout.write(prompt)
                sys.stdout.flush()
            except:
                break

    listener_thread = threading.Thread(target=listen_for_messages)
    listener_thread.start()

    try:
        while True:
            response = input(prompt)
            if response.lower() == 'sair':
                print("Servidor encerrou o chat")
                connectionSocket.send(response.encode('utf-8'))
                break
            connectionSocket.send(response.encode('utf-8'))
    finally:
        connectionSocket.close()
        print(f"Conexão com {addr} encerrada")

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)  # Suporte para múltiplas conexões
print("Servidor pronto para receber conexões")

prompt = "Você (Servidor): "

try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
        client_thread.start()
finally:
    serverSocket.close()
    print("Servidor encerrado")
