import socket
from threading import Thread


def communication(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data)
        except Exception as e:
            print(e)
            break


def service(ip, port):
    server = socket.socket()
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        t = Thread(target=communication, args=(conn,))
        t.start()


if __name__ == '__main__':
    t = Thread(target=service, args=('127.0.0.1', 6789,))
    t.start()
