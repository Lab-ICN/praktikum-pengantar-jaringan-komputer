import socket
import os
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "../keys/cert.pem", "rb") as f:
    server_pub_key = RSA.import_key(f.read())

encrypt_cipher = PKCS1_v1_5.new(server_pub_key)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

server_host = os.getenv("UDP_HOST", "[ip server]")
server_port = int(os.getenv("UDP_PORT", "4445"))
server_address = (server_host, server_port)

print(f"UDP Client Started -> {server_host}:{server_port}")

msg = input("Pesan: ")
if not msg:
    print("No input provided. Exiting.")
else:
    try:
        encrypted = encrypt_cipher.encrypt(msg.encode())
        sock.sendto(encrypted, server_address)

        data, _ = sock.recvfrom(4096)
        decrypted_b64 = data.decode()

        print(f"Data terenkripsi (Base64):\n{decrypted_b64}\n")
    except socket.timeout:
        print("Timeout waiting for UDP response. Check UDP_HOST/UDP_PORT and server reachability.")
    except ValueError as err:
        print(f"Encryption error: {err}")
