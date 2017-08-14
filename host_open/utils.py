import logging

def init_logger(level):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)-12s: %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M',
        filename='debug.log',
        filemode='w'
    )