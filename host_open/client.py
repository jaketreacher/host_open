import argparse
import json
import logging
import pickle
import socket
import sys
import utils

def get_synced_folders():
    """ Reads the appropriate file to get the synced_folder
    information so filepaths can be converted.

    Will look for the file 'synced_folder' in '/.vagrant_info'.

    Vagrantfile setup example:
        config.vm.synced_folder \
            ".vagrant/machines/default/virtualbox", \
            "/.vagrant_info"

    Returns:
        [<tuple>]: Uses the format (guestpath, hostpath)
    """
    folder = '/.vagrant_info'
    data_file = os.path.join(folder, 'synced_folders')

    if not os.path.exists(folder):
        logging.critical("%s doesn't exist. Exiting..." % folder)
        exit()

    with open(data_file, 'r') as file:
        data = json.load(file)

    folders = []
    for key_a in data.keys():
        for key_b in data[key_a].keys():
            guestpath = data[key_a][key_b]['guestpath']
            hostpath = data[key_a][key_b]['hostpath']
            folders.append(
                (guestpath,hostpath)
            )

    return synced_folders

def transmit_data(data):


if __name__ == '__main__':
    utils.init_logger()
    logger = logging.getLogger(__name__)

    message = (var1, var2)

    print('Connecting...', end='')
    sys.stdout.flush()
    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('localhost', 12345))
        print(' done!')
        clientsocket.send(message.encode())
    except ConnectionRefusedError:
        print('\n')
        print('Server not available.')