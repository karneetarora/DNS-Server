import socket
from sys import argv
import argparse

parser = argparse.ArgumentParser(description="""This is a very basic client program""")
parser.add_argument('-f', type=str, help='This is the source file for the strings to reverse', default='source_strings.txt',action='store', dest='in_file')
parser.add_argument('-o', type=str, help='This is the destination file for the reversed strings', default='results.txt',action='store', dest='out_file')
parser.add_argument('port', type=int, help='This is the port to connect to the server on', action='store')
args = parser.parse_args(argv[1:])

host = socket.gethostname()
print(f'[S]: Host is - {host}')

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('[S]: Server socket created')

except socket.error as err:
    print(f"[S]: Couldn't create socket due to {err}")
    exit()
SERVER = ('', args.port)
ss.bind((SERVER))
ss.listen(1)

connection, address = ss.accept()

with connection:
    while True:
        data = connection.recv(512)
        data = data.decode('utf-8')
        index = len(data) + 1
        file = open("Pairs.txt", "r")
        for line in file:
            data_found = False
            if data in line:
                data_found = True
                break
        if data_found:
            print(line[index:])
        elif data_found == False:
            print('Not Found')
        if not data:
            break
        connection.sendall(data.encode('utf=8'))
ss.close()
exit()





