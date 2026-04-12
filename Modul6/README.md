# TCP/UDP Python Server

This repository contains simple Python-based **TCP** and **UDP** servers and clients for basic networking practice.

## Prerequisites Installation

Use [server/prerequisites.sh](server/prerequisites.sh) to install required packages and configure the system.

```bash
chmod +x server/prerequisites.sh
./server/prerequisites.sh
```

The script performs the following:

- Updates system packages
- Installs Python 3, pip, tcpdump, net-tools, and OpenSSH
- Enables and starts SSH server
- Sets up firewall rules to allow:
  - `22/tcp` for SSH
  - `15151/tcp` for TCP server
  - `16161/udp` for UDP server

## TCP Server

File: [server/tcp-server.py](server/tcp-server.py)

This server uses multithreading to handle multiple TCP clients concurrently on port `15151`.

```bash
python3 server/tcp-server.py
```

Functionality:

- Accepts incoming TCP connections
- Receives lowercase messages
- Sends back uppercase version of the message

## UDP Server

File: [server/udp-server.py](server/udp-server.py)

This server listens for UDP datagrams on port `16161`.

```bash
python3 server/udp-server.py
```

Functionality:

- Receives datagrams from any UDP client
- Prints received messages
- Responds with the message converted to uppercase

## Folder Structure

```text
Modul6/
|- README.md
|- client/
|  |- tcp-client.py
|  `- udp-client.py
|- server/
|  |- prerequisites.sh
|  |- tcp-server.py
|  `- udp-server.py
`- systemd/
   |- pjk-tcp-server.service
   `- pjk-udp-server.service
```

## Security and Firewall

The prerequisite script enables `ufw` and opens required ports.

Check firewall status:

```bash
sudo ufw status numbered
```

## Run Servers with Systemd

This repository includes ready-to-use service files:

- [systemd/pjk-tcp-server.service](systemd/pjk-tcp-server.service)
- [systemd/pjk-udp-server.service](systemd/pjk-udp-server.service)

### 1. Adjust service paths and user

Before installing, edit both files so these fields match your machine:

- `User=`
- `WorkingDirectory=`
- `ExecStart=`

Current values point to `/home/member/pjk-tcp-udp/server`, so update them if your project path is different.

### 2. Copy service files to systemd directory

```bash
sudo cp systemd/pjk-tcp-server.service /etc/systemd/system/
sudo cp systemd/pjk-udp-server.service /etc/systemd/system/
```

### 3. Reload daemon and enable services

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now pjk-tcp-server.service
sudo systemctl enable --now pjk-udp-server.service
```

### 4. Verify service status

```bash
sudo systemctl status pjk-tcp-server.service
sudo systemctl status pjk-udp-server.service
```

### 5. View logs

```bash
sudo journalctl -u pjk-tcp-server.service -f
sudo journalctl -u pjk-udp-server.service -f
```

### Optional service management

```bash
sudo systemctl restart pjk-tcp-server.service
sudo systemctl restart pjk-udp-server.service
sudo systemctl disable --now pjk-tcp-server.service
sudo systemctl disable --now pjk-udp-server.service
```
