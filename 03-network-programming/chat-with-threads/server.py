from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class Connection:
    def __init__(self, conn, name):
        self.conn = conn
        self.name = name


class Server:
    def __init__(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(('127.0.0.1', 8009))
        self.server_socket.listen()
        self.clients = {}
        print("Server started on port 8009")
        self.start()

    def start(self):
        while True:
            print("Waiting for new connection ...")
            conn, addr = self.server_socket.accept()
            print(conn, addr)
            name = conn.recv(1024).decode('utf-8')
            self.clients[addr] = Connection(conn, name)
            self.broadcast(name + " just joined")
            th = Thread(target=self.client_thread, args=(self.clients[addr],))
            th.start()

    def broadcast(self, msg):
        for addr in self.clients:
            client = self.clients[addr]
            client.conn.send(str.encode(msg))

    def client_thread(self, client):
        client.conn.send(str.encode("Welcome, we hope you brought some pizza."))
        while True:
            msg = client.conn.recv(1024).decode('utf-8')
            self.broadcast(client.name + ": " + msg)


if __name__ == '__main__':
    server = Server()