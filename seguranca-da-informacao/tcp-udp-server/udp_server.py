import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket created successfully!')

host = 'localhost'
port = 5432

s.bind((host, port))
message = 'Server: Hello Client!'

while 1:
    data, adress = s.recvfrom(4096)

    if data:
        print('Server sending message...')
        s.sendto(data + (message.encode()), adress)