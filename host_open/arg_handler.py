import argparse
import logging

def convert2level(arg):
    """ Convert the 'level' obtained from the command line
    into a useful logging.<LEVEL> value
    """
    arg = arg.lower()
    level_dict = {
        'critial': logging.CRITICAL,
        'error': logging.ERROR,
        'warning': logging.WARNING,
        'info': logging.INFO,
        'debug': logging.DEBUG,
    }

    if arg in level_dict:
        level = level_dict[arg]
    else:
        level = None

    return level

def parse_client(args):
    parser = argparse.ArgumentParser(description='Host Open: Client.')
    parser.add_argument('-p', '--port',
                        help='The port to connect through.',
                        type=int,
                        default=12345)
    parser.add_argument('-l', '--log', 
                        help='The verbosity of log messages.',
                        type=str,
                        default='info')
    parser.add_argument('files',
                        help='The files to send.',
                        nargs='*')

    results = parser.parse_args(args)

    level = convert2level(results.log)
    port = results.port
    files = results.files
    flags = None
    return level, port, files, flags

def parse_server(args):
    pass