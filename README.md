#Chat Application using SSL/TLS
This is a simple chat application that uses SSL/TLS to secure the communication between the client and the server. The application is written in Python using the socket and ssl modules.

##How it works
The application consists of two parts: the server and the client. The server listens on a specific port for incoming connections. When a client connects, the server wraps the socket in an SSL/TLS connection using a self-signed certificate. The client also uses SSL/TLS to connect to the server and verify the server's identity using the same self-signed certificate.
Once the connection is established, the client and the server can exchange messages securely. The server will print out the messages it receives from the client, and prompt the user for a response. The response is then sent back to the client.

##How to use it
Clone the repository to your local machine.
Generate a self-signed certificate using the openssl command-line tool. Save the certificate as cert.pem in the project directory.
Open a terminal and start the server by running python server.py.
Open another terminal and start the client by running python client.py.
Type a message in the client terminal and hit Enter to send it to the server.
The server will print out the message and prompt you for a response.
Type a response in the server terminal and hit Enter to send it to the client.
The client will print out the response.
Note: The client and the server must be running on the same machine for this to work.

Contributing
If you find a bug or would like to suggest an improvement, please open an issue on the GitHub repository. Pull requests are also welcome!
