'''
logs.py
This module is from samueva97 private repository `myutils`.
Do not modify it
'''
import sys
import logging
from datetime import datetime
import json

import environments
from utils import paths



def _create_log_file_name(date_str=None):
    return f"log_{date_str or datetime.utcnow().strftime('%Y-%m-%d')}.log"



# TODO DSE implementare correttamente questa funzione
# logging.basicConfig(
#     format='[%(asctime)s] %(process)d:%(thread)d %(name)s %(module)s:%(funcName)s (%(levelname)s) %(message)s',
#     level=logging.INFO,
#     handlers = [
#         logging.StreamHandler(sys.stdout),
#         logging.FileHandler(paths.resolve_path(paths.folder_path(__file__), 'logs', _create_log_file_name()))
#     ]
# )



_IS_LOG = True
_IS_DEBUG = environments.DEVELOPMENT
_IS_INFO = True
_IS_SUCCESS = True
_IS_WARNING = True
_IS_ERROR = True

_COLOR_NONE = 0
_COLOR_BLUE = 94
_COLOR_PURPLE = 95
_COLOR_GREEN = 92
_COLOR_YELLOW = 93
_COLOR_RED = 91

CHAR_NEW_LINE = '\n'



def _color(text, color):
    text = str(text).replace('\n', f"\033[{_COLOR_NONE}m\n\033[{color}m")
    return f"\033[{color}m{text}\033[{_COLOR_NONE}m"



def color_blue(text):
    '''
    Returns the text colored in blue
    '''
    return _color(text, _COLOR_BLUE)



def color_purple(text):
    '''
    Returns the text colored in purple
    '''
    return _color(text, _COLOR_PURPLE)



def color_green(text):
    '''
    Returns the text colored in green
    '''
    return _color(text, _COLOR_GREEN)



def color_yellow(text):
    '''
    Returns the text colored in yellow
    '''
    return _color(text, _COLOR_YELLOW)



def color_red(text):
    '''
    Returns the text colored in red
    '''
    return _color(text, _COLOR_RED)



def print_blue(text):
    '''
    Prints the text colored in blue
    '''
    print(color_blue(text))



def print_purple(text):
    '''
    Prints the text colored in purple
    '''
    print(color_purple(text))



def print_green(text):
    '''
    Prints the text colored in green
    '''
    print(color_green(text))



def print_yellow(text):
    '''
    Prints the text colored in yellow
    '''
    print(color_yellow(text))



def print_red(text):
    '''
    Prints the text colored in red
    '''
    print(color_red(text))



def _log(text, color_fn=lambda e: e, param_dict=None):
    '''
    _log(text)
    '''
    if _IS_LOG:
        param_str = '\n{param_dict}'.format(param_dict=json.dumps(param_dict, indent=2)) if param_dict else ''
        print(f"{color_blue(f'[{datetime.now().isoformat()}]')} {color_fn(f'{text}{param_str}')}")



def debug(text, param_dict=None):
    '''
    debug(text)
    '''
    if _IS_DEBUG:
        _log(f"(DEBUG) {text}", color_purple, param_dict)



def info(text, param_dict=None):
    '''
    info(text)
    '''
    if _IS_INFO:
        _log(f"(INFO) {text}", lambda e: e, param_dict)



def success(text, param_dict=None):
    '''
    success(text)
    '''
    if _IS_SUCCESS:
        _log(f"(SUCCESS) {text}", color_green, param_dict)



def warning(text, param_dict=None):
    '''
    warning(text)
    '''
    if _IS_WARNING:
        _log(f"(WARNING) {text}", color_yellow, param_dict)



def error(text, param_dict=None):
    '''
    error(text)
    '''
    if _IS_ERROR:
        _log(f"(ERROR) {text}", color_red, param_dict)
