import socket
import logging
from time import time

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(client_ip)s - - [%(asctime)s +0000] "%(method)s %(url)s HTTP/1.1" %(http_status)s %(response_size)s', "%d/%b/%Y:%H:%M:%S")
    file_handler = logging.FileHandler("server.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def handle_request(request: str, ip: str):
    request_lines = request.split('\r\n')
    request_line = request_lines[0]

    if len(request_line.split(" ")) < 3:
        return bad_request(ip)

    path = request_line.split(" ")[1].strip()

    if path == "/" or path == "":
        path = "index.html"

    return write_response(path, ip)

def bad_request(ip: str):
    logger = get_logger("server")
    log_item = {
        "client_ip": ip,
        "method": "GET",
        "url": "N/A",
        "http_status": "400 Bad Request",
        "response_size": len("400")
    }
    logger.log(logging.INFO, msg="", extra=log_item)
    response = f"HTTP/1.1 400 Bad Request \r\nDate: {time()}\r\nContent-Length: {len('400')}\r\nContent-Type: text/html; charset=ISO-8859-1\r\n\r\n400 Bad Request"
    return response

def load_html(name: str) -> str:
    try:
        with open(f"./{name}", "r") as file:
            return file.read()
    except:
        return "404"  

def write_response(path: str, ip: str) -> str:
    html = load_html(path)
    
    if html == "404":
        return not_found_response(path, ip)
    
    logger = get_logger("server")
    log_item = {
        "client_ip": ip,
        "method": "GET",
        "url": path,
        "http_status": "200 OK",
        "response_size": len(html)
    }
    logger.log(logging.INFO, msg="", extra=log_item)

    response = f"HTTP/1.1 200 OK \r\nDate: {time()}\r\nContent-Length: {len(html)}\r\nContent-Type: text/html; charset=ISO-8859-1\r\n\r\n{html}"
    return response

def not_found_response(path: str, ip: str):
    html = "404 Not Found"
    logger = get_logger("server")
    log_item = {
        "client_ip": ip,
        "method": "GET",
        "url": path,
        "http_status": "404 Not Found",
        "response_size": len(html)
    }
    logger.log(logging.INFO, msg="", extra=log_item)
    response = f"HTTP/1.1 404 Not Found \r\nDate: {time()}\r\nContent-Length: {len(html)}\r\nContent-Type: text/html; charset=ISO-8859-1\r\n\r\n{html}"
    return response

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
