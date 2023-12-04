'''
logs.py
This module is from samueva97.
Do not modify it
'''
import logging
from logging import StreamHandler
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime

import environments
from utils import colors
from utils import paths
from utils import converts



_QUERY = logging.DEBUG + 1
_REQUEST = logging.DEBUG + 2
_SUCCESS = logging.INFO + 1









class CustomTimedRotatingFileHandler(TimedRotatingFileHandler):
    '''
    Timed rotating file handler with correct renaming
    '''



    def namer(self, file_name):
        '''
        Overrides
        ---------
        TimedRotatingFileHandler.namer
        '''
        return paths.resolve_path(paths.folder_path(self.baseFilename), f"{datetime.utcnow().isoformat()}-{paths.file_name(self.baseFilename)}")



    def rotator(self, source, dest):
        '''
        Overrides
        ---------
        TimedRotatingFileHandler.rotator
        '''
        if paths.is_entry(source):
            os.rename(source, dest)
            with open(dest, 'rb') as source_file:
                with open(f"{dest}.zstd", 'wb') as destination_file:
                    destination_file.write(converts.byte_to_zstd(source_file.read()))
            os.remove(dest)









class CustomFormatter(Formatter):
    '''
    Formatter for utc time and colored log
    '''
    levelno_color_map = {
        logging.DEBUG: colors.PURPLE,
        _QUERY: colors.ORANGE,
        _REQUEST: colors.BLUE,
        logging.INFO: colors.NONE,
        _SUCCESS: colors.GREEN,
        logging.WARNING: colors.YELLOW,
        logging.ERROR: colors.RED,
        logging.CRITICAL: colors.RED
    }



    def __init__(self, fmt=None, datefmt=None, style='%', validate=True, *, defaults=None):
        '''
        Overrides
        ---------
        Formatter.__init__
        '''
        Formatter.__init__(self, f"{colors.GREY}[%(asctime)s] %(process)d:%(thread)d %(module)s:%(funcName)s %(name)s{colors.NONE} %(log_color)s(%(levelname)s) %(message)s{colors.NONE}", datefmt, style, validate, defaults=defaults)



    def formatTime(self, record, datefmt=None):
        '''
        Overrides
        ---------
        Formatter.formatTime
        '''
        return datetime.utcfromtimestamp(record.created).isoformat()



    def formatMessage(self, record):
        '''
        Overrides
        ---------
        Formatter.formatMessage
        '''
        record.message = record.message.replace(colors.NONE, f"{colors.NONE}{CustomFormatter.levelno_color_map[record.levelno]}")
        record.log_color = CustomFormatter.levelno_color_map[record.levelno]
        return Formatter.formatMessage(self, record)









logging.addLevelName(_QUERY, 'QUERY')
logging.addLevelName(_REQUEST, 'REQUEST')
logging.addLevelName(_SUCCESS, 'SUCCESS')



_LOGGER = logging.getLogger()
_LOGGER.setLevel(logging.DEBUG if environments.IS_DEVELOPMENT else logging.INFO)
custom_formatter = CustomFormatter()
console_handler = StreamHandler()
console_handler.setFormatter(custom_formatter)
_LOGGER.addHandler(console_handler)
if environments.IS_LOG_FILE:
    if not paths.is_entry(environments.LOG_FOLDER_PATH):
        os.makedirs(environments.LOG_FOLDER_PATH)
    elif not paths.is_folder(environments.LOG_FOLDER_PATH):
        raise Exception(f"`{environments.LOG_FOLDER_PATH}` is not a folder")
    file_handler = CustomTimedRotatingFileHandler(paths.resolve_path(environments.LOG_FOLDER_PATH, 'log.log'), when='midnight')
    file_handler.setFormatter(custom_formatter)
    _LOGGER.addHandler(file_handler)



def debug(text):
    '''
    debug(text)
    '''
    logging.debug(text)



def query(text):
    '''
    query(text)
    '''
    logging.log(_QUERY, text)



def request(text):
    '''
    request(text)
    '''
    logging.log(_REQUEST, text)



def info(text):
    '''
    info(text)
    '''
    logging.info(text)



def success(text):
    '''
    success(text)
    '''
    logging.log(_SUCCESS, text)



def warning(text):
    '''
    warning(text)
    '''
    logging.warning(text)



def error(text):
    '''
    error(text)
    '''
    logging.error(text)



def critical(text):
    '''
    critical(text)
    '''
    logging.critical(text)



def exception(text):
    '''
    error(text)
    '''
    logging.exception(text)
