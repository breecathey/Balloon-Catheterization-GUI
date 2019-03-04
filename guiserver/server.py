import socket
import threading

from queue import Queue

class Server:

    def __init__(self, port, host=socket.gethostname()):
        self.host = host
        self.port = port

    def start(self, queue):
        print("Starting Server Socket")
        self.server = socket.socket()
        self.server.bind((self.host, self.port))
        self.server.listen(5)

        (self.connection, self.address) = self.server.accept()
        print("Connection established with client...")

        self.server_thread = threading.Thread(target=self.listen, args=(self.connection, self.address, queue))
        self.server_thread.start()

    def stop(self):
        print("Closing connection with client...")
        self.server_thread.join()
        self.connection.close()

    def receive_data(self, connection, address, queue):
        message = connection.recv(1024)

        queue.put(message)
        
        return message

    def listen(self, connection, address, queue):
        while True:
            message = self.receive_data(connection, address, queue)

            if message == b'close':
                break

if __name__ == '__main__':
    queue = Queue()

    test_server = Server(port=911)
    test_server.start(queue)

    message = ''

    while True:
        if not queue.empty():
            message = queue.get()
            print(message)

            if message == b'close':
                break

    test_server.stop()