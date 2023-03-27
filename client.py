import socket
import ssl
import threading
import tkinter as tk

class Client:
    def __init__(self):
        self.host = 'localhost'
        self.port = 8080
        self.ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        self.ssl_context.load_verify_locations("cert.pem")
        self.ssl_context.check_hostname = False
        self.root = tk.Tk()
        self.root.title("Chat Box")
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(side=tk.BOTTOM)
        self.input_box = tk.Entry(self.input_frame, width=80)
        self.input_box.pack(side=tk.LEFT, padx=5)
        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5)
        self.chat_box = tk.Text(self.root)
        self.chat_box.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.client_socket = self.ssl_context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def start_client(self):
        self.root.mainloop()

    def send_message(self):
        message = self.input_box.get()
        self.input_box.delete(0, tk.END)
        self.client_socket.sendall(message.encode('utf-8'))

    def receive_messages(self):
        try:
            self.client_socket.connect((self.host, self.port))
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')
                self.chat_box.insert(tk.END, message + '\n')  # Add a newline here
                self.chat_box.see(tk.END)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.client_socket.close()



if __name__ == '__main__':
    client = Client()
    client.start_client()
