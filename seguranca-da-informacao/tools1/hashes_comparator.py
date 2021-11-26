import hashlib
import os

os.chdir('D:\\MyProjects\\cursos-dio\\seguranca-da-informacao\\tools1')

file1 = 'a.txt'
file2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'The file {file1} is different from {file2}')
    print(f'The hash of {file1} is: {hash1.hexdigest()}')
    print(f'The hash of {file2} is: {hash2.hexdigest()}')
else:
    print(f'The file {file1} is equal from {file2}')
    print(f'The hashes of {file1} and {file2} are the same: {hash1.hexdigest()}')