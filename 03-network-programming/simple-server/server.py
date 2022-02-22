from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8009))

server_socket.listen()

received_msg = str.encode("Message received")
while True:
    conn, addr = server_socket.accept()
    print(conn, addr)
    message = conn.recv(1024)
    data = message.decode('utf-8')
    print(data)
    conn.send(received_msg)
