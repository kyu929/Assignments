import socket
import argparse


def run_server(port=4000):
    host = ''

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)

        conn, addr = s.accept()
        msg = conn.recv(1024)
        msg.decode()
        msg = msg[::-1]
        conn.sendall(msg)
        conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo sever -p port")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-s', help="input_letter", type=str)

    args = parser.parse_args()
    run_server(port=int(args.p))
