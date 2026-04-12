<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
  
</head>
<body>
    <h1>📡 TCP/UDP Python Server</h1>

<p>This repository contains simple Python-based <strong>TCP</strong> and <strong>UDP</strong> servers and clients, designed to demonstrate basic socket communication using multithreading (for TCP) and datagram handling (for UDP). This repository is built for networking practice purposes.</p>

<hr>

<h2>📦 Prerequisites Installation</h2>

<p>Use the <code>prerequisities.sh</code> script to install all required packages and configure the system for running TCP/UDP servers.</p>

<pre><code>chmod +x prerequisities.sh
./prerequisities.sh
</code></pre>

  <p>This script performs the following:</p>
    <ul>
        <li>Updates system packages</li>
        <li>Installs Python 3, pip, tcpdump, net-tools, and OpenSSH</li>
        <li>Enables and starts SSH server</li>
        <li>Sets up firewall rules to allow:
            <ul>
                <li>22/tcp for SSH</li>
                <li>15151/tcp for TCP Server</li>
                <li>16161/udp for UDP Server</li>
            </ul>
        </li>
    </ul>

  <hr>

  <h2>⚙️ TCP Server</h2>
    <p>File: <code>tcp-server.py</code></p>
    <p>This server uses multithreading to handle multiple TCP clients concurrently on port <code>15151</code>.</p>
    <pre><code>python3 tcp-server.py</code></pre>
    <p>Functionality:</p>
    <ul>
        <li>Accepts incoming TCP connections</li>
        <li>Receives lowercase messages</li>
        <li>Sends back uppercase version of the message</li>
    </ul>
    <hr>
    <h2>📨 UDP Server</h2>
    <p>File: <code>udp-server.py</code></p>
    <p>This server listens for UDP datagrams on port <code>16161</code>.</p>
    <pre><code>python3 udp-server.py</code></pre>
    <p>Functionality:</p>
    <ul>
        <li>Receives datagrams from any UDP client</li>
        <li>Prints received messages</li>
        <li>Responds with the message converted to uppercase</li>
    </ul>
    <hr>
    <h2>📁 Folder Structure</h2>
    <pre>
pjk-tcp-udp/
├── client/
│   ├── tcp-client.py
│   └── udp-client.py
├── prerequisities.sh
├── tcp-server.py
└── udp-server.py
    </pre>
    <hr>
    <h2>🛡️ Security & Firewall</h2>
    <p>The script automatically enables <code>ufw</code> and opens the necessary ports. You can check status with:</p>
    <pre><code>sudo ufw status numbered</code></pre>

</body>
</html>
