import os
import platform
import logging

def get_documents_path():
    system_platform = platform.system()
    if system_platform == 'Windows':
        return os.path.join(os.environ['USERPROFILE'], 'Documents')
    elif system_platform == 'Darwin':
        return os.path.join(os.path.expanduser('~'), 'Documents')
    else:
        return os.path.join(os.path.expanduser('~'), 'Documents')

def get_music_folder_path():
    documents_path = get_documents_path()
    music_folder_path = os.path.join(documents_path, 'Music')
    if not os.path.exists(music_folder_path):
        os.mkdir(music_folder_path)
    return music_folder_path

def setup_logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
