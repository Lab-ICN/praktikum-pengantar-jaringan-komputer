from socket import *
from threading import Thread

serverPort = 15151
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('0.0.0.0', serverPort))  
serverSocket.listen(100)  # Concurrent up to 100 connections
print('The server is ready to receive')

def handle_client(connectionSocket, addr):
    try:
        sentence = connectionSocket.recv(1024)
        print("Sender:", sentence.decode())
        connectionSocket.send(sentence.upper())
    finally:
        connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    Thread(target=handle_client, args=(connectionSocket, addr)).start()
