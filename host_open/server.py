import argpse
import pickle
import logging
import socket
import sys
import utils

utils.init_logger()
logger = logging.getLogger(__name__)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 12345))
serversocket.listen(5)

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(4096).decode()
    if len(buf) > 0:
        print(var1,var2)
        if '-q' in buf:
            break

print('Closed')



if __name__ == '__main__':

