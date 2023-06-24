'''
utils.py
'''
import re

from utils import logs



def sync(filesync_connector_source, source_path, filesync_connector_destination, destination_path, filesync_configs):
    '''
    pass
    '''
    logs.debug(f"(utils.sync) filesync_connector_source: {filesync_connector_source}, source_path: {source_path}, filesync_connector_destination: {filesync_connector_destination}, destination_path: {destination_path}, filesync_configs: {filesync_configs}")
    folder_list_source = []
    file_list_source = []
    for entry in filesync_connector_source.entry_list(source_path):
        if filesync_connector_source.is_folder(source_path, entry):
            folder_list_source.append(entry)
        else:
            file_list_source.append(entry)
    folder_list_source.sort()
    file_list_source.sort()

    folder_list_destination = []
    file_list_destination = []
    for entry in filesync_connector_destination.entry_list(destination_path):
        if filesync_connector_destination.is_folder(destination_path, entry):
            folder_list_destination.append(entry)
        else:
            file_list_destination.append(entry)
    folder_list_destination.sort()
    file_list_destination.sort()

    for folder in folder_list_source:
        folder_path_source = filesync_connector_source.resolve_path(source_path, folder)
        is_ignore = False
        for ignore_regex in filesync_configs.ignore_regex_list_folder:
            is_ignore = is_ignore or re.match(ignore_regex, folder_path_source)
        if not is_ignore:
            folder_path_destination = filesync_connector_destination.resolve_path(destination_path, folder)
            if folder_path_source in filesync_configs.rename_dict_folder:
                folder_path_destination = filesync_configs.rename_dict_folder[folder_path_source]
                del filesync_configs.rename_dict_folder[folder_path_source]
                logs.print_purple(f" || {folder_path_source} -> {folder_path_destination}")
            if folder not in folder_list_destination:
                filesync_connector_destination.make_folder(folder_path_destination)
            logs.print_purple(f" ?? {folder_path_destination}")
            sync(filesync_connector_source, folder_path_source, filesync_connector_destination, folder_path_destination, filesync_configs)
            if folder in folder_list_destination:
                folder_list_destination.remove(folder)
        else:
            logs.print_yellow(f" !! {folder_path_source}")

    for folder in folder_list_destination:
        folder_path_remove = filesync_connector_destination.resolve_path(destination_path, folder)
        is_ignore = False
        for ignore_regex in filesync_configs.ignore_regex_list_folder:
            is_ignore = is_ignore or re.match(ignore_regex, folder_path_remove)
        if not is_ignore:
            if filesync_configs.is_delete:
                logs.print_red(f" -- {folder_path_remove}")
                filesync_connector_destination.remove_folder(folder_path_remove)

    for file in file_list_source:
        file_path_source = filesync_connector_source.resolve_path(source_path, file)
        is_ignore = False
        for ignore_regex in filesync_configs.ignore_regex_list_file:
            is_ignore = is_ignore or re.match(ignore_regex, file_path_source)
        if not is_ignore:
            file_path_destination = filesync_connector_destination.resolve_path(destination_path, file)
            if file_path_source in filesync_configs.rename_dict_file:
                file_path_destination = filesync_configs.rename_dict_file[file_path_source]
                del filesync_configs.rename_dict_file[file_path_source]
                logs.print_purple(f" || {file_path_source} -> {file_path_destination}")
            if file in file_list_destination:
                if filesync_connector_source.m_time(file_path_source) > filesync_connector_destination.m_time(file_path_destination):
                    logs.print_green(f" -> {file_path_destination}")
                    filesync_connector_destination.write_file(filesync_connector_source.read_file(file_path_source), file_path_destination)
                elif filesync_configs.is_dual and filesync_connector_destination.m_time(file_path_destination) > filesync_connector_source.m_time(file_path_source):
                    logs.print_blue(f" <- {file_path_destination}")
                    filesync_connector_source.write_file(filesync_connector_destination.read_file(file_path_destination), file_path_source)
                file_list_destination.remove(file)
            else:
                logs.print_green(f" ++ {file_path_destination}")
                filesync_connector_destination.write_file(filesync_connector_source.read_file(file_path_source), file_path_destination)
        else:
            logs.print_yellow(f" !! {file_path_source}")

    for file in file_list_destination:
        file_path_remove = filesync_connector_destination.resolve_path(destination_path, file)
        is_ignore = False
        for ignore_regex in filesync_configs.ignore_regex_list_file:
            is_ignore = is_ignore or re.match(ignore_regex, file_path_remove)
        if not is_ignore:
            if filesync_configs.is_delete:
                logs.print_red(f" -- {file_path_remove}")
                filesync_connector_destination.remove_file(file_path_remove)
