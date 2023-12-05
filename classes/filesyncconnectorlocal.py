'''
filesyncconnectorlocal.py
'''
import os
import shutil
from datetime import datetime

from utils import paths
from classes.filesyncconnector import FilesyncConnector



class FilesyncConnectorLocal(FilesyncConnector):
    '''
    pass
    '''



    def __init__(self, root_path):
        FilesyncConnector.__init__(self, paths.resolve_path(root_path))



    def is_entry(self, *entry_path_list):
        '''
        pass
        '''
        return paths.is_entry(self.resolve_path(*entry_path_list))



    def is_folder(self, *entry_path_list):
        '''
        pass
        '''
        return paths.is_folder(self.resolve_path(*entry_path_list))



    def entry_list(self, *folder_path_list):
        '''
        pass
        '''
        return os.listdir(self.resolve_path(*folder_path_list))



    def make_folder(self, *folder_path_list):
        '''
        pass
        '''
        os.makedirs(self.resolve_path(*folder_path_list))



    def remove_folder(self, *folder_path_list):
        '''
        pass
        '''
        shutil.rmtree(self.resolve_path(*folder_path_list))



    def m_time(self, *file_path_list):
        '''
        pass
        '''
        return datetime.utcfromtimestamp(os.stat(self.resolve_path(*file_path_list)).st_mtime)



    def read_file(self, *file_path_list):
        '''
        pass
        '''
        with open(self.resolve_path(*file_path_list), 'rb') as file:
            return file.read()



    def write_file(self, byte, *file_path_list):
        '''
        pass
        '''
        folder_path = self.folder_path(*file_path_list)
        if not self.is_folder(folder_path):
            self.make_folder(folder_path)
        with open(self.resolve_path(*file_path_list), 'wb') as file:
            file.write(byte)



    def remove_file(self, *file_path_list):
        '''
        pass
        '''
        os.remove(self.resolve_path(*file_path_list))



    def quit(self):
        '''
        pass
        '''
