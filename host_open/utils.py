import logging
import pickle

def init_logger(level):
    logging.basicConfig(
        level=level,
        format='%(name)-12s: %(levelname)-8s %(message)s',
    )

def pack_data(filepaths, alt_app):
    data = (filepaths, alt_app)
    return pickle.dumps(data)

def unpack_data(data):
    filepaths, alt_app = pickle.loads(data)
    return filepaths, alt_app