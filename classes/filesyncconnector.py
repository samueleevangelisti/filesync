'''
filesyncconnector.py
'''
from utils import typechecks
from utils import paths



class FilesyncConnector:
    '''
    pass
    '''



    def __init__(self, root_path):
        typechecks.check(root_path, str)
        self.root_path = root_path



    def resolve_path(self, *entry_path_list):
        '''
        pass
        '''
        return paths.resolve_path(*((
            self.root_path,
        ) or () if not paths.is_absolute(*entry_path_list) else ()), *entry_path_list)



    def folder_path(self, *entry_path_list):
        '''
        pass
        '''
        return paths.folder_path(self.resolve_path(*entry_path_list))



    def file_name(self, *entry_path_list):
        '''
        pass
        '''
        return paths.file_name(self.resolve_path(*entry_path_list))



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
