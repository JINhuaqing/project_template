# A template for a class file
from utils.misc import  _set_verbose_level, _update_params
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
if not logger.hasHandlers():
    ch = logging.StreamHandler() # for console. 
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -  %(filename)s:%(lineno)d - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch) 



class MyClass:
    def __init__(self, verbose=1) -> None:
        _set_verbose_level(verbose, logger)
        pass