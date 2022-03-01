import struct
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class Client:
    def __init__(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 8009))

        data = input("Your Name: ")

        message = str.encode(data)
        self.client_socket.send(message)
        th = Thread(target=self.send_msg_thread)
        th.start()

        while True:
            msg = self.client_socket.recv(1024).decode('utf-8')
            print(msg)

    def send_msg_thread(self):
        while True:
            msg = input("Say something: ")
            self.client_socket.send(str.encode(msg))


if __name__ == '__main__':
    client = Client()
