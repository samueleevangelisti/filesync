'''
paths.py
'''
from os import path



def resolve_path(*entry_path_list):
    '''
    Resolves the input path and returns the absolute path
    '''
    return path.abspath(path.expandvars(path.join(*entry_path_list)))



def is_entry(*entry_path_list):
    '''
    Returns true if entry exists
    '''
    return path.exists(resolve_path(*entry_path_list))



def folder_path(*file_path_list):
    '''
    Returns the folder path
    '''
    return path.dirname(resolve_path(*file_path_list))
