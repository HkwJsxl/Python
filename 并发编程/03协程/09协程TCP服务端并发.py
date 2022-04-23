from gevent import spawn
from gevent import monkey

monkey.patch_all()

import socket


def communication(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data)
        except Exception as e:
            print(e)
            break
    conn.close()


def service(ip, port):
    server = socket.socket()
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        spawn(communication, conn)


if __name__ == '__main__':
    g = spawn(service('127.0.0.1', 6789))
