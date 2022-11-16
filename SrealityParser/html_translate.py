import socket
from fast_html import create_html


def port_run(apartments):
    # Define socket host, port and create socket
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8085

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)

    for row in apartments:
        row["img_url"] = f'<img src="{row["img_url"]}" width="160 height="120">'
    while True:
        print('#######################################')
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024).decode()
        response = f'HTTP/1.0 200 OK\n\n{create_html(apartments)}'
        client_connection.sendall(response.encode("windows-1250"))
        client_connection.close()

    #server_socket.close()