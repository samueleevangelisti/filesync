'''
utils.py
'''
import re

from utils import prints



def sync(source_filesync_connector, source_path, destination_filesync_connector, destination_path, configs, is_force):
    '''
    pass
    '''
    source_folder_list = []
    source_file_list = []
    for entry in source_filesync_connector.entry_list(source_path):
        if source_filesync_connector.is_folder(source_path, entry):
            source_folder_list.append(entry)
        else:
            source_file_list.append(entry)
    source_folder_list.sort()
    source_file_list.sort()

    destination_folder_list = []
    destination_file_list = []
    for entry in destination_filesync_connector.entry_list(destination_path):
        if destination_filesync_connector.is_folder(destination_path, entry):
            destination_folder_list.append(entry)
        else:
            destination_file_list.append(entry)
    destination_folder_list.sort()
    destination_file_list.sort()

    for folder in source_folder_list:
        source_folder_path = source_filesync_connector.resolve_path(source_path, folder)
        is_ignore = False
        for ignore_regex in configs.folder_ignore_regex_list:
            is_ignore = is_ignore or re.match(ignore_regex, source_folder_path)
        if not is_ignore:
            destination_folder_path = destination_filesync_connector.resolve_path(destination_path, folder)
            if source_folder_path in configs.folder_rename_dict:
                destination_folder_path = configs.folder_rename_dict[source_folder_path]
                del configs.folder_rename_dict[source_folder_path]
                prints.purple(f" || {source_folder_path} -> {destination_folder_path}")
            if folder not in destination_folder_list:
                destination_filesync_connector.make_folder(destination_folder_path)
            prints.purple(f" ?? {destination_folder_path}")
            sync(source_filesync_connector, source_folder_path, destination_filesync_connector, destination_folder_path, configs, is_force)
            if folder in destination_folder_list:
                destination_folder_list.remove(folder)
        else:
            prints.yellow(f" !! {source_folder_path}")

    for folder in destination_folder_list:
        remove_folder_path = destination_filesync_connector.resolve_path(destination_path, folder)
        is_ignore = False
        for ignore_regex in configs.folder_ignore_regex_list:
            is_ignore = is_ignore or re.match(ignore_regex, remove_folder_path)
        if not is_ignore:
            if configs.is_delete:
                prints.red(f" -- {remove_folder_path}")
                destination_filesync_connector.remove_folder(remove_folder_path)

    for file in source_file_list:
        source_file_path = source_filesync_connector.resolve_path(source_path, file)
        if any(re.match(ignore_regex, source_file_path) for ignore_regex in configs.file_ignore_regex_list):
            prints.yellow(f" !! {source_file_path}")
            continue
        destination_file_path = destination_filesync_connector.resolve_path(destination_path, file)
        if source_file_path in configs.file_rename_dict:
            destination_file_path = configs.file_rename_dict[source_file_path]
            del configs.file_rename_dict[source_file_path]
            prints.purple(f" || {source_file_path} -> {destination_file_path}")
        if file in destination_file_list:
            if source_filesync_connector.get_m_time(source_file_path) > destination_filesync_connector.get_m_time(destination_file_path) or configs.is_force or is_force:
                prints.green(f" -> {destination_file_path}")
                destination_filesync_connector.write_file(source_filesync_connector.read_file(source_file_path), destination_file_path)
            if destination_filesync_connector.get_m_time(destination_file_path) > source_filesync_connector.get_m_time(source_file_path) and configs.is_dual:
                prints.blue(f" <- {destination_file_path}")
                source_filesync_connector.write_file(destination_filesync_connector.read_file(destination_file_path), source_file_path)
            destination_file_list.remove(file)
            continue
        prints.green(f" ++ {destination_file_path}")
        destination_filesync_connector.write_file(source_filesync_connector.read_file(source_file_path), destination_file_path)

    for file in destination_file_list:
        remove_file_path = destination_filesync_connector.resolve_path(destination_path, file)
        if any(re.match(ignore_regex, remove_file_path) for ignore_regex in configs.file_ignore_regex_list):
            continue
        if configs.is_delete:
            prints.red(f" -- {remove_file_path}")
            destination_filesync_connector.remove_file(remove_file_path)
