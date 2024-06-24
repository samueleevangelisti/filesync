'''
local_connector.py
'''
import os
import shutil

from utils import datetimes
from utils import paths
from classes.connector import Connector



class LocalConnector(Connector):
    '''
    Ad hoc connector for local filesystem
    '''



    def __init__(self, root_path):
        '''
        Overrides
        ---------
        Connector.__init__
        '''
        Connector.__init__(self, paths.resolve_path(root_path))



    def is_entry(self, *entry_path_list):
        '''
        Overrides
        ---------
        Connector.is_entry
        '''
        return paths.is_entry(self.resolve_path(*entry_path_list))



    def is_folder(self, *entry_path_list):
        '''
        Overrides
        ---------
        Connector.is_folder
        '''
        return paths.is_folder(self.resolve_path(*entry_path_list))



    def entry_list(self, *folder_path_list):
        '''
        Overrides
        ---------
        Connector.entry_list
        '''
        return os.listdir(self.resolve_path(*folder_path_list))



    def make_folder(self, *folder_path_list):
        '''
        Overrides
        ---------
        Connector.make_folder
        '''
        os.makedirs(self.resolve_path(*folder_path_list))



    def remove_folder(self, *folder_path_list):
        '''
        Overrides
        ---------
        Connector.remove_folder
        '''
        shutil.rmtree(self.resolve_path(*folder_path_list))



    def get_m_time(self, *file_path_list):
        '''
        Overrides
        ---------
        Connector.get_m_time
        '''
        return datetimes.from_timestamp(os.stat(self.resolve_path(*file_path_list)).st_mtime)



    def read_file(self, *file_path_list):
        '''
        Overrides
        ---------
        Connector.read_file
        '''
        with open(self.resolve_path(*file_path_list), 'rb') as file:
            return file.read()



    def write_file(self, file_bytes, *file_path_list):
        '''
        Overrides
        ---------
        Connector.write_file
        '''
        folder_path = self.folder_path(*file_path_list)
        if not self.is_folder(folder_path):
            self.make_folder(folder_path)
        with open(self.resolve_path(*file_path_list), 'wb') as file:
            file.write(file_bytes)



    def remove_file(self, *file_path_list):
        '''
        Overrides
        ---------
        Connector.remove_file
        '''
        os.remove(self.resolve_path(*file_path_list))



    def quit(self):
        '''
        Overrides
        ---------
        Connector.quit
        '''
