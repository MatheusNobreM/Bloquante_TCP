import threading
import sys
from socket import *

def listen_for_messages(clientSocket):
    while True:
        try:
            response = clientSocket.recv(1024).decode('utf-8')
            if not response:
                break
            if response.lower() == 'sair':
                print("\nServidor encerrou o chat")
                break

            # Limpar linha atual do terminal
            sys.stdout.write("\r" + " " * len(prompt) + "\r")
            print(f"Servidor: {response}")
            # Reimprimir o prompt para o cliente continuar digitando
            sys.stdout.write(prompt)
            sys.stdout.flush()
        except:
            break

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Conexão iniciada, digite 'sair' para encerrar")

# Thread para ouvir mensagens do servidor
listener_thread = threading.Thread(target=listen_for_messages, args=(clientSocket,))
listener_thread.start()

prompt = "Você: "

try:
    while True:
        sentence = input(prompt)
        if sentence.lower() == 'sair':
            print("Cliente encerrou o chat")
            clientSocket.send(sentence.encode('utf-8'))
            break
        clientSocket.send(sentence.encode('utf-8'))
finally:
    clientSocket.close()
    print("Conexão encerrada")
