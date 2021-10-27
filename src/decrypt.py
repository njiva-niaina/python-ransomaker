import pyAesCrypt
import os
import glob

# Encryption information
BUFFER_SIZE = 64 * 1024

def decrypt(key):
    current_dir = os.environ['USERPROFILE'] + '\Desktop'
    print('Beginning recursive decryption...')
    for x in glob.glob(f'{current_dir}\\**\*', recursive=True):
        full_path = os.path.join(current_dir, x)
        full_new_file = os.path.join(current_dir, os.path.splitext(x)[0])
        if os.path.isfile(full_path):
            print('>>> Encrypted:\t'+full_path+'')
            try:
                pyAesCrypt.decryptFile(full_path, full_new_file, key, BUFFER_SIZE)
                print('>>> Decrypted:\t'+full_new_file+'\n')
                os.remove(full_path)
            except ValueError:
                print('>>> Error - Wrong password!\n')

if __name__ == '__main__':
    key = input('Enter the decryption key: ')
    decrypt(key)
