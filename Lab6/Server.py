import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    while data.find(",,") != -1:
        data = data.replace(",,",",")
    s = data.lstrip(",").replace(" ,", ",").replace(",", ", ")
    print(s)
    conn.send(s.encode())
conn.close()