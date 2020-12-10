import hashlib

file1 = './hash_comparator/file1.txt'
file2 = './hash_comparator/file2.txt'

print("-"*60)


hash1 = hashlib.new('ripemd160')
hash1.update(open(file1,'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file2,'rb').read())


if hash1.digest() != hash2.digest():
    print("Arquivos Diferentes")
    print(f'O arquivo {file1} não é identico ao {file2}')
    print(f'Arquivo 1: {hash1.digest()}')
    print(f'Arquivo 2: {hash2.digest()}')
else:
    print("Arquivos iguais")
    print(f'O arquivo {file1} é identico ao {file2}')
    print(f'Arquivo 1: {hash1.digest()}')
    print(f'Arquivo 2: {hash2.digest()}')