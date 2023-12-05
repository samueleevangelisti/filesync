'''
environments.py
'''
from utils import paths



IS_DEVELOPMENT = False
IS_PRODUCTION = not IS_DEVELOPMENT

IS_LOG_FILE = not IS_DEVELOPMENT
LOG_FOLDER_PATH = None
if IS_LOG_FILE:
    LOG_FOLDER_PATH = paths.resolve_path(paths.folder_path(__file__), 'logs')
