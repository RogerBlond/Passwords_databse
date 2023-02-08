import os
import random
import msvcrt
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

def load_key():
    with open('key.key', 'rb') as f: 
        key = f.read()
    return key

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@','#', '$', '%', '^','&', '*','(', ')','/','-', '+']

    nr_letters = input('How many letters would you like in your key?')
    while not int(nr_letters) in range(1,len(letters)):
        nr_letters = input(f'Please enter number of letters (1 - {len(letters)}): ')

    nr_numbers = input('How many numbers would you like in your key?')
    while not int(nr_numbers) in range(1,len(numbers)):
        nr_letters = input(f'Please enter number of numbers (1 - {len(numbers)}): ')

    nr_symbols = input('How many symbols would you like in your key?')
    while not int(nr_symbols) in range(1,len(symbols)):
        nr_letters = input(f'Please enter number of symbols (1 - {len(symbols)}): ')

    rand_letters = [letters[random.randint(0,len(letters)-1)] for letters[random.randint(0,len(letters)-1)] in range(0,int(nr_letters))]
    rand_symb = [symbols[random.randint(0,len(symbols)-1)] for symbols[random.randint(0,len(symbols)-1)] in range(0,int(nr_symbols))]
    rand_num = [numbers[random.randint(0,len(numbers)-1)] for numbers[random.randint(0,len(numbers)-1)] in range(0,int(nr_numbers))]
    rand_pass = rand_letters + rand_symb + rand_num
    random.shuffle(rand_pass)
    key = ''.join([str(i) for i in rand_pass])
    b_key = key.encode('ASCII') 
    with open('master.key', 'wb') as f: #'wb' stands for binary mode
        f.write(b_key)
    print('Remember that')

def load_master_psswd():
    with open('master.key', 'rb') as f: 
        key = f.read()
    return key

def psswd_encode(text):
    print(text, end ="", flush=True)
    psswd = []
    while True:
        symbol = msvcrt.getch().decode('ASCII')
        if symbol == '\n' or symbol == '\r':    
            break
        print("*", end = "", flush=True)
        psswd += str(symbol)
    password = ''.join([str(i) for i in psswd])    
    print()
    return password

def core():
    global fer
    while True:
            
            key = load_key()
            fer = Fernet(key)

            mode = input('Would you like to add a new password or view existing ones? (add, view, press q to quit)').lower()
            if mode == 'q':
                break

            if mode == 'add':
                add()
            elif mode == 'view':
                view()                
            else:
                print('Invalid mode.')
                continue

def add():
    name = input('Account name: ')
    password = psswd_encode("Enter password: ")

    with open('passwords.txt', 'a') as f:
        f.write(f'{name} | {fer.encrypt(password.encode()).decode()}\n')

def view():
    my_path = os.getcwd()
    if os.path.isfile(my_path+'/passwords.txt'):
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, password = data.split("|")
                print("User:", user, "| Password:", fer.decrypt(password.encode()).decode())
    else:
        print("There's no saved passwords")

if __name__== "__main__":

    my_path = os.getcwd()
    if os.path.isfile(my_path+'/master.key'):   
        saved_password = load_master_psswd()
        master = input('Input master password: ')
        if master == str(saved_password.decode('ASCII')):
            core()
    else:
        print('Hello! This is first run of application. Create master password for your password database')
        write_key()
        generate()
        core()


