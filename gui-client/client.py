import socket

class Client:

    def __init__(self, port, host=socket.gethostname()):
        self.host = host
        self.port = port
        self.client = socket.socket()

    def start(self):
        print("Starting Client Socket")
        
        try:
            self.client.connect((self.host, self.port))
        except:
            print("Unable to connect...")

    def stop(self):
        stop_message = 'close'
        self.client.send(stop_message.encode())
        print("Closing connection with server...")

    def send_data(self, message):
        try:
            self.client.send(message.encode())
        except:
            print("Unable to send a message...")

if __name__ == '__main__':
    test_client = Client(port=911)
    test_client.start()

    message = ''

    while True:
        message = input("Enter a message to send: ").lower()

        test_client.send_data(message)
        
        if message == 'close':
            test_client.stop()
            break
