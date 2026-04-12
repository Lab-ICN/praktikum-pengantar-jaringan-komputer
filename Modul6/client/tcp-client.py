from socket import *

serverName = '[server-ip]'
serverPort = 15151

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    sentence = input('[TCP] Input lowercase sentence: ')
    clientSocket.send(sentence.encode())

    modifiedSentence = clientSocket.recv(1024)
    print('[TCP] From Server:', modifiedSentence.decode())

except Exception as e:
    print(f"Connection error: {e}")

finally:
    clientSocket.close()
