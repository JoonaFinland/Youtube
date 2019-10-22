with open('key.txt', 'rb') as file:
    MASTER_KEY = file.read()
    print('MASTERKEY:', MASTER_KEY)
with open('pass.txt', 'rb') as file:
    MASTER_PASS = file.read()
