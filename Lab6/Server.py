import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    s = data.lstrip(",").replace(",,",",").replace(" ,", ",").replace(",", ", ")
    conn.send(s.encode())
conn.close()