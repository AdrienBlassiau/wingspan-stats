import configparser

from src.path import Path
from src.utils import Utils


class Config:
    """
    This class manages the parameters stored on config file
    """
    def __init__(self):
        config = configparser.ConfigParser()
        Utils.create_file_if_not_exist(Path.get_ini_model_path(), Path.get_ini_path())
        config.read(Path.get_ini_path())

        self.language = config.get('DEFAULT', 'Language')
