import socket

sock = socket.socket()
sock.connect(("localhost", 9090))
while True:
    sock.send(input("Текст: ").encode())
    data = sock.recv(1024).decode()
    print (data)

sock.close()

