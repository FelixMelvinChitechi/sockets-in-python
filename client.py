import socket

server_ip = '127.0.0.1'
server_ip = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(server_ip, server_port)
    data = s.recv(1024)
    print(data)
    
input()
    