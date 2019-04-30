import socket
import argparse
import threading


def run_server(port=4000):
    host = ''

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)

        msg = conn.recv(1024)
        msg.decode()
        msg = msg[::-1]

        conn.sendall(msg)
        print(addr[0], ': close')
        conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo sever -p port")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-s', help="input_letter", type=str)

    args = parser.parse_args()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', int(args.p)))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        print('Connected to :', addr[0], ':', addr[1])
        t = threading.Thread(target=run_server(), args=(conn, addr))
        t.start()
    server.cloes()

