'''
logs.py
'''
from datetime import datetime

import environments



_COLOR_NONE = 0
_COLOR_BLUE = 94
_COLOR_PURPLE = 95
_COLOR_GREEN = 92
_COLOR_YELLOW = 93
_COLOR_RED = 91

_IS_LOG = True
_IS_DEBUG = environments.DEVELOPMENT
_IS_INFO = True
_IS_SUCCESS = True
_IS_WARNING = True
_IS_ERROR = True



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



def _log(text):
    '''
    _log(text)
    '''
    if _IS_LOG:
        print(f"{color_blue(f'[{datetime.now().isoformat()}]')} {text}")



def debug(text):
    '''
    debug(text)
    '''
    if _IS_DEBUG:
        _log(color_purple(f"(DEBUG) {text}"))



def info(text):
    '''
    info(text)
    '''
    if _IS_INFO:
        _log(f"(INFO) {text}")



def success(text):
    '''
    success(text)
    '''
    if _IS_SUCCESS:
        _log(color_green(f"(SUCCESS) {text}"))



def warning(text):
    '''
    warning(text)
    '''
    if _IS_WARNING:
        _log(color_yellow(f"(WARNING) {text}"))



def error(text):
    '''
    error(text)
    '''
    if _IS_ERROR:
        _log(color_red(f"(ERROR) {text}"))
