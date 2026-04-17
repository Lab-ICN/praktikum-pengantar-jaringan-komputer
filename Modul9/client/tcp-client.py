import socket
import ssl
import os

HOST = os.getenv("TCP_HOST", "[ip server]")
PORT = int(os.getenv("TCP_PORT", "4444"))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.minimum_version = ssl.TLSVersion.TLSv1_2
context.maximum_version = ssl.TLSVersion.TLSv1_2
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
context.set_ciphers("kRSA")

print(f"Connecting to {HOST}:{PORT} with TLSv1.2 + RSA...")

try:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        ssock.connect((HOST, PORT))
        print(f"TLS cipher negotiated: {ssock.cipher()}")
        data = ssock.recv(1024)
        print(f"Data dari server: {data.decode()}")
except socket.timeout:
    print("Connection timed out. Check TCP_HOST/TCP_PORT and server reachability.")
except ConnectionRefusedError:
    print("Connection refused. Server is not listening on target host/port.")
except ssl.SSLError as err:
    print(f"TLS error: {err}")
