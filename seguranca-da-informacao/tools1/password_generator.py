import random
import string

length = int(input('Enter the password length you want: '))

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;_:/\?'
rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(length)))