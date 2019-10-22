# Simple command line password manager
# can have multiple users passwords, requires user and master key to login
# saves the passwords to a encrypted text file
import secrets
import hashlib
import binascii
import os
import getpass
import pickle, json
import pyperclip
from cryptography.fernet import Fernet

def password_generator(length=17):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"@#%&/()=?-_:;*'
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt+pwdhash).decode('ascii')

try:
    with open('key.txt', 'rb') as file:
        MASTER_KEY = file.read()
except FileNotFoundError:
    print('No MASTER KEY generated: generating one now:')
    key = Fernet.generate_key()
    print('Generated key:',key)
    MASTER_KEY = key
    with open('key.txt', 'wb') as file:
        file.write(MASTER_KEY)
    os.remove('stored.p') # remove passwords since stored is useless without old key
try:
    with open('pass.txt', 'r') as file:
        MASTER_PASS = file.read()
except FileNotFoundError:
    print('No MASTER USER found.')
    passw = getpass.getpass('Input master password: ')
    MASTER_PASS = hash_password(passw)
    with open('pass.txt', 'w') as file:
        file.write(MASTER_PASS)
    os.remove('stored.p') # remove passwords

def verify_password(stored_pass, given_pass):
    salt = stored_pass[:64]
    stored_pass = stored_pass[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', given_pass.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_pass

def file_to_data():
    with open('stored.p', 'rb') as file:
        data = file.read()
    fernet = Fernet(MASTER_KEY)
    decrypted = fernet.decrypt(data)
    with open('stored.p', 'wb') as file:
        file.write(decrypted)
    main = pickle_load()
    data_to_file(main)
    return main

def pickle_load():
    with open('stored.p', 'rb') as file:
        main = pickle.load(file)
    return main

def pickle_save(data):
    with open('stored.p', 'wb') as file:
        pickle.dump(data, file)

def data_to_file(data):
    pickle_save(data)
    with open('stored.p', 'rb') as file:
        data = file.read()
    fernet = Fernet(MASTER_KEY)
    encrypted = fernet.encrypt(data)
    with open('stored.p', 'wb') as file:
        file.write(encrypted)

def main():

    while True:
        master = getpass.getpass('Enter masterpassword: ')
        if verify_password(MASTER_PASS, master):
            print('Welcome to password manager V0.0.0')
            while True:
                try:
                    main_data = file_to_data()
                except FileNotFoundError:
                    main_data = {}
                choice = input('(A)dd new password, (G)et password or (C)hange password? (L)ist all Services or (Q)uit ').lower()
                if choice == 'a':
                    # add new password
                    get = input('Service name? ').lower()
                    if get not in main_data:
                        while True:
                            gen_pass = password_generator()
                            print('Generated password:',gen_pass)
                            print('Enter for continue \ Anykey for new pass')
                            if input() == '':
                                break
                        main_data[get] = gen_pass
                    else:
                        print('Service already exists')
                    data_to_file(main_data)
                elif choice == 'g':
                    # get existing password
                    get = input('Service name? ').lower()
                    if get in main_data:
                        print('Password:', main_data[get])
                        pyperclip.copy(main_data[get])
                        print('Copied to clipboard')
                    else:
                        print('Service doesn\'t exist')
                elif choice == 'c':
                    # change password
                    get = input('Service name? ').lower()
                    if get in main_data:
                        while True:
                            gen_pass = password_generator()
                            print('New password:',gen_pass)
                            print('Enter for continue \ Anykey for new pass')
                            if input() == '':
                                break
                        main_data[get] = gen_pass
                    else:
                        print('Service doesn\'t exist')
                    data_to_file(main_data)
                elif choice == 'l':
                    if len(main_data) == 0:
                        print('No Services')
                    else:
                        print('Services:',end='\n| ')
                    for name in main_data.keys():
                        print(name, end=' | ')
                    print('')
                elif choice == 'q':
                    quit()
                else:
                    print('Incorrect input')

main()
