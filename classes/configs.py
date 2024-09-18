'''
configs.py
'''
import click

from utils import typechecks



class Configs:
    '''
    Ad hoc config class
    '''



    def __init__(self, order, is_source_ftp, source_path, is_destination_ftp, destination_path, is_force, is_delete, is_dual, ignore_regex_list, rename_dict):
        '''
        Parameters
        ----------
        order : int
            Execution order when more configs are selected
        is_source_ftp : bool
            True if source is ftp
        source_path : str
            Source path
        is_destination_ftp : bool
            True if destination is ftp
        destination_path : str
            Destination path
        is_force : bool
            True to force copy of files from source to destination
        is_delete : bool
            True to delete file not in source
        is_dual : bool
            True to sync newer files from destination to source
        ignore_regex_list : list
            Files and folders to ignore
        rename_dict : dict
            Force renaming of certain files and folders
        '''
        typechecks.check(order, int)
        typechecks.check(is_source_ftp, bool)
        typechecks.check(source_path, str)
        typechecks.check(is_destination_ftp, bool)
        typechecks.check(destination_path, str)
        typechecks.check(is_force, bool)
        typechecks.check(is_delete, bool)
        typechecks.check(is_dual, bool)
        typechecks.check(ignore_regex_list, list)
        typechecks.check(rename_dict, dict)
        self.order = order
        self.is_source_ftp = is_source_ftp
        self.source_path = source_path
        self.is_destination_ftp = is_destination_ftp
        self.destination_path = destination_path
        self.is_force = is_force
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
        Creates configs using click prompt

        Returns
        -------
        Configs
        '''
        return Configs(click.prompt('order', type=int, default=0, show_default=True), click.prompt('is_source_ftp', type=bool, default=False, show_default=True), click.prompt('source_path', type=str, default='.', show_default=True), click.prompt('is_destination_ftp', type=bool, default=False, show_default=True), click.prompt('destination_path', type=str, default='.', show_default=True), click.prompt('is_force', type=bool, default=False, show_default=True), click.prompt('is_delete', type=bool, default=True, show_default=True), click.prompt('is_dual', type=bool, default=False, show_default=True), click.prompt('ignore_regex_list', type=list, default=[
            '.*\\.git/',
            '.*\\_\\_pycache\\_\\_/',
            '.*filesync\\-configs\\.json',
            '.*\\.gitignore',
            '.*\\.gitattributes',
            '.*\\.gitsubmodules'
        ], show_default=True), click.prompt('rename_dict', type=dict, default={}, show_default=True))



    def prompt_modify(self):
        '''
        Modify the configs using click prompt
        '''
        self.order = click.prompt('order', type=int, default=self.order, show_default=True)
        self.is_source_ftp = click.prompt('is_source_ftp', type=bool, default=self.is_source_ftp, show_default=True)
        self.source_path = click.prompt('source_path', type=str, default=self.source_path, show_default=True)
        self.is_destination_ftp = click.prompt('is_destination_ftp', type=bool, default=self.is_destination_ftp, show_default=True)
        self.destination_path = click.prompt('destination_path', type=str, default=self.is_destination_ftp, show_default=True)
        self.is_force = click.prompt('is_force', type=bool, default=self.is_force, show_default=True)
        self.is_delete = click.prompt('is_delete', type=bool, default=self.is_delete, show_default=True)
        self.is_dual = click.prompt('is_dual', type=bool, default=self.is_dual, show_default=True)
        ignore_regex_list = click.prompt('ignore_regex_list', type=list, default=[
            *[f"{ignore_regex}/" for ignore_regex in self.folder_ignore_regex_list],
            *self.file_ignore_regex_list
        ], show_default=True)
        self.folder_ignore_regex_list = []
        self.file_ignore_regex_list = []
        for ignore_regex in ignore_regex_list:
            if ignore_regex[-1] == '/':
                self.folder_ignore_regex_list.append(ignore_regex[:-1])
            else:
                self.file_ignore_regex_list.append(ignore_regex)
        rename_dict = click.prompt('rename_dict', type=dict, default={
            **{f"{key}/": f"{value}/" for key, value in self.folder_rename_dict.items()},
            **self.file_rename_dict
        }, show_default=True)
        self.folder_rename_dict = {}
        self.file_rename_dict = {}
        for key, value in rename_dict.items():
            if key[-1] == '/':
                self.folder_rename_dict[key[:-1]] = value[:-1]
            else:
                self.file_rename_dict[key] = value



    @staticmethod
    def from_dict(configs_dict):
        '''
        Create configs from dict

        Parameters
        ----------
        configs_dict : dict
            Dict from configs
        
        Returns
        -------
        Configs
        '''
        return Configs(configs_dict['order'], configs_dict['is_source_ftp'], configs_dict['source_path'], configs_dict['is_destination_ftp'], configs_dict['destination_path'], configs_dict['is_force'], configs_dict['is_delete'], configs_dict['is_dual'], configs_dict['ignore_regex_list'], configs_dict['rename_dict'])



    def to_dict(self):
        '''
        Create a dict from configs

        Returns
        -------
        dict
        '''
        return {
            'order': self.order,
            'is_source_ftp': self.is_source_ftp,
            'source_path': self.source_path,
            'is_destination_ftp': self.is_destination_ftp,
            'destination_path': self.destination_path,
            'is_force': self.is_force,
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
