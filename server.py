import socket

server_ip = '127.0.0.1'
server_port = 5678


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((server_ip, server_port))
    print("server listening")
    s.listen(1)
    conn, addr=s.accept()
    print(f'connection established from server: {addr}')
    with conn:
        while True:
            conn.send(b'hello world')
            break