"""
Perfect version of code according to pylint module
"""
import os
import random
import msvcrt
from cryptography.fernet import Fernet

def write_key():
    """
    Creates a key to encrypt passwords
    """
    my_key = Fernet.generate_key()
    with open("key.key", "wb") as file:
        file.write(my_key)

def load_key():
    """
    Load a key before using passwords file
    """
    with open('key.key', 'rb') as file:
        my_key = file.read()
    return my_key





def psswd_encode(text):
    """
    Hashes inputing password symbols while typing
    """
    print(text, end ="", flush=True)
    psswd = []
    while True:
        symbol = msvcrt.getch().decode('ASCII')
        if symbol in ('\n','\r'):
            break
        print("*", end = "", flush=True)
        psswd += str(symbol)
    password = ''.join([str(i) for i in psswd])
    print()
    return password

def core():
    """
    Contains logic and hierarchy triggering functions
    """
    while True:
        mode = input('Would you like to add a new password or view existing ones?\
(add, view, press q to quit)').lower()
        if mode == 'q':
            break

        if mode == 'add':
            add()
        elif mode == 'view':
            view()
        else:
            print('Invalid mode.')
            continue

def generate():
    """
    Generates master password for db
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',\
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',\
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@','#', '$', '%', '^','&', '*','(', ')','/','-', '+']

    nr_letters = input('How many letters would you like in your key?')
    while int(nr_letters) not in range(1,len(letters)):
        nr_letters = input(f'Please enter number of letters (1 - {len(letters)}): ')

    nr_numbers = input('How many numbers would you like in your key?')
    while int(nr_numbers) not in range(1,len(numbers)):
        nr_letters = input(f'Please enter number of numbers (1 - {len(numbers)}): ')

    nr_symbols = input('How many symbols would you like in your key?')
    while int(nr_symbols) not in range(1,len(symbols)):
        nr_letters = input(f'Please enter number of symbols (1 - {len(symbols)}): ')

    rand_letters = [letters[random.randint(0,len(letters)-1)]
    for letters[random.randint(0,len(letters)-1)] in range(0,int(nr_letters))]
    rand_symb = [symbols[random.randint(0,len(symbols)-1)]
    for symbols[random.randint(0,len(symbols)-1)] in range(0,int(nr_symbols))]
    rand_num = [numbers[random.randint(0,len(numbers)-1)]
    for numbers[random.randint(0,len(numbers)-1)] in range(0,int(nr_numbers))]
    rand_pass = rand_letters + rand_symb + rand_num
    random.shuffle(rand_pass)
    my_key = ''.join([str(i) for i in rand_pass])
    b_key = my_key.encode('ASCII')
    with open('master.key', 'wb') as file:
        file.write(fer.encrypt(b_key))
    print(f'Remember that: {my_key}')

def load_master_psswd():
    """
    Loads master password file
    """
    with open('master.key', 'rb') as file:
        my_key = file.read()
    return fer.decrypt(my_key).decode()

def add():
    """
    Adds name and password to db
    """
    name = input('Account name: ')
    password = psswd_encode("Enter password: ")

    with open('passwords.txt', 'a', encoding="utf-8") as file:
        file.write(f'{name} | {fer.encrypt(password.encode()).decode()}\n')

def view():
    """
    Views name and password from db
    """
    my_path = os.getcwd()
    if os.path.isfile(my_path+'/passwords.txt'):
        with open('passwords.txt', 'r', encoding="utf-8") as file:
            for line in file.readlines():
                data = line.rstrip()
                user, password = data.split("|")
                print("User:", user, "| Password:", fer.decrypt(password.encode()).decode())
    else:
        print("There's no saved passwords")

if __name__== "__main__":

    current_path = os.getcwd()
    if os.path.isfile(current_path+'/master.key'):
        key = load_key()
        fer = Fernet(key)
        saved_password = load_master_psswd()
        master = input('Input master password: ')
        if master == saved_password:
            core()
    else:
        print('Hello! This is first run of application.\
Create master password for your password database')
        write_key()
        key = load_key()
        fer = Fernet(key)
        generate()
        core()
