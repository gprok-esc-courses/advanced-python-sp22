from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8009))

data = input("Message: ")

message = str.encode(data)
client_socket.send(message)

message = client_socket.recv(1024)
data = message.decode('utf-8')

print(data)

