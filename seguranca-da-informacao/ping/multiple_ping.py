import os #Library import (integrate programs and resources of OS)
#import time 
os.chdir('D:\\MyProjects\\cursos-dio\\seguranca-da-informacao\\ping')

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    for ip in dump:
        print('Checking the Ip:', ip)
        print('-' * 60)
        os.system(f'ping -n 5 {ip}')
        print('-' * 60)
        #time.sleep(2) #Use if you want to create a interval between queries 