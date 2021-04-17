import os

from definitions import ROOT_DIR


class Path:
    DEFAULT_INPUT_PATH = ROOT_DIR + "/input/"
    DEFAULT_OUTPUT_PATH = ROOT_DIR + "/output/"
    DEFAULT_DATA_PATH = ROOT_DIR + "/data/"
    DEFAULT_INI_PATH = ROOT_DIR + "/"
    DEFAULT_SCORE_OUTPUT_FILE_FORMAT = "score_{player_name}.png"
    DEFAULT_SCORE_FILE = "scores.csv"
    DEFAULT_I18N_FILE = "i18n.csv"
    DEFAULT_INI_FILE = "wingspan.stats.ini"
    DEFAULT_INI_MODEL_FILE = "wingspan.stats.model.ini"

    @staticmethod
    def get_output_save_path(player_name):
        return os.path.join(Path.DEFAULT_OUTPUT_PATH, Path.DEFAULT_SCORE_OUTPUT_FILE_FORMAT.format(player_name=player_name))

    @staticmethod
    def get_score_path():
        return os.path.join(Path.DEFAULT_INPUT_PATH, Path.DEFAULT_SCORE_FILE)

    @staticmethod
    def get_i18n_path():
        return os.path.join(Path.DEFAULT_DATA_PATH, Path.DEFAULT_I18N_FILE)

    @staticmethod
    def get_ini_path():
        return os.path.join(Path.DEFAULT_INI_PATH, Path.DEFAULT_INI_FILE)

    @staticmethod
    def get_ini_model_path():
        return os.path.join(Path.DEFAULT_DATA_PATH, Path.DEFAULT_INI_MODEL_FILE)