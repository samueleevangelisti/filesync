'''
filesyncconnectorftp.py
'''
from io import BytesIO
from datetime import datetime
from ftplib import FTP_TLS

from utils import typechecks
from utils import paths
from classes.filesyncconnector import FilesyncConnector



class FilesyncConnectorFtp(FilesyncConnector):
    '''
    pass
    '''



    def __init__(self, root_path, host, port, user, password):
        typechecks.check(host, str)
        typechecks.check(port, int)
        typechecks.check(user, str, None)
        typechecks.check(password, str, None)
        ftp_tls = FTP_TLS()
        ftp_tls.connect(host, port)
        if user:
            ftp_tls.login(user, password)
        FilesyncConnector.__init__(self, paths.resolve_path(*((
            ftp_tls.pwd(),
        ) if not paths.is_absolute(root_path) else ()), root_path))
        self.ftp_tls = ftp_tls



    def is_entry(self, *entry_path_list):
        '''
        pass
        '''
        return self.file_name(*entry_path_list) in self.ftp_tls.nlst(self.folder_path(*entry_path_list))



    def is_folder(self, *entry_path_list):
        '''
        pass
        '''
        entry_path = self.resolve_path(*entry_path_list)
        return bool(tuple(entry for entry in self.ftp_tls.mlsd(self.folder_path(entry_path)) if entry[0] == self.file_name(entry_path) and entry[1]['type'] == 'dir')) or entry_path == '/'



    def entry_list(self, *folder_path_list):
        '''
        pass
        '''
        return self.ftp_tls.nlst(self.resolve_path(*folder_path_list))



    def make_folder(self, *folder_path_list):
        '''
        pass
        '''
        folder_path = self.folder_path(*folder_path_list)
        if not self.is_folder(folder_path):
            self.make_folder(folder_path)
        self.ftp_tls.mkd(self.resolve_path(*folder_path_list))



    def remove_folder(self, *folder_path_list):
        '''
        pass
        '''
        folder_path = self.resolve_path(*folder_path_list)
        for entry in self.ftp_tls.mlsd(folder_path):
            if entry[1]['type'] == 'dir':
                self.remove_folder(folder_path, entry[0])
            else:
                self.remove_file(folder_path, entry[0])
        self.ftp_tls.rmd(folder_path)



    def m_time(self, *file_path_list):
        '''
        pass
        '''
        return datetime.strptime([entry for entry in self.ftp_tls.mlsd(self.folder_path(*file_path_list)) if entry[0] == self.file_name(*file_path_list)][0]['modify'], '%Y%m%d%H%M%S.%f')



    def read_file(self, *file_path_list):
        '''
        pass
        '''
        byte_str = b''
        def _read_file(byte):
            nonlocal byte_str
            byte_str += byte
        self.ftp_tls.retrbinary(f"RETR {self.resolve_path(*file_path_list)}", _read_file)
        return byte_str



    def write_file(self, byte, *file_path_list):
        '''
        pass
        '''
        folder_path = self.folder_path(*file_path_list)
        if not self.is_folder(folder_path):
            self.make_folder(folder_path)
        self.ftp_tls.storbinary(f"STOR {self.resolve_path(*file_path_list)}", BytesIO(byte))



    def remove_file(self, *file_path_list):
        '''
        pass
        '''
        self.ftp_tls.delete(self.resolve_path(*file_path_list))



    def quit(self):
        '''
        pass
        '''
        self.ftp_tls.quit()
