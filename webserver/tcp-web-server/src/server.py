import socket
from handlers.request_handler import handle_request
import time

def start_server(host='127.0.0.1', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Server listening on {host}:{port}')

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Connection from {addr}')
        handle_client(client_socket, addr[0])

def handle_client(client_socket, ip):
    request = client_socket.recv(1024).decode()

    response = handle_request(request, ip)
    client_socket.sendall(response.encode())    
    client_socket.close()

if __name__ == '__main__':
    start_server()