'''
paths.py
'''
from os import path



def resolve_path(*entry_path_list):
    '''
    Resolves the input path and returns the absolute path
    '''
    return path.abspath(path.expandvars(path.join(*entry_path_list)))
