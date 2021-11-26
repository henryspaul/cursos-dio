import ipaddress

ip = '192.168.0.1'
ipnet = '192.168.0.0/24'

address = ipaddress.ip_address(ip)
print(address)

network = ipaddress.ip_network(ipnet, strict = False)
print(network)

for ipnet in network:
    print(ipnet)