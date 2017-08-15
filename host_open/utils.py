import logging
import pickle

def init_logger(level):
    logging.basicConfig(
        level=level,
        format='%(name)-12s: %(levelname)-8s %(message)s',
    )

def pack_data(filepaths, flags):
    data = (filepaths, flags)
    return pickle.dumps(data)

def unpack_data(data):
    filepaths, flags = pickle.loads(data)
    return filepaths, flags