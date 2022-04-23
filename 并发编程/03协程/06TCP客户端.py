import socket

client = socket.socket()
client.connect(('127.0.0.1', 6789))
while True:
    client.send(b'hello world')
    data = client.recv(1024)
    print(data.decode('utf-8'))
