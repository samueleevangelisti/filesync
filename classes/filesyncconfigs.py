'''
filesyncconfigs.py
'''
from utils import logs



class FilesyncConfigs:
    '''
    pass
    '''



    def __init__(self, source_path, destination_path, is_delete, is_dual, ignore_regex_list, rename_dict):
        logs.debug('(FilesyncConfigs.__init__)', {
            'source_path': source_path,
            'destination_path': destination_path,
            'is_delete': is_delete,
            'is_dual': is_dual,
            'ignore_regex_list': ignore_regex_list,
            'rename_dict': rename_dict
        })
        self.source_path = source_path
        self.destination_path = destination_path
        self.is_delete = is_delete
        self.is_dual = is_dual
        self.ignore_regex_list_folder = []
        self.ignore_regex_list_file = []
        for ignore_regex in ignore_regex_list:
            if ignore_regex[-1] == '/':
                self.ignore_regex_list_folder.append(ignore_regex[:-1])
            else:
                self.ignore_regex_list_file.append(ignore_regex)
        self.rename_dict_folder = {}
        self.rename_dict_file = {}
        for key, value in rename_dict.items():
            if key[-1] == '/':
                self.rename_dict_folder[key[:-1]] = value[:-1]
            else:
                self.rename_dict_file[key] = value



    @staticmethod
    def from_dict(configs_dict):
        '''
        pass
        '''
        logs.debug('(FilesyncConfigs.from_dict)', {
            'configs_dict': configs_dict
        })
        return FilesyncConfigs(configs_dict['source_path'], configs_dict['destination_path'], configs_dict['is_delete'], configs_dict['is_dual'], configs_dict['ignore_regex_list'], configs_dict['rename_dict'])



    def to_dict(self):
        '''
        pass
        '''
        logs.debug('(FilesyncConfigs.to_dict)')
        return {
            'source_path': self.source_path,
            'destination_path': self.destination_path,
            'is_delete': self.is_delete,
            'is_dual': self.is_dual,
            'ignore_regex_list': [
                *[f"{ignore_regex}/" for ignore_regex in self.ignore_regex_list_folder],
                *self.ignore_regex_list_file
            ],
            'rename_dict': {
                **{f"{key}/": f"{value}/" for key, value in self.rename_dict_folder.items()},
                **self.rename_dict_file
            }
        }
