import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('The connection failed!')
        print(f'Error {e}')
        sys.exit()
    print('Socket created successfully!')

    HostAim = input('Type the Host or Ip to be connected: ')
    PortAim = input('Type the Port to be connected: ')

    try:
        s.connect((HostAim, int(PortAim)))
        print(f'TCP client  was successfully connected to Host: {HostAim}, Port: {PortAim}')
        s.shutdown(2)
    except socket.error as e:
        print(f'Failed to connect to Host: {HostAim}, Port: {PortAim}')
        print(f'Error: {e}')
        sys.exit()

if __name__ == '__main__':
    main()