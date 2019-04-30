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
        print('From :', host, ':', post, ', ', recvData.decode('utf-8'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-i', help="host_number", required=True)

    args = parser.parse_args()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = args.i
    post = int(args.p)
    client.connect((host, post))
    print('Connected to :', host, ':', post)
    sender = threading.Thread(target=send, args=(client,))
    receiver = threading.Thread(target=receive, args=(client,))
    sender.start()
    receiver.start()
