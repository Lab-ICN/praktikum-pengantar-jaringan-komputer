import socket
import ssl
import os
from pathlib import Path

HOST = os.getenv("TCP_BIND", "0.0.0.0")
PORT = int(os.getenv("TCP_PORT", "4444"))
CERT_FILE = "../keys/cert.pem"
KEY_FILE = "../keys/private.key"
BASE_DIR = Path(__file__).resolve().parent

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.minimum_version = ssl.TLSVersion.TLSv1_2
context.maximum_version = ssl.TLSVersion.TLSv1_2
context.set_ciphers("kRSA")
context.load_cert_chain(certfile=BASE_DIR / CERT_FILE, keyfile=BASE_DIR / KEY_FILE)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(5)

print(f"TCP TLS server listening on {HOST}:{PORT}")

while True:
    conn, addr = sock.accept()
    print(f"Client connected: {addr}")

    try:
        with context.wrap_socket(conn, server_side=True) as tls_conn:
            print(f"TLS cipher negotiated with {addr}: {tls_conn.cipher()}")
            tls_conn.sendall(b"Halo dari TCP TLS server")
    except ssl.SSLError as err:
        print(f"TLS error from {addr}: {err}")
    except Exception as err:
        print(f"Unexpected error from {addr}: {err}")
