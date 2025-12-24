import socket
domain = "youtube.com"
try:
    ip = socket.gethostbyname(domain)
    print(f"ip address of {domain}:{ip}")
except socket.gaierror:
    print(f"could not resolve {domain}")