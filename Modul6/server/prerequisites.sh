#!/bin/bash
# ==============================================
# PYTHON SERVER PREREQUISITES INSTALLATION SCRIPT
# ==============================================

# System Update
echo "[1/4] Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Package Installation
echo "[2/4] Installing required packages..."
sudo apt install -y \
	python3 \
	python3-pip \
	tcpdump \
	net-tools \
	openssh-server \
	ufw

# SSH Setup
echo "[3/4] Configuring SSH service..."
sudo systemctl enable --now ssh

# Firewall Configuration
echo "[4/4] Setting up firewall rules..."
sudo ufw allow 22/tcp comment 'SSH Access'
sudo ufw allow 15151/tcp comment 'TCP Server'
sudo ufw allow 16161/udp comment 'UDP Server'
sudo ufw enable

# Verification
echo -e "\n=== INSTALLATION COMPLETE ==="
echo "Python: $(python3 --version 2>&1)"
echo "Pip: $(pip3 --version 2>&1)"
echo "SSH: $(sudo systemctl is-active ssh)"
echo -e "\nFIREWALL STATUS:"
sudo ufw status numbered

echo -e "\nPorts opened:"
echo "- 22/tcp (SSH)"
echo "- 15151/tcp (TCP Server)"
echo "- 16161/udp (UDP Server)"
echo "=============================="
