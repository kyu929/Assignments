import socket
import argparse

def run(host, port, line):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(line.encode())
        resp = s.recv(1024)
        print(resp.decode())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-i', help="host_number", required=True)
    parser.add_argument('-s', help="input_letter", type=str)

    args = parser.parse_args()

    run(host=args.i, port=int(args.p), line=str(args.s))
