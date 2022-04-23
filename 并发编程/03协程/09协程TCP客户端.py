import socket
from threading import Thread, current_thread


def Client():
    client = socket.socket()
    client.connect(('127.0.0.1', 6789))
    n = 0
    while True:
        msg = '%s %s' % (current_thread().name.encode('utf-8'), n)
        n += 1
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)
        if not data: break
        print(data.decode('utf-8'))


if __name__ == '__main__':
    for i in range(100):
        t = Thread(target=Client)
        t.start()
