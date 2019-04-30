import socket
import argparse
import threading


def send(sock):
    while True:
        sendData = input()
        sock.send(sendData.encode('utf-8'))


def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('From :', addr[0], ':', addr[1], ', ', recvData.decode('utf-8'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo sever -p port")
    parser.add_argument('-p', help="port_number", required=True)

    args = parser.parse_args()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', int(args.p)))
    server.listen(1)

    conn, addr = server.accept()
    print('Connected to :', addr[0], ':', addr[1])
    sender = threading.Thread(target=send, args=(conn,))
    receiver = threading.Thread(target=receive, args=(conn,))
    sender.start()
    receiver.start()


