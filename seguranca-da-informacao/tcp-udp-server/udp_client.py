import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket created successfully!')

host = 'localhost'
port = 5432
message = 'Hello server'

try:
    print(f'Client: {message}')
    s.sendto(message.encode(), (host, port))# se der errado trocar para o numero da porta

    data, server = s.recvfrom(4096)
    data = data.decode()
    print(f'Client: {data}')
finally:
    print('Client: Closing the connection')
    s.close()