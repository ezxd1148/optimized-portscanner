"""
main.py
"""

import socket

target = "scanme.nmap.org"
port = 10


def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        return True
    except:
        return False


if check_port(target, port):
    print(f"Port {port} is open on {target}")
else:
    print(f"Port {port} is closed on {target}")
