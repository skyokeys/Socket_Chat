import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    return server_socket


command = input()
if command == 'start server' or 'ss':
    i = 0
    server_host = '0.0.0.0'
    server_port = 12345
    server_socket = start_server()
    server_socket.bind((server_host, server_port))
    server_socket.listen()
    print(f'[*] listening på {server_host} : {server_port}')
    client_socket, client_address = server_socket.accept()
    print('[*] a client has connect to server')
    while True:
        messenge_inc = client_socket.recv(800).decode('utf-8')
        client_socket.send(messenge_inc.encode('utf-8'))
