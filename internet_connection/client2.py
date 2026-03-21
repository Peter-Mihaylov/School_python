import socket
HOST = '127.0.0.1'    # The remote host
PORT = 10000             # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to server: {(HOST, PORT)}")
    s.sendall(input("Enter a message:").encode())
    data = s.recv(1024)
print(f"Received: {data}")