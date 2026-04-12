from socket import *

serverPort = 16161
serverSocket = socket(AF_INET, SOCK_DGRAM)  # IPv4 + UDP
serverSocket.bind(('0.0.0.0', serverPort))  
print("The server is ready to receive")

while True:
    try:
        message, clientAddress = serverSocket.recvfrom(2048)  # Receive the datagram from client
        decoded_msg = message.decode()
        print(f"FROM {clientAddress}: {decoded_msg}")
        
        response = decoded_msg.upper().encode()
        serverSocket.sendto(response, clientAddress)  
        print(f"REPLY: {response.decode()}")

    except Exception as e:
        print(f"Error: {e}")
