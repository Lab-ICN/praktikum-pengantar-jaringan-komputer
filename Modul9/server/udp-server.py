import base64
import socket
from pathlib import Path
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

HOST = "0.0.0.0"
PORT = 4445
BUFFER_SIZE = 4096
BASE_DIR = Path(__file__).resolve().parent


with open(BASE_DIR / "private.key", "rb") as f:
    private_key = RSA.import_key(f.read())

with open(BASE_DIR / "cert.pem", "rb") as f:
    public_key = RSA.import_key(f.read())


decrypt_cipher = PKCS1_v1_5.new(private_key)
encrypt_cipher = PKCS1_v1_5.new(public_key)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"UDP Server listening on {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)

    sentinel = get_random_bytes(32)
    decrypted = decrypt_cipher.decrypt(data, sentinel)

    if decrypted == sentinel:
        print(f"[{addr}] Failed to decrypt payload")
        sock.sendto(b"Invalid encrypted payload", addr)
        continue

    try:
        plaintext = decrypted.decode()
    except UnicodeDecodeError:
        plaintext = "<binary data>"

    print(f"[{addr}] Pesan diterima: {plaintext}")

    encrypted_response = encrypt_cipher.encrypt(decrypted)
    encrypted_response_b64 = base64.b64encode(encrypted_response)
    sock.sendto(encrypted_response_b64, addr)
