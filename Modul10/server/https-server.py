import os
import ssl
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HOST = os.getenv("HTTPS_BIND", "0.0.0.0")
PORT = int(os.getenv("HTTPS_PORT", "4443"))
BASE_DIR = Path(__file__).resolve().parent
CERT_FILE = BASE_DIR / "../keys/cert.pem"
KEY_FILE = BASE_DIR / "../keys/private.key"


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            body = (
                "<html><head><title>PJK HTTPS Server</title></head>"
                "<body><h1>Halo dari HTTPS server</h1>"
                "<p>Server ini berjalan dengan TLSv1.2 dan RSA key exchange.</p>"
                "</body></html>"
            ).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/health":
            body = b"ok"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        body = b"404 Not Found"
        self.send_response(404)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(f"[{self.client_address[0]}:{self.client_address[1]}] {format % args}")



def build_ssl_context() -> ssl.SSLContext:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    context.set_ciphers("kRSA")
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    return context



def main() -> None:
    httpd = ThreadingHTTPServer((HOST, PORT), RequestHandler)
    httpd.socket = build_ssl_context().wrap_socket(httpd.socket, server_side=True)
    print(f"HTTPS server listening on https://{HOST}:{PORT}")
    print(f"Using cert: {CERT_FILE}")
    print(f"Using key : {KEY_FILE}")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
