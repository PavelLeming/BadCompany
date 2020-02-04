import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
conn.send('first'.encode())

conn2, addr2 = sock.accept()
conn2.send('second'.encode())

conn.send('READY'.encode())
conn2.send('READY'.encode())

print('connected1:', addr)
print('connected2:', addr2)

while True:
    data = conn.recv(1024)
    conn2.send(data)
    print(data, 1.1)
    data = conn2.recv(1024)
    conn.send(data)
    print(data, 2.1)
    data = conn.recv(1024)
    conn2.send(data)
    data = conn.recv(1024)
    conn2.send(data)


conn.close()
conn2.close()