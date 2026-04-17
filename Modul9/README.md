# Module 9 — TCP TLS + UDP RSA

## For Students (Python client only)

This section is only for running the client. You **do not need** to run the server.

### 1) Prerequisites
- Python 3.10+ (or any available Python 3 version)
- Network access to the instructor/assistant server
- The server's `cert.pem` file (required by `udp-client.py`)

### 2) Set up the client
```bash
cd client
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3) Run the TCP client (TLS v1.2 + RSA)
Set the server host/port through environment variables, then run:

```bash
export TCP_HOST=<IP_SERVER>
export TCP_PORT=4444
python3 tcp-client.py
```

On success, the output usually shows the negotiated TLS cipher and this message:
`Halo dari TCP TLS server`

### 4) Run the UDP client (RSA-encrypted message)
```bash
export UDP_HOST=<IP_SERVER>
export UDP_PORT=4445
python3 udp-client.py
```

- When prompted with `Pesan:`, type your message.
- The client will print the response in Base64 format.

### 5) Decrypt the Base64 response
```bash
python3 rsa-decrypt.py
```

Then paste the Base64 string from the UDP client output.

---

## For Instructors / Teaching Assistants

This section covers running the TCP+UDP server, including an option to run it as systemd services.

### 1) Key structure
The `keys/` folder contains:
- `cert.pem`
- `private.key`

Both files are required by the Python server and must be available in the `keys/` folder.

### 2) Install server dependencies
```bash
cd server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3) Run the server manually (quick debugging)
TCP server (default bind `0.0.0.0:4444`):
```bash
python3 tcp-server.py
```

UDP server (bind `0.0.0.0:4445`):
```bash
python3 udp-server.py
```

### 4) Configure TCP host/port (optional)
`tcp-server.py` supports these environment variables:
- `TCP_BIND` (default `0.0.0.0`)
- `TCP_PORT` (default `4444`)

Example:
```bash
TCP_BIND=0.0.0.0 TCP_PORT=4444 python3 tcp-server.py
```

### 5) Deploy as systemd services
Service unit files are available in the `systemd/` folder:
- `pjk-tcp-server-encrypted.service`
- `pjk-udp-server-encrypted.service`

> Important: the current service files use `/home/member/...` paths. Update `User`, `WorkingDirectory`, and `ExecStart` for your server.

Installation example:
```bash
sudo cp systemd/pjk-tcp-server-encrypted.service /etc/systemd/system/
sudo cp systemd/pjk-udp-server-encrypted.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now pjk-tcp-server-encrypted.service
sudo systemctl enable --now pjk-udp-server-encrypted.service
```

Check status/logs:
```bash
sudo systemctl status pjk-tcp-server-encrypted.service
sudo systemctl status pjk-udp-server-encrypted.service
sudo journalctl -u pjk-tcp-server-encrypted.service -f
sudo journalctl -u pjk-udp-server-encrypted.service -f
```
