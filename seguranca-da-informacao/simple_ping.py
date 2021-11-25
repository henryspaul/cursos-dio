import os #Library import (integrate programs and resources from OS)

ip_ou_host = input('Type the Ip or Host to be checked: ')
print('-' * 60)
os.system('ping -n 10 {}'.format(ip_ou_host))
print('-' * 60)