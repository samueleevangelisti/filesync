'''
connector.py
'''
from utils import typechecks
from utils import paths



class Connector:
    '''
    Connector to navigate folders and files
    '''



    def __init__(self, root_path):
        '''
        Parameters
        ----------
        root_path : str
            Path of the root
        '''
        typechecks.check(root_path, str)
        self.root_path = root_path



    def resolve_path(self, *entry_path_list):
        '''
        Resolve the path according to the root path

        Parameters
        ----------
        entry_path_list : list<str>
            List of entries composing the path

        Returns
        -------
        str
        '''
        return paths.resolve_path(*(((
            self.root_path,
        ) if self.root_path else ()) if not paths.is_absolute(*entry_path_list) else ()), *entry_path_list)



    def folder_path(self, *entry_path_list):
        '''
        Return the path of the folder

        Parameters
        ----------
        entry_path_list : list<str>
            List of entries composing the path

        Returns
        -------
        str
        '''
        return paths.get_folder_path(self.resolve_path(*entry_path_list))



    def file_name(self, *entry_path_list):
        '''
        Return the name of the file

        Parameters
        ----------
        entry_path_list : list<str>
            List of entries composing the path

        Returns
        -------
        str
        '''
        return paths.get_file_name(self.resolve_path(*entry_path_list))



    def is_entry(self, *entry_path_list):
        '''
        Return True if the entry exists

        Parameters
        ----------
        entry_path_list : list<str>
            List of entries composing the path

        Returns
        -------
        bool
        '''
        raise NotImplementedError('Method not implemented')



    def is_folder(self, *entry_path_list):
        '''
        Return true if the entry is a folder

        Parameters
        ----------
        entry_path_list : list<str>
            List of entries composing the path

        Returns
        -------
        bool
        '''
        raise NotImplementedError('Method not implemented')



    def entry_list(self, *folder_path_list):
        '''
        Return the list of entry inside the folder

        Parameters
        ----------
        folder_path_list : list<str>
            List of entries composing the path

        Returns
        -------
        list<str>
        '''
        raise NotImplementedError('Method not implemented')



    def make_folder(self, *folder_path_list):
        '''
        Creates a folder

        Parameters
        ----------
        folder_path_list : list<str>
            List of entries composing the path
        '''
        raise NotImplementedError('Method not implemented')



    def remove_folder(self, *folder_path_list):
        '''
        Remove a folder

        Parameters
        ----------
        folder_path_list : list<str>
            List of entries composing the path
        '''
        raise NotImplementedError('Method not implemented')



    def get_m_time(self, *file_path_list):
        '''
        Return the last modification time of a file

        Parameters
        ----------
        file_path_list : list<str>
            List of entries composing the path

        Returns
        -------
        datetime
        '''
        raise NotImplementedError('Method not implemented')



    def read_file(self, *file_path_list):
        '''
        Return the content of a file in bytes

        Parameters
        ----------
        file_path_list : list<str>
            List of entries composing the path

        Returns
        -------
        bytes
        '''
        raise NotImplementedError('Method not implemented')



    def write_file(self, file_bytes, *file_path_list):
        '''
        Write a file

        Parameters
        ----------
        bytes : bytes
            Content of the file
        file_path_list : list<str>
            List of entries composing the path
        '''
        raise NotImplementedError('Method not implemented')



    def remove_file(self, *file_path_list):
        '''
        Remove a file

        Parameters
        ----------
        file_path_list : list<str>
            List of entries composing the path
        '''
        raise NotImplementedError('Method not implemented')



    def quit(self):
        '''
        Quit the connection to filesystem if needed
        '''
        raise NotImplementedError('Method not implemented')
