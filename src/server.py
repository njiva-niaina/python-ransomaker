import socket

def create_socket_and_receive_data(ip_address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip_address, port))
        print('Listening for connections...')
        s.listen(1)
        conn, addr = s.accept()
        print(f'Connection from {addr} established')
        with conn:
            while True:
                host_and_key = conn.recv(1024).decode()
                with open('encrypted_host.txt', 'a') as f:
                    f.write(host_and_key+'\n')
                break
            print('Connection completed and closed')

if __name__ == '__main__':
    ip_address = input('Enter the ip address: ')
    port = int(input('Enter the port: '))
    create_socket_and_receive_data(IP_ADDRESS, PORT)