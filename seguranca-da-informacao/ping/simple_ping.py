import os #Library import (integrate programs and resources of OS)

ip_ou_host = input('Type the Ip or Host to be checked: ') 
#Creating the variable that receives an Ip or Host from the user
print('-' * 60)
os.system(f'ping -n 10 {ip_ou_host}') #Calling the system method from library OS - ping command 
#-n = number of packages
print('-' * 60)