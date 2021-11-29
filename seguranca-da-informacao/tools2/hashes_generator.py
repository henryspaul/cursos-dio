import hashlib

string = input('Enter the text to be generated the hash: ')


menu = int(input(''' ##### Menu - Select the type of hash #####
                1. MD5
                2. SHA1
                3. SHA256
                4. SHA512
                Enter the chosen number: '''))

if menu == 1:
    result = hashlib.md5(string.encode('utf-8'))
    print('The md5 hash of the string is: ', result.hexdigest())
elif menu == 2:
    result = hashlib.sha1(string.encode('utf-8'))
    print('The SHA1 hash of the string is: ', result.hexdigest())
elif menu == 3:
    result = hashlib.sha256(string.encode('utf-8'))
    print('The SHA256 hash of the string is: ', result.hexdigest())
elif menu == 4:
    result = hashlib.sha512(string.encode('utf-8'))
    print('The SHA512 hash of the string is: ', result.hexdigest())
else:
    print('Invalid input, try again!')