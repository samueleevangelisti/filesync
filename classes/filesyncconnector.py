'''
filesyncconnector.py
'''
from os import path

from utils import logs
from utils import paths



class FilesyncConnector:
    '''
    pass
    '''



    def __init__(self, root_path):
        logs.debug(f"(FilesyncConnector.__init__) root_path: {root_path}")
        self.root_path = root_path



    def resolve_path(self, *entry_path_list):
        '''
        pass
        '''
        logs.debug(f"(FilesyncConnector.resolve_path) entry_path_list: {entry_path_list}")
        return paths.resolve_path(*(((self.root_path if self.root_path is not None else ''), ) if not path.isabs(entry_path_list[0]) else ()), *entry_path_list)



    def folder_path(self, *entry_path_list):
        '''
        pass
        '''
        logs.debug(f"(FilesyncConnector.folder_path) entry_path_list: {entry_path_list}")
        return path.dirname(self.resolve_path(*entry_path_list))



    def file_name(self, *entry_path_list):
        '''
        pass
        '''
        logs.debug(f"(FilesyncConnector.file_name) entry_path_list: {entry_path_list}")
        return path.basename(self.resolve_path(*entry_path_list))



    def is_entry(self, *entry_path_list):
        '''
        pass
        '''
        raise NotImplementedError('Method not implemented')



    def is_folder(self, *entry_path_list):
        '''
        pass
        '''
        raise NotImplementedError('Method not implemented')



    def entry_list(self, *folder_path_list):
        '''
        pass
        '''
        raise NotImplementedError('Method not implemented')



    def make_folder(self, *folder_path_list):
        '''
        pass
        '''
        raise NotImplementedError('Method not implemented')



    def remove_folder(self, *folder_path_list):
        '''
        pass
        '''
        raise NotImplementedError('Method not implemented')



    def m_time(self, *file_path_list):
        '''
        pass
        '''
        raise NotImplementedError('Method not implemented')



    def read_file(self, *file_path_list):
        '''
        pass
        '''
        raise NotImplementedError('Method not implemented')



    def write_file(self, byte, *file_path_list):
        '''
        pass
        '''
        raise NotImplementedError('Method not implemented')



    def remove_file(self, *file_path_list):
        '''
        pass
        '''
        raise NotImplementedError('Method not implemented')



    def quit(self):
        '''
        pass
        '''
        raise NotImplementedError('Method not implemented')
