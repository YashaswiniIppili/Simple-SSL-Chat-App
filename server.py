import socket
import ssl
import threading

class Server:
    def __init__(self):
        self.host = 'localhost'
        self.port = 8080
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.ssl_context.load_cert_chain(certfile="cert.pem")

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.server_socket.accept()
            client_socket = self.ssl_context.wrap_socket(client_socket, server_side=True)
            print(f"New client connected: {client_address}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received message from client: {data.decode()}")
                message = input("Enter response: ")
                client_socket.sendall(message.encode())
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()


if __name__ == '__main__':
    server = Server()
    server.start_server()
