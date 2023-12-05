'''
filesyncconfigs.py
'''
import click

from utils import typechecks



class FilesyncConfigs:
    '''
    pass
    '''



    def __init__(self, is_source_ftp, source_path, is_destination_ftp, destination_path, is_delete, is_dual, ignore_regex_list, rename_dict):
        typechecks.check(is_source_ftp, bool)
        typechecks.check(source_path, str)
        typechecks.check(is_destination_ftp, bool)
        typechecks.check(destination_path, str)
        typechecks.check(is_delete, bool)
        typechecks.check(is_dual, bool)
        typechecks.check(ignore_regex_list, list)
        typechecks.check(rename_dict, dict)
        self.is_source_ftp = is_source_ftp
        self.source_path = source_path
        self.is_destination_ftp = is_destination_ftp
        self.destination_path = destination_path
        self.is_delete = is_delete
        self.is_dual = is_dual
        self.folder_ignore_regex_list = []
        self.file_ignore_regex_list = []
        for ignore_regex in ignore_regex_list:
            if ignore_regex[-1] == '/':
                self.folder_ignore_regex_list.append(ignore_regex[:-1])
            else:
                self.file_ignore_regex_list.append(ignore_regex)
        self.folder_rename_dict = {}
        self.file_rename_dict = {}
        for key, value in rename_dict.items():
            if key[-1] == '/':
                self.folder_rename_dict[key[:-1]] = value[:-1]
            else:
                self.file_rename_dict[key] = value



    @staticmethod
    def prompt_create():
        '''
        pass
        '''
        return FilesyncConfigs(click.prompt('is_source_ftp', type=bool, default=False, show_default=True), click.prompt('source_path', type=str, default='.', show_default=True), click.prompt('is_destination_ftp', type=bool, default=False, show_default=True), click.prompt('destination_path', type=str, default='.', show_default=True), click.prompt('is_delete', type=bool, default=True, show_default=True), click.prompt('is_dual', type=bool, default=False, show_default=True), click.prompt('ignore_regex_list', type=list, default=[
            '.*\\.git/',
            '.*\\_\\_pycache\\_\\_/',
            '.*filesync\\-configs\\.json',
            '.*\\.gitignore',
            '.*\\.gitattributes',
            '.*\\.gitsubmodules'
        ], show_default=True), click.prompt('rename_dict', type=dict, default={}, show_default=True))



    @staticmethod
    def from_dict(configs_dict):
        '''
        pass
        '''
        return FilesyncConfigs(configs_dict['is_source_ftp'], configs_dict['source_path'], configs_dict['is_destination_ftp'], configs_dict['destination_path'], configs_dict['is_delete'], configs_dict['is_dual'], configs_dict['ignore_regex_list'], configs_dict['rename_dict'])



    def to_dict(self):
        '''
        pass
        '''
        return {
            'is_source_ftp': self.is_source_ftp,
            'source_path': self.source_path,
            'is_destination_ftp': self.is_destination_ftp,
            'destination_path': self.destination_path,
            'is_delete': self.is_delete,
            'is_dual': self.is_dual,
            'ignore_regex_list': [
                *[f"{ignore_regex}/" for ignore_regex in self.folder_ignore_regex_list],
                *self.file_ignore_regex_list
            ],
            'rename_dict': {
                **{f"{key}/": f"{value}/" for key, value in self.folder_rename_dict.items()},
                **self.file_rename_dict
            }
        }
