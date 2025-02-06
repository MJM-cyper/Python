from logger import get_logger
import logging
import time

def handle_request(request: str, ip: str):
    request_lines = request.split('\r\n')
    request_line = request_lines[0]
    

    line = request_line.split(" ")
    path = line[1]
    path = path.strip()


    if "/" not in path:
        logger = get_logger("server")
        log_item = {
            "client_ip": ip,
            "method": "GET",
            "url": path,
            "http_status": "400 Bad Request",
            "response_size": len("400")
        }
        logger.log(logging.INFO, msg="", extra=log_item)
        response = f"HTTP/1.1 400 bad request \r\nDate: {time.time()}\r\nContent-Length: {len("400")}\r\nContent-Type: text/html; charset=ISO-8859-1\r\n\r\n{"400"}"
        return response
    
    return write_response(path[1:], ip)


def load_html(name: str) -> str:
    
    try:
        with open(f"./handlers/{name}", "r") as file:
            
            return file.read()
    except:
        return "404" # todo: lav en 404.html page
    

def write_response(path: str, ip: str) -> str:
    log_item = {}
    logger = get_logger("server")
    html = load_html(path)
    if html == "404": # Todo format time.
        log_item = {
            "client_ip": ip,
            "method": "GET",
            "url": path,
            "http_status": "404 Not Found",
            "response_size": len("404")
        }
        response = f"HTTP/1.1 404 Not Found \r\nDate: {time.time()}\r\nContent-Length: {len(html)}\r\nContent-Type: text/html; charset=ISO-8859-1\r\n\r\n{html}"
        logger.log(logging.INFO, msg="", extra=log_item)
        return response
    
    response = f"HTTP/1.1 200 OK \r\nDate: {time.time()}\r\nContent-Length: {len(html)}\r\nContent-Type: text/html; charset=ISO-8859-1\r\n\r\n{html}"
    log_item = {
        "client_ip": ip,
        "method": "GET",
        "url": path,
        "http_status": "200 OK",
        "response_size": len(html)
    }

    logger.log(logging.INFO, msg="", extra=log_item)
    return response
    